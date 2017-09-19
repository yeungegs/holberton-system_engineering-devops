#!/usr/bin/python3
"""Python script that extends script from Task 0
and exports data in JSON formatted file
File must have all records
"""
import json
import requests
import sys

if __name__ == "__main__":
    EMPLOYEE_ID = sys.argv[1]
    USERNAME = requests.get(
        "https://jsonplaceholder.typicode.com/users/{:d}"
        .format(int(EMPLOYEE_ID))).json().get("username")
    
    ALL_TASKS = []
    r = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    for task in r:
        if (task.get("userId") == int(EMPLOYEE_ID)):
            list = {}
            list["task"] = task.get("title")
            list["completed"] = task.get("completed")
            list["username"] = USERNAME
            ALL_TASKS.append(list)

    with open("{}.json".format(EMPLOYEE_ID), 'w') as jsonfile:
        json.dump({EMPLOYEE_ID: ALL_TASKS}, jsonfile)
