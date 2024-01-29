set -e
pdm run ruff src tests --fix
pdm run black src tests
pdm run mypy src tests
pdm run coverage run -m pytest && pdm run coverage report --show-missing
