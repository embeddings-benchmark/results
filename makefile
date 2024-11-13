install-for-tests:
	@echo "--- Installing dependencies for tests ---"
	pip install pip --upgrade
	pip install .

test:
	@echo "--- Running tests ---"
	pytest

pre-push:
	@echo "--- Running pre-push commands ---"
	python reduce_large_json_files.py