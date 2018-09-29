#!/usr/bin/env bash

docker build -t git-task/test -f Dockerfile.test . && docker run -it git-task/test pytest