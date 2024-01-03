#!/usr/bin/python3

"""
Gather data from an API
"""
import requests
import sys


if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com"

    # Construct the URL for the user API endpoint
    user_id = sys.argv[1]
    user_url = base_url + "/users/{}".format(user_id)

    # Make an HTTP GET request to the user API endpoint
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Construct the URL for the todos API endpoint
    todos_url = base_url + "/todos"
    todos_params = {"userId": user_id}

    # Make an HTTP GET request to the todos API endpoint
    todos_response = requests.get(todos_url, params=todos_params)
    todos_data = todos_response.json()

    # Filter completed tasks and retrieve their titles
    completed_tasks = [task.get("title") for task in todos_data
                       if task.get("completed")]

    # Display information about completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get("name"), len(completed_tasks), len(todos_data)))

    # Display the titles of completed tasks
    for task_title in completed_tasks:
        print("\t {}".format(task_title))
