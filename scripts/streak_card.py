#!/usr/bin/env python3
"""Build an animated contribution-streak card from GitHub's own API.

No third-party card service involved, so nothing here can 503 on us.
Colours match the github_dark theme used by the summary cards above it.
"""
import json, os, sys, urllib.request
from datetime import date, datetime, timedelta, timezone

USER  = os.environ.get("STREAK_USER", "nahid-adnan")
TOKEN = os.environ.get("GH_TOKEN", "")
OUT   = os.environ.get("STREAK_OUT", "assets/streak.svg")

BG, TEXT, MUTED, ACCENT, RULE = "#0D1117", "#C9D1D9", "#8B949E", "#58A6FF", "#30363D"

Q = """
query($login:String!,$from:DateTime!,$to:DateTime!){
  user(login:$login){
    createdAt
    contributionsCollection(from:$from,to:$to){
      contributionCalendar{
        weeks{ contributionDays{ date contributionCount } }
      }
    }
  }
}"""

def gql(variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": Q, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {TOKEN}",
                 "Content-Type": "application/json",
                 "User-Agent": "streak-card"})
    with urllib.request.urlopen(req, timeout=45) as r:
        payload = json.load(r)
    if "errors" in payload:
        raise RuntimeError(payload["errors"])
    return payload["data"]["user"]

def collect():
    """Walk year by year from account creation to today."""
    today = datetime.now(timezone.utc)
    first = gql({"login": USER,
                 "from": (today - timedelta(days=364)).isoformat(),
                 "to": today.isoformat()})
    created = datetime.fromisoformat(first["createdAt"].replace("Z", "+00:00"))

    days, cursor = {}, created
    while cursor < today:
        window = min(cursor + timedelta(days=364), today)
        data = gql({"login": USER, "from": cursor.isoformat(), "to": window.isoformat()})
        for wk in data["contributionsCollection"]["contributionCalendar"]["weeks"]:
            for d in wk["contributionDays"]:
                days[d["date"]] = d["contributionCount"]
        cursor = window + timedelta(days=1)
    return created.date(), days

def streaks(days):
    if not days:
        return 0, 0, None, None, 0, None, None
    keys  = sorted(days)
    total = sum(days.values())
    today = date.today()

    best = cur = 0
    best_start = best_end = None
    run_start = None
    for k in keys:
        if days[k] > 0:
            cur += 1
            if run_start is None:
                run_start = k
            if cur > best:
                best, best_start, best_end = cur, run_start, k
        else:
            cur, run_start = 0, None

    # current streak: walk back from today. today counting zero is fine,
    # the day isn't over yet.
    cur_len, cur_start, d = 0, None, today
    if days.get(d.isoformat(), 0) == 0:
        d -= timedelta(days=1)
    while days.get(d.isoformat(), 0) > 0:
        cur_len += 1
        cur_start = d
        d -= timedelta(days=1)
    return total, cur_len, cur_start, today if cur_len else None, best, best_start, best_end

def fmt(d):
    return d.strftime("%b ") + str(d.day) if d else ""

def build(created, total, cur, cur_start, best, best_start, best_end):
    W, H = 495, 195
    third = W / 3
    cx    = W / 2
    rng   = f"{fmt(created)} - Present"
    cur_rng  = f"{fmt(cur_start)}" if cur else "—"
    best_rng = f"{fmt(best_start)} - {fmt(best_end)}" if best else "—"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Contribution streak">
<style>
  text {{ font-family:'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif; }}
  .num  {{ font-size:38px; font-weight:700; fill:{ACCENT}; }}
  .lab  {{ font-size:13.5px; font-weight:600; fill:{TEXT}; }}
  .dt   {{ font-size:11.5px; fill:{MUTED}; }}
  .curLab {{ font-size:13.5px; font-weight:700; fill:{ACCENT}; }}
  .fade {{ opacity:0; animation:fade .7s ease-out forwards; }}
  @keyframes fade {{ to {{ opacity:1; }} }}
  .ring {{ fill:none; stroke:{ACCENT}; stroke-width:5;
           stroke-dasharray:264; stroke-dashoffset:264;
           animation:draw 1.1s cubic-bezier(.4,0,.2,1) .3s forwards; }}
  @keyframes draw {{ to {{ stroke-dashoffset:0; }} }}
  .flame {{ animation:flick 1.9s ease-in-out infinite; transform-origin:center; }}
  @keyframes flick {{ 0%,100% {{ opacity:.85; }} 50% {{ opacity:1; }} }}
  .frame {{ fill:none; stroke-width:2; animation:hue 9s linear infinite; }}
  @keyframes hue {{ 0% {{stroke:#58A6FF}} 20% {{stroke:#A371F7}} 40% {{stroke:#F778BA}}
                    60% {{stroke:#FFD43B}} 80% {{stroke:#3FB950}} 100% {{stroke:#58A6FF}} }}
</style>
  <rect width="{W}" height="{H}" rx="7" fill="{BG}"/>

  <line x1="{third:g}" y1="34" x2="{third:g}" y2="{H-34}" stroke="{RULE}" stroke-width="1"/>
  <line x1="{2*third:g}" y1="34" x2="{2*third:g}" y2="{H-34}" stroke="{RULE}" stroke-width="1"/>

  <g class="fade" style="animation-delay:.10s">
    <text class="num" x="{third/2:g}" y="86"  text-anchor="middle">{total}</text>
    <text class="lab" x="{third/2:g}" y="116" text-anchor="middle">Total Contributions</text>
    <text class="dt"  x="{third/2:g}" y="140" text-anchor="middle">{rng}</text>
  </g>

  <g class="fade" style="animation-delay:.25s">
    <circle class="ring" cx="{cx:g}" cy="82" r="42"/>
    <text class="num" x="{cx:g}" y="95" text-anchor="middle">{cur}</text>
    <text class="curLab" x="{cx:g}" y="140" text-anchor="middle">Current Streak</text>
    <text class="dt" x="{cx:g}" y="162" text-anchor="middle">{cur_rng}</text>
    <g class="flame">
      <path d="M{cx:g} 28 c 5 7 -3 9 0 15 c 4 -2 5 -7 4 -10 c 5 4 7 10 4 15 c -2 4 -6 6 -8 6 c -6 0 -11 -4 -11 -10 c 0 -8 8 -11 11 -16 z" fill="{ACCENT}"/>
    </g>
  </g>

  <g class="fade" style="animation-delay:.40s">
    <text class="num" x="{2.5*third:g}" y="86"  text-anchor="middle">{best}</text>
    <text class="lab" x="{2.5*third:g}" y="116" text-anchor="middle">Longest Streak</text>
    <text class="dt"  x="{2.5*third:g}" y="140" text-anchor="middle">{best_rng}</text>
  </g>

  <rect class="frame" x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="7"/>
</svg>
'''

if __name__ == "__main__":
    if not TOKEN:
        print("::error::GH_TOKEN is empty"); sys.exit(1)
    created, days = collect()
    total, cur, cur_start, _, best, best_start, best_end = streaks(days)
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    open(OUT, "w").write(build(created, total, cur, cur_start, best, best_start, best_end))
    print(f"{OUT}: total={total} current={cur} longest={best} days_seen={len(days)}")
