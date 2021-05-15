.PHONY: tests
tests:
	python3 -m pytest
	pytest ./procon --doctest-modules
