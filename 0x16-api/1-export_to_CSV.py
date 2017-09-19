#!/usr/bin/python3
"""Python script that extends script from Task 0
and exports data in CSV format"""
import csv
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
            list = []
            list.extend((EMPLOYEE_ID,
                        USERNAME,
                        task.get("completed"),
                        task.get("title")))
            ALL_TASKS.append(list)

    with open("{}.csv".format(EMPLOYEE_ID), 'w') as csvfile:
        fieldnames = ["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"]
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writerows(ALL_TASKS)
