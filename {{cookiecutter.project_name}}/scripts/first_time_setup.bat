:: Make sure to create the repo prior to running
git init
git add .
git commit -m "Initial commit."
git branch -M main
git remote add origin https://github.com/56kyle/{{cookiecutter.project_name}}.git
git push -u origin main
poetry install --with dev
poetry build
