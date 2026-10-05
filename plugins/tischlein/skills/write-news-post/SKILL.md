---
name: write-news-post
description: 'Write and publish a news post for the venue website, such as holidays, new menus, events or opening-hour changes, in the venue''s voice and languages. Use for "News schreiben", "Beitrag schreiben", "Neuigkeit veröffentlichen", "Betriebsferien ankündigen", "write a news post" or "announce on the website".'
---

Call the Tischlein MCP tool `get-guidance` with `topic: "write-news-post"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
