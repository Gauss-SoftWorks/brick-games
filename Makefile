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

########
# TEST #
########
test:
		poetry run pytest

################
# SORT IMPORTS #
################
.PHONY: sort
sort:
	poetry run isort src/ tests/
