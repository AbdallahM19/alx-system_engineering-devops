#!/usr/bin/python3
"""Write a Python script that, using this REST API"""

import requests
import sys


def get_employee_todo_progress(id):
    url = "https://jsonplaceholder.typicode.com/users"
    url_id = url + "/{}".format(id)
    url_todos = url_id + '/todos'
    response_url_id = requests.get(url_id)
    response_url_todos = requests.get(url_todos)
    employee_name = response_url_id.json().get('name')
    todos = response_url_todos.json()
    completed_tasks = [
        todo['title'] for todo in todos if todo['completed']
    ]
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            len(completed_tasks),
            len(todos)
        )
    )
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    """Employee EMPLOYEE_NAME is done with"""
    if len(sys.argv) != 2:
        print("Usage: python script.py {{ employee_id }}")
        sys.exit(1)
    id = sys.argv[1]
    get_employee_todo_progress(id)
