#!/usr/bin/python3
"""Python script that accesses a REST API for a given employee ID,
returns information about his/her TODO list progress"""
import requests
import sys

if __name__ == "__main__":
    employeeid = sys.argv[1]
    name = requests.get("https://jsonplaceholder.typicode.com/users/{:d}"
                        .format(employeeid)).json().get("name")
    tasksall = 0
    taskscompleted = []
    r = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    for task in r:
        if (task.get("userId") == int(employeeid)):
            tasksall += 1
            if (task.get("completed")):
                taskscompleted.append(task.get("title"))

            
