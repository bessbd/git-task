#!/usr/bin/env bash

exit 0

docker build -t git-task/test -f Dockerfile.test . && docker run -it git-task/test groovy test.groovy
