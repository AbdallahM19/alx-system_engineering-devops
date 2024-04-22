#!/usr/bin/python3
"""Write a Python script that, using this REST API"""

import requests
import sys


def get_employee_todo_progress(id):
    url = "https://jsonplaceholder.typicode.com/users/"
    url_id = url + "/{}".format(id)
    url_todos = url_id + '/todos'
    response_url_id = requests.get(url_id)
    response_url_todos = requests.get(url_todos)
    employee_username = response_url_id.json().get('username')
    todos = response_url_todos.json()
    with open('{}.csv'.format(id), 'w') as csv_file:
        for i in todos:
            csv_file.write(
                '"{}","{}","{}","{}"\n'.format(
                    id,
                    employee_username,
                    i.get('completed'),
                    i.get('title')
                )
            )


if __name__ == "__main__":
    """Employee EMPLOYEE_NAME is done with"""
    if len(sys.argv) != 2:
        print("Usage: python script.py {{ employee_id }}")
        sys.exit(1)
    id = sys.argv[1]
    get_employee_todo_progress(id)
