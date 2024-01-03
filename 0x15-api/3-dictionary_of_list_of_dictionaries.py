#!/usr/bin/python3
"""
export data in the JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"

    request = requests.get(base_url)
    users = request.json()

    users_dict = {}
    for user in users:
        USER_ID = user.get("id")
        USERNAME = user.get("username")
        base_url = ("https://jsonplaceholder.typicode.com/"
                    "users/{}").format(USER_ID)
        base_url = base_url + "/todos/"
        request = requests.get(base_url)

        tasks = request.json()
        users_dict[USER_ID] = []
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get("completed")
            TASK_TITLE = task.get("title")
            users_dict[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })

    with open("todo_all_employees.json", "w") as f:
        json.dump(users_dict, f)
