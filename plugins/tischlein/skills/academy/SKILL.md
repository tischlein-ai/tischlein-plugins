---
name: academy
description: 'The tischlein Akademie: short learning videos with a quiz. Find what to learn next, explain progress, quiz and points to staff and owners, and import and publish episodes as platform admin. Use for "Was soll ich als Nächstes lernen?", "Akademie", "Lernvideo", "Quiz", "Unterweisung", "academy", "what should I learn next".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "academy"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
