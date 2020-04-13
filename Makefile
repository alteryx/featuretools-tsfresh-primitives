lint-fix:
	select="E225,E303,E302,E203,E128,E231,E251,E271,E127,E126,E301,W291,W293,E226,E306,E221"
	autopep8 --in-place --recursive --max-line-length=100 --select=${select} featuretools_tsfresh_primitives
	isort --recursive featuretools_tsfresh_primitives

lint-tests:
	flake8 featuretools_tsfresh_primitives
	isort --check-only --recursive featuretools_tsfresh_primitives

unit-tests:
	pytest --cov=featuretools_tsfresh_primitives --cache-clear --show-capture=stderr -vv
