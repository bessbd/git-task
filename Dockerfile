FROM bessbd/docker-python-pytest
COPY . /git-task
RUN \
    cd /git-task && \
    flake8 && \
    python3 setup.py sdist bdist_wheel && \
    pip install /git-task/dist/*.whl && \
    python -m gittask install
WORKDIR /git-task
