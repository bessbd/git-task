import logging
import sys

sys.path.append("..")
from gittask.GitTask import GitTask  # noqa: E402


def test_parse_file_does_not_exist(tmpdir, caplog):
    tmpdir.chdir()
    caplog.set_level(logging.INFO)
    GitTask()
    assert caplog.record_tuples == [
        ('root', logging.INFO, 'No .tasks.yml file found. Proceeding with'
                               ' empty task list.'),
    ]


def test_init_produces_nothing_on_stdout_stderr(capsys):
    GitTask()
    out, err = capsys.readouterr()
    assert (out, err) == ('', '')


def test_add_bvt(tmpdir, capsys, caplog):
    test_summary = "test task"
    tmpdir.chdir()
    git_task = GitTask()
    git_task.add(test_summary)
    out, err = capsys.readouterr()
    assert (out, err) == ("Adding new item with summary: \"test task\"\n", '')
    assert tmpdir.join(".tasks.yml").read() == "- test task\n"
