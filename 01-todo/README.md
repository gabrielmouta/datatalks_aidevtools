# Todo App (Django)

A small TODO application built with Django as part of work on the DataTalksClub "AI Dev Tools" course. This repository contains a minimal Django project and a `todo` app with create/edit/delete functionality, due dates, and the ability to mark items as resolved.

**Features**
- Create, edit and delete TODOs
- Assign due dates
- Mark TODOs as resolved
- Simple admin registration and templates for quick testing

**Tech stack**
- Python 3.14.0
- Django 5.2.8

**Course / Credits**
- Based on exercises from: https://github.com/DataTalksClub/ai-dev-tools-zoomcamp
- Project scaffolded with help from a chatbot (GPT-5 mini).

**Quickstart (Windows PowerShell)**
1. Open a PowerShell terminal in the repository root (where `manage.py` lives).
2. Create and activate a virtual environment (adjust name if you used something else):

```powershell
python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process; .\.venv\Scripts\Activate.ps1
```

3. Upgrade pip and install dependencies (install Django):

```powershell
.\.venv\Scripts\python -m pip install --upgrade pip
pip install django==5.2.8
```

4. Run migrations and create a superuser:

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

5. Run the server and open the app in your browser:

```powershell
python manage.py runserver
# then open http://127.0.0.1:8000/
```

**Run tests**
- Activate your virtualenv (same command as above) and run:

```powershell
python manage.py test todo
```

If you run into a conflict with a globally installed top-level `tests` package, you can run the specific test files directly:

```powershell
python -m unittest todo.tests.test_models
python -m unittest todo.tests.test_views
```

**Important notes**
- Project-level templates are registered in `todoproject/settings.py` with `TEMPLATES['DIRS'] = [BASE_DIR / 'templates']` and `APP_DIRS = True`. App templates live under `todo/templates/todo/`.
- If you accidentally pushed your virtual environment to the remote, the repository now includes a `.gitignore` entry for the venv and the venv has been removed from tracking. If you want to remove the venv files from the repository history (to shrink the repo), consider using the BFG Repo-Cleaner or `git filter-branch` (these rewrite history and require a force-push; coordinate with collaborators).

**Project layout (important files)**
- `manage.py` — Django CLI entry
- `todoproject/` — Django project settings & URLs
- `todo/` — the app with `models.py`, `views.py`, `urls.py`, `admin.py`, and `templates/`
- `templates/` — project-level templates (`base.html`, `home.html`)
