#!/usr/bin/env python3
"""Fetch the profile-details summary card and correct it from GitHub's own API.

The hosted card (github-profile-summary-cards) truncates the display name
("nahid-adnan (B M NAH...)") and serves stale numbers. This keeps its look and
rgb-soft animation, but:
  - shows the username only in the title,
  - replaces the contribution total with the same count the streak card uses,
  - replaces the public-repo count and public email with live values.
If anything unexpected happens, the previous committed card is left untouched.
"""
import importlib.util, json, os, re, sys, urllib.request
import xml.dom.minidom

USER  = os.environ.get("STREAK_USER", "nahid-adnan")
TOKEN = os.environ.get("GH_TOKEN", "")
OUT   = os.environ.get("PROFILE_OUT", "assets/cards/profile-details.svg")
CARD  = ("https://github-profile-summary-cards.vercel.app/api/cards/profile-details"
         f"?username={USER}&theme=github_dark&animation=rgb-soft")

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("streak_card", os.path.join(here, "streak_card.py"))
streak = importlib.util.module_from_spec(spec); spec.loader.exec_module(streak)

Q = """query($login:String!){ user(login:$login){
  email
  repositories(privacy:PUBLIC, ownerAffiliations:OWNER){ totalCount }
}}"""

def graphql(query, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json",
                 "User-Agent": "profile-card"})
    with urllib.request.urlopen(req, timeout=45) as r:
        payload = json.load(r)
    if "errors" in payload:
        raise RuntimeError(payload["errors"])
    return payload["data"]["user"]

def fix(svg, total, repos, email):
    out, n = re.subn(r'(<text[^>]*>)\s*' + re.escape(USER) + r'\s*\([^<]*\)\s*(</text>)',
                     r'\g<1>' + USER + r'\g<2>', svg, count=1)
    if n != 1:
        raise ValueError("title line not found")
    out, n = re.subn(r'(<text[^>]*>)\s*[\d,]+ Contributions on GitHub\s*(</text>)',
                     rf'\g<1>{total:,} Contributions on GitHub\g<2>', out, count=1)
    if n != 1:
        raise ValueError("contributions line not found")
    out, n = re.subn(r'(<text[^>]*>)\s*\d+ Public Repos?\s*(</text>)',
                     rf'\g<1>{repos} Public Repo{"" if repos == 1 else "s"}\g<2>', out, count=1)
    if n != 1:
        raise ValueError("public repos line not found")
    if email:
        out = re.sub(r'(<text[^>]*>)\s*[\w.+-]+@[\w-]+(?:\.[\w-]+)+\s*(</text>)',
                     rf'\g<1>{email}\g<2>', out, count=1)
    xml.dom.minidom.parseString(out.encode())   # must still be valid SVG
    return out

if __name__ == "__main__":
    if not TOKEN:
        print("::error::GH_TOKEN is empty"); sys.exit(1)
    try:
        _, days = streak.collect()
        total = streak.streaks(days)[0]
        user = graphql(Q, {"login": USER})
        req = urllib.request.Request(CARD, headers={"User-Agent": "profile-card"})
        svg = urllib.request.urlopen(req, timeout=60).read().decode("utf-8")
        email = user.get("email") or os.environ.get("PROFILE_EMAIL", "")
        card = fix(svg, total, user["repositories"]["totalCount"], email)
    except Exception as e:                       # keep the last good card
        print(f"::warning::profile card not updated: {e}"); sys.exit(0)
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    open(OUT, "w").write(card)
    print(f"{OUT}: total={total} repos={user['repositories']['totalCount']} email={'set' if user.get('email') else 'none'}")
