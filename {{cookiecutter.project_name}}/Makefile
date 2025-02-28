deps:
	pip-compile requirements.in
	pip-sync requirements.txt

make test:
	pytest --cov=.
