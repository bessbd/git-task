.PHONY: all
all: test

dockerbuild:
	docker build -t git-task/test .

dockerrun:
	docker run -it git-task/test pytest

test: dockerbuild dockerrun
