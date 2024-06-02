:: Make sure to create the repo prior to running
git init
git add .
git commit -m "Initial commit."

:: Create main branch
git branch -M main
git remote add origin https://github.com/56kyle/{{cookiecutter.project_name}}.git
git push -u origin main

:: Install poetry
poetry env use %PYTHON39%
poetry install --with dev
poetry build

:: Install pre-commit hooks
nox -s pre-commit -- install

:: Update poetry.lock
poetry update
git add .
git commit --message="Runs poetry update."
git push

:: Creates first release
git switch --create release main
poetry version patch
git commit --message="{{cookiecutter.project_name}} 0.0.1" pyproject.toml
git push origin release

:: Switch back to main
git checkout main

:: Create develop branch
git switch -c develop
git push -u origin develop
