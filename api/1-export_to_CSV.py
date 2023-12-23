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
    employee_progress(argv[1])
