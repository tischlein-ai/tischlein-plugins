---
name: insights
description: 'Answer the owner''s business questions from measured figures: profit of a day, week or month, day summary, dishes that earn no money, what more or less of, peak hours, goods cost, waste. Use for "Wie profitabel war der Tag", "Was haben wir verdient", "Fass den Tag zusammen", "Welche Gerichte verdienen kein Geld", "Renner und Penner", "Wovon mehr, wovon weniger", "Wann ist am meisten los", "Wareneinsatz", "Schwund", "Stornos", "Ø-Bon", "profit report", "menu engineering".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "insights"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
