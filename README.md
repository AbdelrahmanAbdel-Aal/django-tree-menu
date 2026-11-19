# Django Tree Menu — example project

A Django project demonstrating a named, tree-structured navigation menu with a custom template tag.

## Features visible in the source

- `Menu` and `MenuItem` models, including parent-child relationships and ordering.
- Menu management in the Django admin.
- Explicit paths or Django named routes for menu items.
- A `draw_menu` inclusion tag that identifies the current URL and its ancestor menu items.
- Tree rendering through Django templates.

> This repository is an example Django project; it is not presented as a published, installable Python package. The tag retrieves the menu and its items in separate queries, so it does not provide a one-query-per-menu guarantee. Additional ancestor lookups may occur. Performance has not been benchmarked.

## Getting started

Prerequisites: Python and Django. The checked-in project settings identify Django 5.2.3 as the generation version; the repository does not provide a standalone dependency manifest. Use a fresh environment, not the tracked `venv/`.

```bash
git clone https://github.com/AbdelrahmanAbdel-Aal/django-tree-menu.git
cd django-tree-menu
python -m venv .venv
```

Activate the virtual environment:

- **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
- **macOS/Linux:** `source .venv/bin/activate`

Install Django and initialise the database:

```bash
python -m pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

> Check the project's actual dependency versions and settings before using it for production. The examples above illustrate local development only.

## Create a menu

1. Open `/admin/` and sign in.
2. Create a **Menu**, such as `main`.
3. Add **MenuItem** records with titles, URLs, optional parent items and an ordering value.
4. Render the menu in a Django template:

```django
{% load menu_tags %}
{% draw_menu "main" %}
```

The inclusion tag reads `request` from its template context, so render the template with a request-aware context (for example, enable Django's request context processor).

## Where the implementation lives

- `menu/models.py` — menu data models and URL handling.
- `menu/admin.py` — Django admin registration.
- `menu/templatetags/menu_tags.py` — `draw_menu` logic.
- `menu/templates/menu/` — menu templates.
- `treemenu_project/` — project settings and URLs.

## Project status

This README was checked against the source; the setup commands have not been executed as an end-to-end smoke test. `menu/tests.py` currently contains no implemented test cases.

The checked-in settings enable debug mode and contain a development secret key. The repository also tracks a virtual environment, bytecode and a SQLite database. Treat this as a local example, not a production deployment configuration. No tracked files were removed as part of this documentation change.
