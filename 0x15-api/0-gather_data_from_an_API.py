#!/usr/bin/python3

"""
Gather data from an API
"""

import json
import requests
import sys

if __name__ == "__main__":
    def fetch_todo_progress(employee_id):
        base_url = "https://jsonplaceholder.typicode.com"
        user_url = f"{base_url}/users/{employee_id}"
        todo_url = f"{user_url}/todos"

        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()

        # Fetch TODO list for the user
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Filter completed tasks
        completed_tasks = [task for task in todo_data if task['completed']]

        # Display information
        print(f"Employee {user_data['name']} is done with tasks "
              f"({len(completed_tasks)}/{len(todo_data)}):")

        # Display completed tasks
        for task in completed_tasks:
            print("\t", task['title'])

    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        employee_id = int(sys.argv[1])
        fetch_todo_progress(employee_id)
