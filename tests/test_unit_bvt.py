import logging
import sys

sys.path.append("..")
from gittask.GitTask import GitTask  # noqa: E402


def test_parse_file_does_not_exist(tmpdir, caplog):
    tmpdir.chdir()
    caplog.set_level(logging.INFO)
    git_task = GitTask()
    assert caplog.record_tuples == [
        ('root', logging.INFO, 'No ' + GitTask.TASKS_FILE_NAME +
         ' file found. Proceeding with empty task list.'),
    ]
    assert git_task.task_list is None


def test_parse_file_empty(tmpdir):
    tmpdir.chdir()
    tmpdir.join(GitTask.TASKS_FILE_NAME).write('')
    git_task = GitTask()
    assert git_task.task_list is None


def test_init_produces_nothing_on_stdout_stderr(capsys):
    GitTask()
    out, err = capsys.readouterr()
    assert (out, err) == ('', '')


def test_add_bvt(tmpdir, capsys, caplog):
    test_summary = "test task"
    tmpdir.chdir()
    git_task = GitTask()
    git_task.add(test_summary)
    assert git_task.task_list == [test_summary]
    out, err = capsys.readouterr()
    assert (out, err) == ("Adding new item with summary: \"test task\"\n", '')
    assert tmpdir.join(".tasks.yml").read() == "- test task\n"
