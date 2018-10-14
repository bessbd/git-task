.DEFAULT_GOAL := test

.PHONY: all dockerbuild dockerrun test clean

all: test

dockerbuild:
	docker build -t git-task/test .

dockerrun:
	docker run -it git-task/test pytest

test: dockerbuild dockerrun

clean:
	rm -rf .pytest_cache build dist __pycache__
