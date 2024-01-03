#!/usr/bin/python3

"""
Gather data from an API
"""
import re
import requests
import sys


if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com"

    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            request = requests.get('{}/users/{}'.format(base_url, id)).json()
            task_request = requests.get('{}/todos'.format(base_url)).json()
            user_name = request.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task_request))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user_name,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
