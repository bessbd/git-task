#!/usr/bin/env bash

rm -rf dist
python3 setup.py sdist bdist_wheel
docker build -t git-task/test -f Dockerfile.test . && docker run -it git-task/test pytest