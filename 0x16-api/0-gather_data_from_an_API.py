#!/usr/bin/python3
"""Python script that accesses a REST API for a given employee ID,
returns information about his/her TODO list progress"""
import requests
import sys

if __name__ == "__main__":
    employeeid = sys.argv[1]
    EMPLOYEE_NAME = requests.get("https://jsonplaceholder.typicode.com/users/{:d}"
                        .format(int(employeeid))).json().get("name")
    tasksall = 0
    taskscompleted = []
    r = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    for task in r:
        if (task.get("userId") == int(employeeid)):
            tasksall += 1
            if (task.get("completed")):
                taskscompleted.append(task.get("title"))
    print("Employee {:s} is done with tasks({:d}/{:d}):".format
          (EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in taskscompleted:
        print("\t {:s}".format(task))
