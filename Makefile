PY = python3
PIP = pip3

build:
	$(PY) -m venv venv
	source venv/bin/activate
	pip install --index-url https://lief.s3-website.fr-par.scw.cloud/latest lief

