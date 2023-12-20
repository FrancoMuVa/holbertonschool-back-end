#!/usr/bin/python3
"""
    Script that, using REST API, for a given employee ID,
    returns information about his/her todo list progress.
"""

import requests
from sys import argv


def employee_progress(employee_id):
    """ Show employee progres """
    URL = "https://jsonplaceholder.typicode.com"

    user = requests.get(f'{URL}/users/{employee_id}').json()
    user_name = user["name"]

    todo_list = requests.get(f'{URL}/users/{employee_id}/todos').json()

    done_tasks, t_tasks = 0, 0
    for task in todo_list:
        if task["completed"] is True:
            done_tasks = done_tasks + 1
        t_tasks = t_tasks + 1

    print(f"Employee {user_name} is done with tasks({done_tasks}/{t_tasks}):")
    for task in todo_list:
        if task["completed"] is True:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    employee_progress(argv[1])
