# Tree Menu Django App

This is a reusable Django app that renders a dynamic, tree-structured menu on any page using a template tag.

---

## ✅ Features

- Tree structure menu (parent-child)
- Active item detection based on current URL
- Expand parents and children of the active item
- Manage menu and items via Django admin panel
- Named URL or explicit URL support
- Only **1 database query per menu**
- Multiple menus on the same page using `{% draw_menu "menu_name" %}`

---

## 🚀 Setup

### 1. Clone the project

```bash
git clone https://github.com/AbdelrahmanAbdel-Aal/django-tree-menu.git
cd django-tree-menu


2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

3. Install dependencies
pip install django

4. Run migrations
python manage.py makemigrations
python manage.py migrate

5. Create superuser
python manage.py createsuperuser

6. Run the server
python manage.py runserver

🧱 How to use
1- Go to /admin

2- Add a Menu (e.g. name: main)

3- Add MenuItem objects under that menu. Use the parent field to nest them.

4- In your templates, use:
    {% load menu_tags %}
    {% draw_menu "main" %}


📁 Project Structure
TreeMenu_project/
├── manage.py
├── treemenu_project/
│   └── settings.py, urls.py, ...
├── menu/
│   ├── models.py
│   ├── admin.py
│   ├── templatetags/
│   │   └── menu_tags.py
│   ├── templates/
│   │   └── menu/
│   │       ├── menu.html
│   │       └── menu_item.html
├── templates/
│   └── home.html
├── README.md
└── db.sqlite3

