import datetime
import logging
import os
import random
import shlex
import string
import subprocess

import fire
import parsedatetime
import yaml


class GitTask:
    """Git-task is a task management system"""

    __TASKS_FILE_NAME = ".tasks.yml"

    __task_list = None

    def __init__(self):
        try:
            with(open(self.__TASKS_FILE_NAME, 'r')) as tasks_file:
                self.__task_list = yaml.load(tasks_file)
        except FileNotFoundError:
            logging.info(
                f"No {self.__TASKS_FILE_NAME} file found. Proceeding with "
                f"empty task list.")

    def add(self, summary, assignee=None, deadline=None):
        """Add a task with the details provided"""
        print(f'Adding new item with summary: "{summary}"')
        if deadline is not None:
            time_struct, parse_status = parsedatetime.Calendar().parse(
                deadline)
            deadline = datetime.datetime(*time_struct[:6]).isoformat()
        self.__task_list = self.__list_default_tasks() + [
            self.__normalize_task(summary, assignee=assignee,
                                  deadline=deadline)]
        self.__save()

    def ls(self):
        """List all tasks"""
        if self.__task_list is None:
            print(f"No {self.__TASKS_FILE_NAME} present in current directory.")
        elif not self.__list_default_tasks():
            print("Hooray, task list is empty!")
        else:
            print(self.__serialize_list(self.__task_list))

    def reformat(self):
        self.__save()

    def rm(self, id):
        """Remove one task"""
        def __id_matches(item):
            [(key, details)] = item.items()
            return 'id' in details and details['id'].startswith(id)

        id = str(id)

        items = [item for item in self.__list_default_tasks() if
                 __id_matches(item)]
        if len(items) == 0:
            print(f"Task with id: {id} not found")
        elif len(items) > 1:
            print(
                f"More than one task with id {id} found: \n"
                f"{self.__serialize_list(items)}")
        else:
            print(f"Removing task with id: {id}: \n"
                  f"{self.__serialize_list(items)}")
            self.__task_list.remove(items[0])
            self.__save()

    @staticmethod
    def install_git_alias():
        """
        Install a global git alias. Basically execute `git config
        --global alias.task <path to GitTask.py>`
        """
        subprocess.check_call(
            shlex.split(
                f"git config --global alias.task "
                f"\'!python3 {os.path.realpath(__file__)}\'"))

    @staticmethod
    def uninstall_git_alias():
        """Remove global git alias that was installed by `install_git_alias`"""
        subprocess.check_call(
            shlex.split("git config --global --unset-all alias.task"))

    @staticmethod
    def config_get(key):
        """Get a config variable"""
        pass

    @staticmethod
    def config_set(key, value):
        """Set a config variable"""
        pass

    @staticmethod
    def config_global_get(key):
        """Get a config variable"""
        pass

    @staticmethod
    def config_global_set(key, value):
        """Set a config variable"""
        pass

    def __list_default_tasks(self):
        return self.__task_list or []

    @staticmethod
    def __normalize_task(item, **kwargs):
        def __gen_id():
            return ''.join(
                random.SystemRandom().choices(string.ascii_lowercase, k=8))

        if type(item) is str:
            item = {item: {}}
        if type(item) is not dict:
            raise ValueError("Unexpected item type")

        [(key, details)] = item.items()
        details.setdefault("id", __gen_id())
        details.update({k: v for k, v in kwargs.items() if v is not None})
        return {key: {k: v for k, v in details.items() if v is not None}}

    def __save(self):
        if self.__task_list is not None:
            with(open(self.__TASKS_FILE_NAME, 'w')) as tasks_file:
                self.__serialize_list(self.__task_list, stream=tasks_file)

    def __serialize_list(self, item_list, **kwargs):
        return yaml.dump(
            [self.__normalize_task(item) for item in item_list],
            default_flow_style=False,
            **kwargs
        )


def main():  # Required for entry_points in setup.py
    fire.Fire(GitTask)


if __name__ == '__main__':
    main()
