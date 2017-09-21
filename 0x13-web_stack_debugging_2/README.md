[![Holberton logo](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)](https://www.holbertonschool.com/)
# 0x13. Web stack debugging #2

### Author: Elaine Yeung [<img src="https://user-images.githubusercontent.com/23224088/27935507-4e614b68-6260-11e7-8b20-d0352ef3ff53.png" height="18px"/>](https://twitter.com/egsy) 

## Synopsis
This project introduces **RT DESCRIPTION HERE**

### At the end of this project students should be able to explain to anyone, **without the help of Google**:

### Resources

### Project Requirements
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- All your Bash script files must be executable
- Your Bash scripts must pass `Shellcheck` without any error
- Your Bash scripts must run without error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing


## Project Breakdown
Task # | Type | Short description | File name and link |
---: | --- | --- | --- |
0 | **Mandatory** |<p>The <code>root</code> user is a superuser that can do anything on a Unix machine, the top administrator. Security wise, you must do everything that you can to prevent an att  acker from logging in as <code>root</code>. With this in mind, it&#39;s a good practice not to run your web servers as <code>root</code> (which is the default for most configurat  ions) and instead run the process as the less privileged <code>nginx</code> user instead. This way, if a hacker does find a security issue that allows them to break-in to your se  rver, the impact is limited by the permissions of the <code>nginx</code> user.</p>    <p>Fix this container so that Nginx is running as the <code>nginx</code> user.</p>    <p>Requirements:</p>    <ul>  <li><code>nginx</code> must be running as <code>nginx</code> user</li>  <li><code>nginx</code> must be listening on all active IPs on port <code>8080</code></li>  <li>You cannot use <code>apt-get remove</code></li>  <li>Write a Bash script that configures the container to fit the above requirements</li> </ul> | [0-run_nginx_as_nginx](./0-run_nginx_as_nginx)




  
