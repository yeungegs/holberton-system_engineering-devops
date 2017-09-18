0-gather_data_from_an_API.py
1-export_to_CSV.py
2-export_to_JSON.py
3-dictionary_of_list_of_dictionaries.py
<!-- Task Body -->
  <p>Write a Python script that, using this <a href="https://jsonplaceholder.typicode.com/">REST API</a>, for a given employee ID, returns information about his/her TODO list progress.</p>

<p>Requirements:</p>

<ul>
<li>You are free to use any native Python3 module</li>
<li>The script must accept an integer as a parameter, which is the employee ID</li>
<li>The script must display on the standard output the employee TODO list progress in this exact format:

<ul>
<li>First line: <code>Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):</code>

<ul>
<li><code>EMPLOYEE_NAME</code>: name of the employee</li>
<li><code>NUMBER_OF_DONE_TASKS</code>: number of completed tasks</li>
<li><code>TOTAL_NUMBER_OF_TASKS</code>: total number of tasks, which is the sum of completed and non-completed tasks</li>
</ul></li>
<li>Second and N next lines display the title of completed tasks: Tab <code>TASK_TITLE</code></li>
</ul></li>
</ul>

<p>Example:</p>

<!-- Task Body -->
  <p>Using what you did in the task #0, extend your Python script to export data in the CSV format.</p>

<p>Requirements:</p>

<ul>
<li>Records all tasks that are owned by this employee</li>
<li>Format must be: <code>&quot;USER_ID&quot;,&quot;USERNAME&quot;,&quot;TASK_COMPLETED_STATUS&quot;,&quot;TASK_TITLE&quot;</code></li>
<li>File name must be: <code>USER_ID.csv</code></li>
</ul>

<p>Example:</p>

<!-- Task Body -->
  <p>Using what you did in the task #0, extend your Python script to export data in the JSON format.</p>

<p>Requirements:</p>

<ul>
<li>Records all tasks that are owned by this employee</li>
<li>Formart must be: <code>{ &quot;USER_ID&quot;: [ {&quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS, &quot;username&quot;: &quot;USERNAME&quot;}}, {&quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS, &quot;username&quot;: &quot;USERNAME&quot;}}, ... ]}</code></li>
<li>File name must be: <code>USER_ID.json</code></li>
</ul>

<p>Example:</p>

<!-- Task Body -->
  <p>Using what you did in the task #0, extend your Python script to export data in the JSON format.</p>

<p>Requirements:</p>

<ul>
<li>Records all tasks from all employees</li>
<li>Formart must be: <code>{ &quot;USER_ID&quot;: [ {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, ... ], &quot;USER_ID&quot;: [ {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, ... ]}</code></li>
<li>File name must be: <code>todo_all_employees.json</code></li>
</ul>

<p>Example:</p>

[![Holberton logo](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)](https://www.holbertonschool.com/)
# NAME OF PROJECT

### Author: Elaine Yeung [<img src="https://user-images.githubusercontent.com/23224088/27935507-4e614b68-6260-11e7-8b20-d0352ef3ff53.png" height="18px"/>](https://twitter.com/egsy) 

## Synopsis
This project introduces **INSERT DESCRIPTION HERE**

### At the end of this project students should be able to explain to anyone, **without the help of Google**:

### Resources

### Project Requirements
-   Allowed editors: `vi`, `vim`, `emacs`
-   All your Bash script files will be interpreted on Ubuntu 14.04 LTS
-   All your files should end with a new line
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   Your Bash script must pass `shellcheck` without any error
-   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing

The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash` for instance is that it will make your script portable for different OS where Bash might be in a different location.

## Project Breakdown
Task # | Type | Short description | File name and link |
---: | --- | --- | --- |
0 | **Mandatory** | | 
1 | **Mandatory** | | 
2 | **Mandatory** | | 
3 | **Mandatory** | | 
4 | **Mandatory** | | 
5 | **Mandatory** | | 

