0-transfer_file
1-install_nginx_web_server
2-setup_a_domain_name
3-redirection
4-not_found_page_404

[![Holberton logo](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)](https://www.holbertonschool.com/)
# 0x09. Web server

### Author: Elaine Yeung [<img src="https://user-images.githubusercontent.com/23224088/27935507-4e614b68-6260-11e7-8b20-d0352ef3ff53.png" height="18px"/>](https://twitter.com/egsy) 

## Synopsis
This project applies concepts related to web server management and administration and applies concepts of DNS, web servers, Continuous Integration/Continuous Deployment, containers, and web stack debugging

![Holberton Web server project](https://i.imgur.com/8Gu52Qv.png)

### At the end of this project students should be able to explain to anyone, **without the help of Google**:

*   What DNS stands for
*   What is DNS main role
*   What are DNS record types for:
    *   `A`
	*   `CNAME`
	*   `TXT`
	*   `MX`
	*   What is the main role of a web server
				
### Resources

*   [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
*   [Nginx](https://en.wikipedia.org/wiki/Nginx)
*   [Root and sub domain](https://support.landingi.com/article/147-the-root-domain-and-sub-domain-differences)
*   [HTTP redirection](https://moz.com/learn/seo/redirection)
*   [Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404)
*   [Logs files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)

man: `scp`, `curl`

[![Web stack - web server](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/Screenshot+2017-07-06+19.24.05.png)](https://www.youtube.com/watch?v=AZg4uJkEa-4&feature=youtu.be&hd=1)

In this project, some of the tasks will be graded on 2 aspects:

1.  Is your `web-01` server configured according to requirements
2.  Is your answer file containing a Bash script that automatically performs commands to configure a Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file `/tmp/test` containing the string `hello world` and modify the configuration of Nginx to listen on port `8080` instead of `80`, I can use `emacs` on my server to create the file and to modify Nginx configuration file `/etc/nginx/sites-enabled/default`.

But my answer file would contain:

```sh
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu

```

As you can tell, I am not using `emacs` to perform the task in my answer file. This exercise is aiming at training you on automating your work, if you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an [SRE](https://www.atlassian.com/it-unplugged/devops/site-reliability-engineering-sre), that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the `root` user, you do not need to use the `sudo` command.

A good Software Engineer is a [lazy Software Engineer](https://www.techwell.com/techwell-insights/2013/12/why-best-programmers-are-lazy-and-act-dumb). ![Software Engineer solving blackboard punishment using loop](https://i.imgur.com/82VsYEC.jpg)

Tips: to test your answer Bash script, feel free to reproduce the checker environment:

*   start a `ubuntu:14.04` Docker container
*   run your script on it
*   see how it behaves

Check out the Docker concept page for more info about how to manipulate containers.



### Project Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck` (version `0.3.3-1~ubuntu14.04.1` via `apt-get`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Project Breakdown
Task # | Type | Short description | File name and link |
---: | --- | --- | --- |
0 | **Mandatory** | | [0-transfer_file](./0-transfer_file)
1 | **Mandatory** | | [1-install_nginx_web_server](./1-install_nginx_web_server)
2 | **Mandatory** | | [2-setup_a_domain_name](./2-setup_a_domain_name)
3 | **Mandatory** | | [3-redirection](./3-redirection)
4 | **Mandatory** | | [4-not_found_page_404](./4-not_found_page_404)
