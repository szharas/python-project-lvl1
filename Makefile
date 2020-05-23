install:
	poetry install

lint:
	poetry run flake8 brain_games

build: lint
	poetry build

publish: lint build
	poetry config repositories.TestPyPI https://test.pypi.org/legacy/
	poetry publish --repository TestPyPI
