[![Holberton logo](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)](https://www.holbertonschool.com/)
# 0x16. API

### Author: Elaine Yeung [<img src="https://user-images.githubusercontent.com/23224088/27935507-4e614b68-6260-11e7-8b20-d0352ef3ff53.png" height="18px"/>](https://twitter.com/egsy) 

## Synopsis
This project introduces concepts of building Python scripts in order to access an API.

### At the end of this project students should be able to explain to anyone, **without the help of Google**:

  * What Bash scripting should not be used for
  * What is an API
  * What is a REST API
  * What are microservices
  * What is the CSV format
  * What is the JSON format
  * Python style guide:
     * Package and module name style
	 * Class name style
	 * Variable name style
	 * Function name style
	 * Constant name style
	 * What is CapWords or CamelCase

### Resources
*   [Friends don't let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
*   [What is an API](http://www.webopedia.com/TERM/A/API.html)
*   [What is a REST API](https://www.sitepoint.com/developers-rest-api/)
*   [What are microservices](https://smartbear.com/learn/api-design/what-are-microservices/)
*   [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://www.python.org/dev/peps/pep-0008/)

<ul>
<li><a href="https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script">Friends don&#39;t let friends program in shell script</a></li>
<li><a href="http://www.webopedia.com/TERM/A/API.html">What is an API</a></li>
<li><a href="https://www.sitepoint.com/developers-rest-api/">What is a REST API</a></li>
<li><a href="https://smartbear.com/learn/api-design/what-are-microservices/">What are microservices</a></li>
<li><a href="https://www.python.org/dev/peps/pep-0008/">PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry</a></li>
</ul>

### Project Requirements
*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   Libraries imported in your Python files must be organized in alphabetical order
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the `PEP 8` style
*   All your files must be executable
*   The length of your files will be tested using `wc`
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   You must use [get](https://docs.python.org/3.4/library/stdtypes.html#dict.get) to access to dictionary value by key (it won't throw an exception if the key doe sn't exist in the dictionary)
*   Your code should not be executed when imported (by using `if __name__ == "__main__":`)

## Project Breakdown
Task # | Type | Short description | File name and link |
---: | --- | --- | --- |
0 | **Mandatory** |<p>Write a Python script that, using this <a href="https://jsonplaceholder.typicode.com/">REST API</a>, for a given employee ID, returns information about his/her TODO list progress.</p><p>Requirements:</p><ul><li>You are free to use any native Python3 module</li><li>The script must accept an integer as a parameter, which is the employee ID</li><li>The script must display on the standard output the employee TODO list progress in this exact format:<ul><li>First line: <code>Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):</code><ul><li><code>EMPLOYEE_NAME</code>: name of the employee</li><li><code>NUMBER_OF_DONE_TASKS</code>: number of completed tasks</li><li><code>TOTAL_NUMBER_OF_TASKS</code>: total number of tasks, which is the sum of completed and non-completed tasks</li></ul></li><li>Second and N next lines display the title of completed tasks: Tab <code>TASK_TITLE</code></li></ul></li></ul> | [0-gather_data_from_an_API.py](./0-gather_data_from_an_API.py)
1 | **Mandatory** |<p>Using what you did in the task #0, extend your Python script to export data in the CSV format.</p><p>Requirements:</p><ul><li>Records all tasks that are owned by this employee</li><li>Format must be: <code>&quot;USER_ID&quot;,&quot;USERNAME&quot;,&quot;TASK_COMPLETED_STATUS&quot;,&quot;TASK_TITLE&quot;</code></li><li>File name must be: <code>USER_ID.csv</code></li></ul> | [1-export_to_CSV.py](./1-export_to_CSV.py)
2 | **Mandatory** |<p>Using what you did in the task #0, extend your Python script to export data in the JSON format.</p><p>Requirements:</p><ul><li>Records all tasks that are owned by this employee</li><li>Formart must be: <code>{ &quot;USER_ID&quot;: [ {&quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS, &quot;username&quot;: &quot;USERNAME&quot;}}, {&quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS, &quot;username&quot;: &quot;USERNAME&quot;}}, ... ]}</code></li><li>File name must be: <code>USER_ID.json</code></li></ul> | [2-export_to_JSON.py](./2-export_to_JSON.py)
3 | **Mandatory** |<p>Using what you did in the task #0, extend your Python script to export data in the JSON format.</p><p>Requirements:</p><ul><li>Records all tasks from all employees</li><li>Formart must be: <code>{ &quot;USER_ID&quot;: [ {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, ... ], &quot;USER_ID&quot;: [ {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, ... ]}</code></li><li>File name must be: <code>todo_all_employees.json</code></li></ul> | [3-dictionary_of_list_of_dictionaries.py](./3-dictionary_of_list_of_dictionaries.py)
