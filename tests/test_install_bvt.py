import shlex
import subprocess


def test_help_works():
    assert subprocess.check_output(shlex.split("git task")).decode().startswith("Type:        GitTask")
