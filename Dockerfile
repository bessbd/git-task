FROM python
COPY . /git-task
WORKDIR /git-task
RUN \
    python3 setup.py sdist bdist_wheel && \
    pip install /git-task/dist/*.whl && \
    gittask install_git_alias && \
    echo 'eval "$(gt -- --completion)"' >> ~/.bashrc
