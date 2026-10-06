# Tischlein – plugin for Claude & ChatGPT

🇩🇪 **Deutsche Version: [README.md](README.md)**

**Tischlein** runs websites, menus and guest requests for restaurants, cafés, bars and Kneipen. There is no admin backend: the team manages everything by talking to Claude or ChatGPT, with a preview before every write.

This repository is the `tischlein` plugin marketplace. The `tischlein` plugin bundles the Tischlein MCP server (`https://tischlein.pro/mcp`) and **skills** that activate on natural phrases ("import our menu from this PDF"). The skills here are **stubs** only: description and trigger phrases. The actual playbook is served live by the server through the MCP tool `get-guidance`, so it is current after every Tischlein deploy without reinstalling the plugin.

> ⚠️ **Generated.** This repository is generated from the Tischlein app (published on every merge to `main`). Manual edits are overwritten.

Version: **1.49.0**

## Skills

| Skill | `get-guidance` topic | Server-side guidance |
|---|---|---|
| `answer-inquiries` | `answer-inquiries` | available |
| `answer-reviews` | `answer-reviews` | available |
| `audit-allergens` | `audit-allergens` | available |
| `capture-applicant` | `capture-applicant` | available |
| `daily-specials` | `daily-specials` | available |
| `go-live` | `go-live` | available |
| `import-menu-from-pdf` | `import-menu-from-pdf` | available |
| `migrate-website` | `migrate-website` | available |
| `month-close` | `month-close` | available |
| `newsletter` | `newsletter` | available |
| `onboard-restaurant` | `onboard-restaurant` | available |
| `plan-shifts` | `plan-shifts` | available |
| `purchasing` | `purchasing` | available |
| `sell-vouchers-and-tickets` | `sell-vouchers-and-tickets` | available |
| `send-feedback` | `send-feedback` | available |
| `setup-event-location` | `setup-event-location` | available |
| `staff-tasks` | `staff-tasks` | available |
| `suggest-landing-pages` | `suggest-landing-pages` | available |
| `theme-authoring` | `theme-authoring` | available |
| `translate-site` | `translate-site` | available |
| `weekly-review` | `weekly-review` | partial, rest with milestone 5 |
| `write-job-posting` | `write-job-posting` | available |
| `write-news-post` | `write-news-post` | available |

While a playbook is not published yet, `get-guidance` answers with the milestone it comes with and what already works today; the skill says so and continues with `overview` and the general tools. For questions about how Tischlein works, `get-guidance` also searches the Tischlein documentation (`search`, `read`). Any skill can also be started explicitly, e.g. `/tischlein:import-menu-from-pdf`.

## Installation

### Claude Desktop and Claude Code (recommended: hosted marketplace)

```
/plugin marketplace add https://tischlein.pro/plugins/marketplace.json
/plugin install tischlein@tischlein
```

Alternatively via GitHub: `/plugin marketplace add tischlein-ai/tischlein-plugins`.

The connector login happens in a Claude Code session: `/mcp` → **tischlein** → **Authenticate**, sign in to Tischlein in the browser and enter the 6-digit code. In chat, use a custom connector instead (see below). Claude Code also prompts on the first tool call.

Updating: `/plugin marketplace update tischlein`, then `/plugin update tischlein@tischlein`.

### Claude Desktop / claude.ai / Cowork (connector)

Without the plugin: **Settings → Connectors → Add custom connector** with the URL

```
https://tischlein.pro/mcp
```

Sign-in via OAuth. All tools are available; Claude fetches the playbooks through `get-guidance`.

### ChatGPT / Codex

- **ChatGPT:** Settings → Apps & Connectors → (developer mode) → create a connector with the URL `https://tischlein.pro/mcp`, authentication OAuth.
- **Codex:** `codex plugin marketplace add tischlein-ai/tischlein-plugins`, then `codex plugin add tischlein@tischlein` and `codex mcp login tischlein`. Without the plugin: `codex mcp add tischlein --url https://tischlein.pro/mcp`.

## Security

- The plugin carries no data and no workflow instructions – only trigger phrases. Everything else is served by the server after sign-in, within your permissions.
- Every write is shown as a preview first (`confirmed:false`) and only runs after you confirm.

## Layout

```
.claude-plugin/marketplace.json        Claude Code marketplace "tischlein"
.agents/plugins/marketplace.json       Codex/ChatGPT marketplace
plugins/tischlein/
  .claude-plugin/plugin.json           Claude plugin manifest
  .mcp.json                            MCP server for Claude (http)
  plugin.json, mcp.json                portable Agent Plugins package (OpenAI, streamable-http)
  .codex-plugin/plugin.json            Codex fallback manifest
  skills/<slug>/SKILL.md               stub skills
  skills/<slug>/scripts/               helper scripts (Python 3, no dependencies)
```
