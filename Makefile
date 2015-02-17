all: dependencies test

test:
	python *_test.py

dependencies:
	which python

.PHONY: all dependencies test
