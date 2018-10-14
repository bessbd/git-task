.DEFAULT_GOAL := test

.PHONY: all dockerbuild dockerrun test clean release upload

all: test

dockerbuild:
	docker build -t git-task/test .

dockerrun:
	docker run -it git-task/test pytest

test: dockerbuild dockerrun

clean:
	rm -rf .pytest_cache build dist __pycache__

release:
	git tag $(python3 setup.py --version) && git push --tags

upload:
	docker run -e TWINE_USERNAME -e TWINE_PASSWORD --mount src="$(pwd)",target=/app,type=bind -w /app -it python bash -c "pip3 install twine && python3 setup.py sdist bdist_wheel && twine upload dist/*"
