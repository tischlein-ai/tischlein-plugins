---
name: setup-spa
description: 'Set up and run the spa of a hotel or day spa: areas, saunas, treatment rooms, therapists, treatments from a price list, Aufguss and class plans, day passes, 10er cards, Spa-Tage, policies, health questionnaires, the spa pages, stays with room charges, desk bookings and offers for free hours. Use for "Spa einrichten", "Wellness", "Sauna", "Aufgussplan", "Behandlungen", "Massage buchen", "Preisliste Spa", "Tageskarte", "Spa-Tag", "Zimmer belasten", "set up the spa".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "setup-spa"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
