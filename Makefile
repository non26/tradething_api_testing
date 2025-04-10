env:
	source .venv/bin/activate

denv:
	deactivate

pkglist:
	pip list

install:
	pip install -r requirements.txt

