#!/usr/bin/python3
"""
    Using what from Task #0, extend the
    python script to export data in CSV format.
"""

import csv
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


def export_to_csv(employee_id):
    """ export data in CSV format """
    URL = "https://jsonplaceholder.typicode.com"
    user = requests.get(f'{URL}/users/{employee_id}').json()

    todo_list = requests.get(f'{URL}/users/{employee_id}/todos').json()

    filename = f"{user['id']}.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todo_list:
            writer.writerow([
                user['id'],
                user['username'],
                task['completed'],
                task['title']
            ])


if __name__ == "__main__":
    export_to_csv(argv[1])
