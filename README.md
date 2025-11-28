# datatalks_aidevtools — AI Dev Tools Workspace

This repository is a workspace for exercises done while following the DataTalksClub "AI Dev Tools" Zoomcamp. Each numbered folder contains an exercise or small project demonstrating a tool, technique, or workflow covered in the course.

Current content
- `01-todo/` — a minimal Django TODO app. See `01-todo/README.md` for details and quickstart instructions.

Purpose
- Keep a single place with worked examples and small projects while learning how to use developer tooling and AI-assisted workflows.

How to use this workspace
1. Clone the repository and open it in your editor of choice.

```powershell
git clone https://github.com/<youruser>/datatalks_aidevtools.git
cd datatalks_aidevtools
```

2. Create a virtual environment per-machine (recommended):

```powershell
python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process; .\.venv\Scripts\Activate.ps1
```

3. Install dependencies for the project you want to run. For the first exercise run:

```powershell
pip install -r requirements.txt
```

4. Follow the exercise-specific README inside each folder (`01-todo/README.md`).

Tests
- Each exercise should provide tests under its `tests/` folder. Run tests per-exercise to avoid conflicts:

```powershell
cd 01-todo
python ../manage.py test todo
```

Repository conventions
- Add a new folder for each exercise (e.g., `02-...`).
- Put exercise documentation in a `README.md` file inside the exercise folder.
- Keep long-running or heavy artifacts out of git (use `.gitignore` to exclude virtualenvs, data, and large files).

Credits & tools
- Course: DataTalksClub — AI Dev Tools Zoomcamp: https://github.com/DataTalksClub/ai-dev-tools-zoomcamp
- This workspace used AI assistance during development (chatbot: GPT-5 mini) to scaffold code and documentation.
