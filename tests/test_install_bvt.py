import re
import shlex
import subprocess

GITTASK_NO_PARAMS_DEFAULT_OUTPUT = "Type:        GitTask"


def get_stdout_for(command):
    cmd_to_exec = "docker run -v /var/run/docker.sock:/var/run/docker.sock " \
                  "git-task bash -c \"" + command + "\""
    return subprocess.check_output(shlex.split(cmd_to_exec)).decode()


def assert_command_output_starts_with_default_output(command):
    assert get_stdout_for(command).startswith(
        GITTASK_NO_PARAMS_DEFAULT_OUTPUT)


def test_git_alias_works():
    assert_command_output_starts_with_default_output("git task")


def test_executable_works():
    assert_command_output_starts_with_default_output("gittask")


def test_list_no_tasks_yml():
    assert get_stdout_for("gt list").\
        startswith("No .tasks.yml present in current directory.")


def test_add_item():
    assert get_stdout_for("gt add \"foo\"").\
        startswith("Adding new item with summary: \"foo\"")


def test_list_after_add():
    output_regex = re.compile('Adding new item with summary: "foo"\\n'
                              '- foo:\\s+id: \\w{8}\\s*')
    assert output_regex.match(get_stdout_for("gt add foo && gt list")
                              ) is not None
