[![Holberton logo](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)](https://www.holbertonschool.com/)
# 0x14. Application server #0

### Author: Elaine Yeung [<img src="https://user-images.githubusercontent.com/23224088/27935507-4e614b68-6260-11e7-8b20-d0352ef3ff53.png" height="18px"/>](https://twitter.com/egsy) 

## Synopsis
This project introduces and applies concepts related to web server management, server administration and web stack debugging.

### At the end of this project students should be able to explain to anyone, **without the help of Google**:

### Resources
<ul>
<li><a href="https://www.nginx.com/resources/glossary/application-server-vs-web-server/">Application server vs web server</a></li>
<li><a href="https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04">How To Serve a Flask Application with Gunicorn and Nginx on Ubuntu 14.04</a></li>
<li><a href="http://docs.gunicorn.org/en/latest/run.html">Running Gunicorn</a></li>
<li><a href="http://flask.readthedocs.io/en/0.6/api/#flask.Flask.route">Be careful with the way Flask manages slash in route</a></li>
<li><a href="http://upstart.ubuntu.com/cookbook/">Upstart documentation</a></li>
</ul>

<p><a href="https://www.youtube.com/watch?v=x-OkxsrEGYc"><img src="http://i.imgur.com/iH23y08.png" alt="Appliation server video"></a></p>

<p>You web infrastructure is already serving web pages via Nginx that you installed in your <a href="https://intranet.hbtn.io/projects/266">first web stack project</a>. And while a web server can also serve dynamic content, the task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.</p>

<p><img src="http://i.imgur.com/QbqjElZ.jpg" alt="Application server"></p>

### Project Requirements
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Everything Python-related must be done using `python3`
-   Provide comments in all your config files
-   Allowed editors: `vi`, `vim`, `emacs`
-   All your Bash script files will be interpreted on Ubuntu 14.04 LTS
-   All your files should end with a new line
-   All your Bash script files must be executable
-   Your Bash script must pass `shellcheck` without any error
-   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing

The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash` for instance is that it will make your script portable for different OS where Bash might be in a different location.

## Project Breakdown
Task # | Type | Short description | File name and link |
---: | --- | --- | --- |
0 | **Mandatory** |Serve what you built for <a href="https://intranet.hbtn.io/projects/290">AirBnB clone - Web framework</a> on <code>web01</code>.<br><br>Requirements:<ul><li>Git clone your Airbnb clone</li><li>Install Gunicorn and other libraries required by your application</li><li>Create an Upstart script that starts Gunicorn to serve <code>web_flask/0-hello_route.py</code> from your Airbnb clone</li><li>Setup Nginx so that the route <code>/airbnb-onepage/</code> points to Gunicorn</li><li>Nginx must serve this locally but also on its public IP on port <code>80</code></li><li>Provide the Upstart config file you wrote, upload it as answer file with the name <code>0-welcome_gunicorn-upstart_config</code></li><li>Provide the Nginx config file you wrote, upload it as answer file with the name <code>0-welcome_gunicorn-nginx_config</code></li></ul> | [0-welcome_gunicorn-upstart_config](./0-welcome_gunicorn-upstart_config), [0-welcome_gunicorn-nginx_config](./0-welcome_gunicorn-nginx_config)
1 | **Mandatory** |Let&#39;s serve what you built for <a href="https://intranet.hbtn.io/projects/290">AirBnB clone - Web framework</a> on <code>web01</code>.<br><br>Requirements:<ul><li>Create an Upstart script that starts Gunicorn to serve <code>web_flask/6-number_odd_or_even.py</code> from your Airbnb clone</li><li>Setup Nginx so that the route <code>/airbnb-dynamic/</code> points to Gunicorn</li><li>Nginx must serve this locally but also on its public IP on port <code>80</code></li><li>Provide your Upstart config file, name it <code>1-pass_parameter-upstart_config</code></li><li>Provide your Nginx config file, name it <code>1-pass_parameter-nginx_config</code></li></ul> | [1-pass_parameter-upstart_config](./1-pass_parameter-upstart_config), [1-pass_parameter-nginx_config](./1-pass_parameter-nginx_config)
