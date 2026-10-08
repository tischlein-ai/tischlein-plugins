---
name: weekly-review
description: 'Summarise the venue''s week: website statistics, wishlist insights, open inquiries, Google reviews, sold-out dishes and stale content, with suggested next steps. Use for "Wochenrückblick", "wie lief die Woche", "Statistiken", "Wochenbericht", "was ist offen", "weekly review" or "how did we do this week".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "weekly-review"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
