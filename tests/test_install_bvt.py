import shlex
import subprocess

DEFAULT_OUTPUT_NO_PARAMS = "Type:        GitTask"


def test_git_alias_works():
    assert subprocess.check_output(shlex.split("git task")).decode().startswith(DEFAULT_OUTPUT_NO_PARAMS)


def test_executable_works():
    assert subprocess.check_output(shlex.split("gittask")).decode().startswith(DEFAULT_OUTPUT_NO_PARAMS)


def test_python_module_works():
    assert subprocess.check_output(shlex.split("python -m gittask")).decode().startswith(DEFAULT_OUTPUT_NO_PARAMS)
