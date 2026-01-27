install-for-tests:
	@echo "--- Installing dependencies for tests ---"
	uv synv --group dev

test:
	@echo "--- Running tests ---"
	uv run --no-sync pytest

pre-push:
	@echo "--- Running pre-push commands ---"
	python reduce_large_json_files.py
