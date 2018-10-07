import sys
sys.path.append("..")
from gittask.GitTask import GitTask


def test_add_works(capsys):
    GitTask.add()
    out, err = capsys.readouterr()
    assert out == "add\n"
