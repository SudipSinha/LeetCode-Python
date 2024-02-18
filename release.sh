set -e
pdm run ruff check --select I --fix src tests
pdm run ruff format src tests
pdm run mypy src tests
pdm run coverage run -m pytest && pdm run coverage report --show-missing
pdm build
