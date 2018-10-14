import shlex
import subprocess

GITTASK_NO_PARAMS_DEFAULT_OUTPUT = "Type:        GitTask"


def assert_command_output_starts_with_default_output(command):
    assert subprocess.check_output(shlex.split(command)).decode().startswith(
        GITTASK_NO_PARAMS_DEFAULT_OUTPUT)


def test_git_alias_works():
    assert_command_output_starts_with_default_output("git task")


def test_executable_works():
    assert_command_output_starts_with_default_output("gittask")


def test_python_module_works():
    assert_command_output_starts_with_default_output("python -m gittask")
