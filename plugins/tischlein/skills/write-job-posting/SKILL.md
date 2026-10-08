---
name: write-job-posting
description: 'Write or revise a job posting for kitchen, service or bar staff and publish it on the venue website. Use for "Stellenanzeige schreiben", "Koch gesucht", "Servicekraft suchen", "Aushilfe gesucht", "Minijob ausschreiben", "write a job posting" or "we are hiring".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "write-job-posting"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
