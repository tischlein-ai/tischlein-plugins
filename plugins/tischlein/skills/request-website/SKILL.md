---
name: request-website
description: 'Ask tischlein to build a new website or move the existing one: take the request with its questionnaire (old website, style, menu, reservations, languages, domain, photos, go-live, contact) over one or several sessions. tischlein builds it for the venue; the owner follows it in the app. Use for "neue Website", "Website erstellen", "Website umziehen", "Website migrieren", "von WordPress/Wix zu tischlein", "build my website" or "move our site to tischlein".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "request-website"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
