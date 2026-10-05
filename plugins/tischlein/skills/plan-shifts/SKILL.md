---
name: plan-shifts
description: 'Plan the weekly staff schedule: copy a week, add or move shifts, fill open shifts, check working-time rules (ArbZG, JArbSchG), absences and availability, and publish the plan to the team. Use for "Dienstplan", "Schichtplan erstellen", "wie diese Woche", "Samstag zwei mehr im Service", "Schicht tauschen", "wer arbeitet am", "plan shifts" or "staff schedule".'
---

Call the Tischlein MCP tool `get-guidance` with `topic: "plan-shifts"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
