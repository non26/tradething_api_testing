env:
	source .venv/bin/activate

denv:
	deactivate

pkglist:
	pip list

install:
	pip install -r requirements.txt


test-long:
	python3 test_future/test_single_long_position.py