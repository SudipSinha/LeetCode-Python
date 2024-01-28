pdm run black src tests
pdm run ruff src tests
pdm run coverage run -m pytest && pdm run coverage report --show-missing
