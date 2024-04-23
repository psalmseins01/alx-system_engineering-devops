#!/usr/bin/python3
"""
Using REST API to gather employee data
"""

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            response = requests.get('{}/users/{}'.format(REST_API, id)).json()
            req_task = requests.get('{}/todos'.format(REST_API)).json()
            emp_name = response.get('name')
            tasks = list(filter(lambda x: x.get('UserId') == id, req_task))
            finished_task = list(filter(lambda x: x.get('completed'), tasks))
            print('Employee {} is done with tasks ({}/{}):'.format(
                    emp_name,
                    len(finished_task),
                    len(tasks)
                )
            )
            if len(finished_task) > 0:
                for task in finished_task:
                    print('\t {}'.format(task.get('title')))
