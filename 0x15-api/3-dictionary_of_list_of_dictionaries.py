#!/usr/bin/python3
"""Script to fetch REST API for employees todo lists"""

import json
import requests
import sys


if __name__ == "__main__":
    server_addr = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(server_addr)
    Users = response.json()

    users_dict = dict()
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        server_addr = "https://jsonplaceholder.typicode.com/users/{}".format(USER_ID)
        url = server_addr + '/todos'
        response = requests.get(url)

        tasks = response.json()
        users_dict[USER_ID] = []
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            users_dict[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })
    """Dumping into json"""
    with open('todo_all_employees.json', 'w') as hd:
        json.dump(users_dict, hd)
