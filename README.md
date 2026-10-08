# Tischlein – Plugin für Claude & ChatGPT

🇬🇧 **English version: [README.en.md](README.en.md)**

**Tischlein** betreibt Websites, Speisekarten und Gästeanfragen für Restaurants, Cafés, Bars und Kneipen. Es gibt kein Admin-Backend: Ihr Team pflegt alles im Gespräch mit Claude oder ChatGPT – mit einer Vorschau vor jeder Änderung.

Dieses Repository ist der Plugin-Marketplace `tischlein`. Das Plugin `tischlein` bringt den Tischlein-MCP-Server (`https://tischlein.pro/mcp`) und **Skills** mit, die auf natürliche Sätze reagieren („Importiere unsere Speisekarte aus diesem PDF“). Die Skills hier sind nur **Stubs**: Beschreibung und Auslöser-Phrasen. Die eigentliche Anleitung liefert der Server live über das MCP-Tool `get-guidance` – sie ist also nach jedem Tischlein-Deploy aktuell, ohne das Plugin neu zu installieren.

> ⚠️ **Generiert.** Dieses Repository wird automatisch aus der Tischlein-App erzeugt (veröffentlicht bei jedem Merge auf `main`). Manuelle Änderungen werden überschrieben.

Version: **1.62.0**

## Skills

| Skill | `get-guidance`-Topic | Server-Anleitung |
|---|---|---|
| `answer-inquiries` | `answer-inquiries` | verfügbar |
| `answer-reviews` | `answer-reviews` | verfügbar |
| `audit-allergens` | `audit-allergens` | verfügbar |
| `capture-applicant` | `capture-applicant` | verfügbar |
| `daily-specials` | `daily-specials` | verfügbar |
| `go-live` | `go-live` | verfügbar |
| `import-menu-from-pdf` | `import-menu-from-pdf` | verfügbar |
| `migrate-website` | `migrate-website` | verfügbar |
| `month-close` | `month-close` | verfügbar |
| `newsletter` | `newsletter` | verfügbar |
| `onboard-restaurant` | `onboard-restaurant` | verfügbar |
| `plan-shifts` | `plan-shifts` | verfügbar |
| `purchasing` | `purchasing` | verfügbar |
| `sell-vouchers-and-tickets` | `sell-vouchers-and-tickets` | verfügbar |
| `send-feedback` | `send-feedback` | verfügbar |
| `setup-event-location` | `setup-event-location` | verfügbar |
| `staff-tasks` | `staff-tasks` | verfügbar |
| `suggest-landing-pages` | `suggest-landing-pages` | verfügbar |
| `theme-authoring` | `theme-authoring` | verfügbar |
| `translate-site` | `translate-site` | verfügbar |
| `weekly-review` | `weekly-review` | teilweise, Rest mit Meilenstein 5 |
| `write-job-posting` | `write-job-posting` | verfügbar |
| `write-news-post` | `write-news-post` | verfügbar |

Solange eine Anleitung noch nicht veröffentlicht ist, antwortet `get-guidance` mit dem Meilenstein, mit dem sie kommt, und mit dem, was heute schon geht; der Skill sagt das offen und arbeitet mit `overview` und den allgemeinen Tools weiter. Für Fragen zur Bedienung durchsucht `get-guidance` außerdem die Tischlein-Dokumentation (`search`, `read`). Jeder Skill lässt sich auch direkt starten, z. B. `/tischlein:import-menu-from-pdf`.

## Installation

### Claude Desktop und Claude Code (empfohlen: gehosteter Marketplace)

```
/plugin marketplace add https://tischlein.pro/plugins/marketplace.json
/plugin install tischlein@tischlein
```

Alternativ über GitHub: `/plugin marketplace add tischlein-ai/tischlein-plugins`.

Die Anmeldung beim Connector läuft in einer Claude-Code-Sitzung über `/mcp` → **tischlein** → **Authenticate**: im Browser bei Tischlein anmelden und den 6-stelligen Code eingeben. In Claude im Chat geht es stattdessen über einen benutzerdefinierten Connector (siehe unten). Beim ersten Tool-Aufruf fragt Claude Code ohnehin danach.

Aktualisieren: `/plugin marketplace update tischlein`, dann `/plugin update tischlein@tischlein`.

### Claude Desktop / claude.ai / Cowork (Connector)

Ohne Plugin: **Einstellungen → Connectors → Benutzerdefinierten Connector hinzufügen** mit der URL

```
https://tischlein.pro/mcp
```

Anmeldung per OAuth. Alle Tools stehen dann bereit; die Anleitungen holt sich Claude über `get-guidance`.

### ChatGPT / Codex

- **ChatGPT:** Einstellungen → Apps & Connectors → (Entwicklermodus) → Connector anlegen mit der URL `https://tischlein.pro/mcp`, Authentifizierung OAuth.
- **Codex:** `codex plugin marketplace add tischlein-ai/tischlein-plugins`, dann `codex plugin add tischlein@tischlein` und `codex mcp login tischlein`. Ohne Plugin: `codex mcp add tischlein --url https://tischlein.pro/mcp`.

## Sicherheit

- Das Plugin enthält keine Daten und keine Arbeitsanweisungen – nur Auslöser-Phrasen. Alles andere liefert der Server nach Anmeldung, innerhalb Ihrer Rechte.
- Jede Schreibaktion wird zuerst als Vorschau gezeigt (`confirmed:false`) und erst nach Ihrer Bestätigung ausgeführt.

## Aufbau

```
.claude-plugin/marketplace.json        Claude-Code-Marketplace „tischlein“
.agents/plugins/marketplace.json       Codex/ChatGPT-Marketplace
plugins/tischlein/
  .claude-plugin/plugin.json           Claude-Plugin-Manifest
  .mcp.json                            MCP-Server für Claude (http)
  plugin.json, mcp.json                portables Agent-Plugins-Paket (OpenAI, streamable-http)
  .codex-plugin/plugin.json            Codex-Fallback-Manifest
  skills/<slug>/SKILL.md               Stub-Skills
  skills/<slug>/scripts/               Hilfsskripte (Python 3, ohne Abhängigkeiten)
```
