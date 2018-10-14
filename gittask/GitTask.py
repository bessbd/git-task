import os

import fire
import shlex
import subprocess


class GitTask:
    """Git-task is a task management system"""

    @staticmethod
    def add():
        print("add")

    @staticmethod
    def list():
        print("list")

    @staticmethod
    def remove():
        """Removes one todo item"""
        print("remove")

    @staticmethod
    def install_git_alias():
        subprocess.check_call(
            shlex.split(
                "git config --global alias.task '!python3 " + os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    "GitTask.py") + "'"))

    @staticmethod
    def uninstall_git_alias():
        subprocess.check_call(
            shlex.split("git config --global --unset-all alias.task"))


def main():
    fire.Fire(GitTask)


if __name__ == '__main__':
    main()
