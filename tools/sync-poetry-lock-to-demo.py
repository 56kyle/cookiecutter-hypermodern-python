"""Script used for replacing the local poetry.lock with the poetry.lock in the demo project."""
import shutil
from pathlib import Path

from loguru import logger

from tools.util import DEFAULT_DEMO_NAME
from tools.util import PROJECT_DEMOS_FOLDER
from tools.util import TEMPLATE_FOLDER


def sync_poetry_lock_to_demo() -> None:
    demo_root: Path = PROJECT_DEMOS_FOLDER / DEFAULT_DEMO_NAME
    demo_poetry_lock_path: Path = _find_poetry_lock_path(demo_root)
    output_poetry_lock_path: Path = _find_poetry_lock_path(TEMPLATE_FOLDER)

    _copy_poetry_lock_from_demo(
        demo_poetry_lock_path=demo_poetry_lock_path,
        output_poetry_lock_path=output_poetry_lock_path
    )
    logger.info(f"Copied demo from {demo_poetry_lock_path=} to {output_poetry_lock_path=}.")


def _copy_poetry_lock_from_demo(
    demo_poetry_lock_path: Path,
    output_poetry_lock_path: Path
) -> None:
    """Copies over the poetry.lock from the provided demo project root."""
    shutil.copy(
        src=demo_poetry_lock_path,
        dst=output_poetry_lock_path
    )


def _find_poetry_lock_path(search_root: Path) -> Path:
    for path in search_root.rglob("poetry.lock"):
        return path
    raise FileNotFoundError(f"Failed to find a poetry.lock within the provided search path: {search_root=}")





