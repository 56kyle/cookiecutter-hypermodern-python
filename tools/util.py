from pathlib import Path

import platformdirs


REPO_ROOT: Path = Path(__file__).parent.parent
REPO_POETRY_LOCK_PATH: Path = REPO_ROOT / "poetry.lock"

TEMPLATE_FOLDER: Path = REPO_ROOT / "{{cookiecutter.project_name}}"
TEMPLATE_POETRY_LOCK_PATH: Path = TEMPLATE_FOLDER / "poetry.lock"


HYPERMODERN_COOKIECUTTER_CACHE_FOLDER: Path = platformdirs.user_cache_path(
    appname="cookiecutter-hypermodern-python",
    appauthor="56kyle",
    ensure_exists=True
)

PROJECT_DEMOS_FOLDER: Path = HYPERMODERN_COOKIECUTTER_CACHE_FOLDER / "project_demos"
DEFAULT_DEMO_NAME: str = "demo-cookiecutter-project"

DEMO_FOLDER: Path = PROJECT_DEMOS_FOLDER / DEFAULT_DEMO_NAME
DEMO_POETRY_LOCK_PATH: Path = DEMO_FOLDER / "poetry.lock"



