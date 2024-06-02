:: Make sure to create the repo prior to running
git init
git add .
git commit -m "Initial commit."

:: Create main branch
git branch -M main
git remote add origin https://github.com/56kyle/{{cookiecutter.project_name}}.git
git push -u origin main

:: Create develop branch
git -c credential.helper= -c core.quotepath=false -c log.showSignature=false checkout -b develop main^0 --
git push -u origin develop

:: Install poetry
poetry env use %PYTHON39%
poetry install --with dev
poetry build

:: Install pre-commit hooks
nox -s pre-commit -- install

:: Update poetry.lock
poetry update
git add .
git commit -m "Runs poetry update."
git push

:: Creates first release
git -c credential.helper= -c core.quotepath=false -c log.showSignature=false checkout -b release/0.0.1 develop^0 --
poetry version patch
git add .
git commit -m "Bumps version to 0.0.1."
git push -u origin release/0.0.1

