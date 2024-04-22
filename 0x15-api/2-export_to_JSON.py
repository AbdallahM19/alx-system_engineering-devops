#!/usr/bin/python3
"""Write a Python script that, using this REST API"""

import requests
import json
import sys


def get_employee_todo_progress(id):
    url = "https://jsonplaceholder.typicode.com/users"
    url_id = url + "/{}".format(id)
    url_todos = url_id + '/todos'
    response_url_id = requests.get(url_id)
    response_url_todos = requests.get(url_todos)
    employee_username = response_url_id.json().get('username')
    todos = response_url_todos.json()
    dict_id = {id: []}
    for i in todos:
        dict_id[id].append({
                "task": i.get('title'),
                "completed": i.get('completed'),
                "username": employee_username
            }
        )
    with open('{}.json'.format(id), 'w') as csv_file:
        json.dump(dict_id, csv_file)


if __name__ == "__main__":
    """Employee EMPLOYEE_NAME is done with"""
    if len(sys.argv) != 2:
        print("Usage: python script.py {{ employee_id }}")
        sys.exit(1)
    id = sys.argv[1]
    get_employee_todo_progress(id)
