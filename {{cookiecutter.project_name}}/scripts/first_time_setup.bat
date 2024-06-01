:: Must set TWINE_USERNAME and TWINE_PASSWORD prior to running
git init
git add .
git commit -m "Initial commit."

poetry install --with dev
poetry build
