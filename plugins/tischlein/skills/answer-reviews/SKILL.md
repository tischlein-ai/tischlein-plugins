---
name: answer-reviews
description: 'Answer Google reviews: fetch the unanswered ones, draft personal replies in the venue''s voice and the review''s language, show every draft to the owner and publish only approved texts. Use for "Bewertungen beantworten", "neue Google-Bewertungen", "auf Rezension antworten", "schlechte Bewertung", "1-Stern-Bewertung", "answer reviews" or "reply to Google reviews".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "answer-reviews"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
