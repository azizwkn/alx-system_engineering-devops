#!/usr/bin/python3
"""
export data in the JSON format.
"""

import csv
import json
import requests
import sys


if __name__ == "__main__":
    USER_ID = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + USER_ID
    request = requests.get(user_url)
    USERNAME = request.json().get("username")

    user_todos = user_url + "/todos"
    request = requests.get(user_todos)
    tasks = request.json()

    dict_data = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get("completed")
        TASK_TITLE = task.get("title")
        dict_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})

    with open("{}.json".format(USER_ID), "w") as f:
        json.dump(dict_data, f)
