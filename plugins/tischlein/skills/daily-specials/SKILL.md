---
name: daily-specials
description: 'Publish daily specials and lunch menus, and mark dishes sold out or available again. Use for "Tagesgericht", "Mittagstisch", "Tageskarte", "heute gibt es", "Gericht ausverkauft", "wieder verfügbar", "daily specials", "lunch menu" or "mark as sold out".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "daily-specials"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
