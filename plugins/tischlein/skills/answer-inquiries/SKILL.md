---
name: answer-inquiries
description: 'Review open guest inquiries (table, event and catering requests), draft replies and confirm, decline or cancel them after the user approves. Use for "Anfragen beantworten", "offene Anfragen", "Reservierungsanfrage", "Feier anfragen", "Catering-Anfrage", "answer inquiries" or "reply to booking requests".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "answer-inquiries"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
