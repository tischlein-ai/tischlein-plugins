---
name: send-feedback
description: 'Send feedback to the tischlein team: when the user hits a bug, misses a feature, is unhappy with tischlein or wants to praise it, draft a short reproducible report, show it and submit it after their OK. Use for "Feedback", "Fehler melden", "Bug melden", "Idee", "Verbesserungsvorschlag", "das funktioniert nicht", "warum geht das nicht", "send feedback" or "report a bug".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "send-feedback"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
