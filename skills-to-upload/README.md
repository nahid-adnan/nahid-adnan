# Skills to upload to your Claude account

These are upload-ready skill packages. Each `.zip` contains a single skill
folder with a `SKILL.md` at its top level — the format the claude.ai Skills
uploader expects.

## How to add them to your Claude account (web / Cowork / Code-on-web)

1. Download a `.zip` from this folder.
2. Go to **claude.ai** → **Settings** → **Capabilities** (labeled **Features**
   on some accounts) → **Skills**.
3. Click **Upload skill** and select the `.zip`.
4. Toggle the skill **on**.

If there is no **Skills** section, custom-skill upload may not be enabled for
your plan/account yet — that is an account-level setting, not something a
session can change.

## What's here

| File | Source | Notes |
|------|--------|-------|
| `academy-guide.zip` | anthropics/skills (Apache-2.0) | Recommends Claude Academy courses/tutorials. |
| `claude-api.zip` | anthropics/skills (Apache-2.0) | Reference for the Claude API / Anthropic SDK. Developer-oriented. |
| `discernment-nudge.zip` | anthropics/skills (Apache-2.0) | Prompts a sanity-check after actionable answers. |
| `frontend-design.zip` | anthropics/skills (Apache-2.0) | Visual-design guidance for building UI. Developer-oriented. |
| `webapp-testing.zip` | anthropics/skills (Apache-2.0) | Playwright-based local web-app testing. Developer-oriented. |
| `composio.zip` | ComposioHQ/composio | Router/guidance for Composio apps (Gmail, Slack, GitHub, Notion, ...). Needs the Composio MCP set up to actually take actions. |

## Alternative: local Claude Code install

To install any of these into the **Claude Code CLI on your own machine**
(a separate store from your account), use the community `skills` CLI, e.g.:

```bash
npx skills add ComposioHQ/composio --skill composio -g -y
```

That installs locally under `~/.claude/skills/`; it does **not** add the skill
to your claude.ai web chat — only the `.zip` upload above does that.
