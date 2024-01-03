#!/usr/bin/python3

"""
export data in the CSV format
"""
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/' + user
    request = requests.get(user_url)

    user_name = request.json().get('username')
    task = user_url + '/todos'
    request = requests.get(task)
    tasks = request.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            """Complete"""
            title_task = task.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))
