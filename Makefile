.DEFAULT_GOAL := test

.PHONY: all dockerbuild dockertest test clean release upload

all: test

dockerbuild:
	docker build -t git-task .

dockerdevbuild:
	docker build -t git-task/test -f Dockerfile.dev .

dockertest:
	docker run -v /var/run/docker.sock:/var/run/docker.sock git-task/test \
	pytest

devshell: dockerbuild dockerdevbuild
	docker run -it git-task bash

test: dockerbuild dockerdevbuild dockertest

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
