#!/usr/bin/python3
"""
    Using what from Task #0, extend the
    python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


def employee_progress(employee_id):
    """ Show employee progres """
    URL = "https://jsonplaceholder.typicode.com"
    user = requests.get(f'{URL}/users/{employee_id}').json()
    user_name = user["name"]
    todo_list = requests.get(f'{URL}/users/{employee_id}/todos').json()

    filename = f"{employee_id}.json"
    with open(filename, "w") as f:
        progress = {f"{employee_id}": []}
        for task in todo_list:
            task_dict = {}
            task_dict["task"] = task["title"]
            task_dict["completed"] = task["completed"]
            task_dict["username"] = user_name
            progress[f"{employee_id}"].append(task_dict)

        f.write(json.dumps(progress))


if __name__ == "__main__":
    employee_progress(argv[1])
