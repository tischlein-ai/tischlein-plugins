---
name: capture-applicant
description: 'Capture a job applicant who applied outside the website form (WhatsApp chat, screenshot, email, phone call, walk-in) and create the application in Tischlein with the responsible person. Use for "Bewerbung per WhatsApp", "Bewerber anlegen", "hat sich per WhatsApp beworben", "Bewerbung erfassen", "neuer Bewerber", "capture applicant" or "add this applicant".'
---

Call the Tischlein MCP tool `get-guidance` with `topic: "capture-applicant"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
