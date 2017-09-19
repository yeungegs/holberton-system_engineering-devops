#!/usr/bin/python3
"""Python script that extends script from Task 0
and exports data in JSON formatted file
File must have all records from all employees
"""
import json
import requests

if __name__ == "__main__":
    ALL_USERS = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    ALL_TASKS = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()
    ALL_RECORDS = {}

    for user in ALL_USERS:
        EMPLOYEE_ID = user.get("id")
        USERNAME = user.get("username")

        for task in ALL_TASKS:
            if (task.get("userId") == int(EMPLOYEE_ID)):
                dict = {}
                dict["task"] = task.get("title")
                dict["completed"] = task.get("completed")
                dict["username"] = USERNAME
                ALL_TASKS.append(dict)

        ALL_RECORDS[EMPLOYEE_ID] = ALL_TASKS

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(ALL_RECORDS, jsonfile)
