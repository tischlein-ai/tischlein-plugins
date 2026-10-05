---
name: import-menu-from-pdf
description: 'Import a menu from a PDF, photo or old web page into Tischlein dishes, sections and menus, including prices, allergens and additives, with a preview before anything is saved. Use for "Speisekarte importieren", "Karte aus PDF übernehmen", "Speisekarte abtippen", "Getränkekarte hochladen", "import menu from PDF" or "upload our menu".'
---

Call the Tischlein MCP tool `get-guidance` with `topic: "import-menu-from-pdf"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
