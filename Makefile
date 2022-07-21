.PHONY: clean
clean:
	find . -name '*.pyo' -delete
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete
	find . -name '*~' -delete
	find . -name '.coverage.*' -delete

.PHONY: lint
lint:
	isort --check-only featuretools_tsfresh_primitives
	black featuretools_tsfresh_primitives -t py310 --check
	flake8 featuretools_tsfresh_primitives

.PHONY: lint-fix
lint-fix:
	black -t py310 featuretools_tsfresh_primitives
	isort featuretools_tsfresh_primitives

.PHONY: test
test:
	pytest featuretools_tsfresh_primitives/

.PHONY: testcoverage
testcoverage:
	pytest featuretools/ --cov=featuretools_tsfresh_primitives

.PHONY: installdeps
installdeps:
	pip install --upgrade pip
	pip install -e ".[dev]"
	pre-commit install
