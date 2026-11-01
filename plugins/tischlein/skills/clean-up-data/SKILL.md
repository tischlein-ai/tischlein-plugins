---
name: clean-up-data
description: 'Find and clean up what is missing or not linked in the venue''s data — allergens, prices, recipes, stock articles, till mappings, supplier invoices, translations and legal texts — with progress in percent, asking the owner one point at a time. Use for "Datenqualität", "Daten aufräumen", "was fehlt noch", "ist alles verknüpft", "fehlende Allergene", "Gerichte ohne Rezept", "clean up data" or "data quality".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "clean-up-data"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
