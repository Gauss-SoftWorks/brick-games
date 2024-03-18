#######
# RUN #
#######
run:
	poetry run python src/brick_games/main.py

#########
# LINTs #
#########
lint: ## run static analysis with mypy
	poetry run python -m mypy src/

format: ## run autoformatting with black
	poetry run python -m black src/ tests/

lf: lint format ## Lint and format

###################
# TEST & COVERAGE # 
###################
test:
		poetry run pytest

coverage:  ## clean and run unit tests with coverage
	poetry run coverage	run --source=src -m pytest --verbose tests
	poetry run coverage report --show-missing --fail-under 40
	poetry run coverage html

################
# SORT IMPORTS #
################
.PHONY: sort
sort:
	poetry run isort src/ tests/
