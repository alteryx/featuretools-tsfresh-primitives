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
	black featuretools_tsfresh_primitives -t py39 --check
	flake8 featuretools_tsfresh_primitives

.PHONY: lint-fix
lint-fix:
	black -t py39 featuretools_tsfresh_primitives
	isort featuretools_tsfresh_primitives

.PHONY: tests
tests:
	pytest --cache-clear --show-capture=stderr -vv ${ADDOPTS}

.PHONY: installdeps
installdeps:
	pip install --upgrade pip
	pip install -e .
	pip install -r dev-requirements.txt