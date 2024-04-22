#!/usr/bin/python3
"""Write a Python script that, using this REST API"""

import json
import requests
import sys


if __name__ == "__main__":
    """Employee EMPLOYEE_NAME is done with"""
    url = "https://jsonplaceholder.typicode.com/users"
    all_users = (requests.get(url)).json()
    dict_user = {}
    for x in all_users:
        user_id = x.get('id')
        user_username = x.get('username')
        url_todos = url + '/{}/todos'.format(user_id)
        response_url_todos = requests.get(url_todos)
        todos = response_url_todos.json()
        dict_user[user_id] = []
        for i in todos:
            dict_user[user_id].append({
                    "username": user_username,
                    "task": i.get('title'),
                    "completed": i.get('completed')
                }
            )
    with open('todo_all_employees.json', 'w') as csv_file:
        json.dump(dict_user, csv_file)
