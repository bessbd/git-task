.DEFAULT_GOAL := test

.PHONY: all dockerbuild dockerrun test clean release upload

all: test

dockerbuild:
	docker build -t git-task/test .

dockerrun:
	docker run git-task/test pytest

devshell:
	docker build -t git-task/test . && docker run -it git-task/test bash

test: dockerbuild dockerrun

clean:
	rm -rf .pytest_cache build dist __pycache__

install_semver:
	pip install semver

bump_patch:
	python -c "import semver; version=semver.bump_patch(open('VERSION')\
	.read().strip()); f=open('VERSION', 'w'); f.write(version)"

bump_minor:
	python -c "import semver; version=semver.bump_minor(open('VERSION')\
	.read().strip()); f=open('VERSION', 'w'); f.write(version)"

bump_major:
	python -c "import semver; version=semver.bump_major(open('VERSION')\
	.read().strip()); f=open('VERSION', 'w'); f.write(version)"

bump_commit:
	git commit -am "Bump version to `cat VERSION`"

release:
	git tag `python3 setup.py --version` && git push && git push --tags

upload:
	docker run -e TWINE_USERNAME -e TWINE_PASSWORD --mount \
	src="`pwd`",target=/app,type=bind -w /app -it python bash -c \
	"pip3 install twine && python3 setup.py sdist bdist_wheel && \
	twine upload dist/*"
