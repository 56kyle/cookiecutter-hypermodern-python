import shutil
import sys
from pathlib import Path

import shutil
import sys

import click

from cookiecutter.main import cookiecutter
from loguru import logger

from tools.util import DEFAULT_DEMO_NAME
from tools.util import PROJECT_DEMOS_FOLDER
from tools.util import REPO_ROOT


def generate_demo_project() -> Path:
    """Generates a demo project and returns its Path."""
    PROJECT_DEMOS_FOLDER.mkdir(exist_ok=True)
    _remove_any_existing_demo(PROJECT_DEMOS_FOLDER)
    cookiecutter(
        template=str(REPO_ROOT),
        no_input=True,
        extra_context={
            "project_name": DEFAULT_DEMO_NAME,
        },
        overwrite_if_exists=True,
        output_dir=str(PROJECT_DEMOS_FOLDER)
    )
    return PROJECT_DEMOS_FOLDER / DEFAULT_DEMO_NAME


def _remove_any_existing_demo(parent_path: Path) -> None:
    """Removes any existing demos."""
    for path in parent_path.iterdir():
        shutil.rmtree(path)


@click.command()
def main() -> None:
    """Geneates a demo project."""
    try:
        generate_demo_project()
    except Exception as error:
        click.secho(f"error: {error}", fg="red")
        sys.exit(1)


if __name__ == '__main__':
    main(prog_name="generate-demo-project")
