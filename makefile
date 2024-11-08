install-for-tests:
	@echo "--- Installing dependencies for tests ---"
	# just use the dev dependencies from mteb to keep everything compatible
	pip install .

test:
	@echo "--- Running tests ---"
	pytest

pre-push:
	@echo "--- Running pre-push commands ---"
	python reduce_large_json_files.py