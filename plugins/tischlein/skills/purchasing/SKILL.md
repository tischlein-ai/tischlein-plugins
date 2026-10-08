---
name: purchasing
description: 'Ordering from suppliers ("Wareneinkauf"): set up suppliers, storage locations and the Warenliste from a list, photo, delivery note or invoice; mark what is low, build the order round, send each supplier only their lines (e-mail, WhatsApp, PDF), check deliveries. Use for "Lieferant anlegen", "Warenliste", "Einkaufsliste", "Bufala ist alle", "Was muss ich bestellen", "Schick die Bestellung", "Lieferung prüfen" or "supplier order".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "purchasing"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
