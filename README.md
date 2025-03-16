#   LeetCode_Python
Python solutions of LeetCode problems and similar interview problems.

##  Contributing details
If you are using VS Code, simply _build_ the project. Note that the build script in `.vscode/tasks.json` requires the following:
1.  [uv](https://docs.astral.sh/uv/) for project management.
2.  [Ruff](https://docs.astral.sh/ruff/) for formatting and linting. Install using `uv tool install ruff`.
3.  [mypy](https://www.mypy-lang.org/) for static type checking. Install using `uv tool install mypy`.

The build script does the following:
1. Run the Ruff linter on the `src` and `tests` folders.
2. Run the Ruff formatter on the `src` and `tests` folders.
3. Run the mypy on the `src` and `tests` folders.
4. Run pytest and report coverage.
5. Build the package.
