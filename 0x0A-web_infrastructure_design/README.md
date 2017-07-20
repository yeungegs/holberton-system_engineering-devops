
[![Holberton logo](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)](https://www.holbertonschool.com/)
# 0x0A. Web infrastructure design #0

### Author: Elaine Yeung [<img src="https://user-images.githubusercontent.com/23224088/27935507-4e614b68-6260-11e7-8b20-d0352ef3ff53.png" height="18px"/>](https://twitter.com/egsy)

## Synopsis
This project applies newly learned concepts about web infrastructure.

### At the end of this project students should be able to explain to anyone, **without the help of Google**:
*   You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
*   You must be able to explain what are each component doing
*   You must be able to explain system redundancy
*   Know all the mentioned acronyms: LAMP, SPOF, QPS

### Resources
Task #0:

*   [What is a database](http://searchsqlserver.techtarget.com/definition/database)
*   [DNS record types](https://pressable.com/blog/2014/12/23/dns-record-types-explained/)
*   [Single point of failure](https://en.wikipedia.org/wiki/Single_point_of_failure)

Task #1:

*   [How to avoid downtime when deploying new code](https://softwareengineering.stackexchange.com/questions/35063/how-do-you-update-your-production-codebase-database-schema-without-causing-downt#answers-header)
*   [High availability cluster (active-active/active-passive)](https://docs.oracle.com/cd/E17904_01/core.1111/e10106/intro.htm#ASHIA712)

Task #2:

*   [What is HTTPS](https://www.instantssl.com/ssl-certificate-products/https.html)
*   [What is a firewall](http://www.webopedia.com/TERM/F/firewall.html)

[![Web infrastructure design with whiteboarding](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/302/web+infrastructure+design.png)](https://www.youtube.com/watch?v=VbqbNUSfUgs)

## Requirements:


### Project Requirements
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   For each task, once you are done whiteboarding (on a whiteboard, piece of paper or software or your choice), take a picture/screenshot of your diagram
*   This project will be manually reviewed:
	*   As each task is completed, the name of that task will turn green
	*   Upload a screenshot, showing that you completed the required levels, to any image hosting service (I personally use [imgur](http://imgur.com/) but feel free to use anything you want).
	*   For the following tasks, insert the link from of your screenshot into the answer file
	*   After pushing your answer file to Github, insert the Github file link into the URL box
*   You will also have to whiteboard each task in front of a mentor, staff or student - no computer or notes will be allowed during the whiteboarding session
	*   Focus on what you are being asked:
	*   Cover what the requirements mention, we will explore details in a later project
	*   Keep in mind that you will have 30 minutes to perform the exercise, you will get points for what is asked in requirements
	*   Similarly in a job interview, you should answer what the interviewer asked for, be careful about being too verbose - always ask the interviewer if going into details is necessary - speaking too much can play against you
	*   In this project, again, avoid going in details if not asked

## Project Breakdown
Task # | Type | Short description | File name and link |
---: | --- | --- | --- |
0 | **Mandatory** |<p>A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a <a href="https://en.wikipedia.org/wiki/LAMP_(software_bundle)">LAMP stack</a>.</p><p>On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via <code>www.foobar.com</code>. Start your explanation by having a user wanting to access your website.</p><p>Requirements:</p><ul><li> You must use:<ul><li>1 server</li><li>1 web server (Nginx)</li><li>1 application files (your code base)</li><li>1 database (MySQL)</li><li>1 domain name <code>foobar.com</code> configured with a <code>www</code> record that points to your server IP <code>8.8.8.8</code></li></ul></li><li>You must be able to explain some specifics about this infrastructure:<ul><li>What is a server</li><li>What is the role of the domain name</li><li>What type of DNS record <code>www</code> is in <code>www.foobar.com</code></li><li>What is the role of the web server</li><li>What is the role of the database</li><li>What is the server using to communicate with the computer of the user requesting the website</li></ul></li><li>You must be able to explain what are the issues with this infrastructure:<ul><li>SPOF</li><li>Downtime when maintenance needed (like deploying new code web server needs to be restarted)</li><li>Cannot scale if too much incoming traffic</li></ul></li></ul> | [0-simple_web_stack](./0-simple_web_stack)
1 | **Mandatory** |<p>On a whiteboard, design a three servers web infrastructure that host the website <code>www.foobar.com</code>.</p><p>Requirements:</p><ul><li> You must add:<ul><li>2 servers</li><li>1 web server (Nginx)</li><li>1 load-balancer (HAproxy)</li><li>1 application files (your code base)</li><li>1 database (MySQL)</li></ul></li><li>You must be able to explain some specifics about this infrastructure:<ul><li>For every additional element, why you are adding it</li><li>What distribution algorithm your load balancer is configured with and how it works</li><li>Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both</li><li>How a database Primary-Replica (Master-Slave) cluster works</li><li>What is the difference between the Primary node and the Replica node in regard to the application</li></ul></li><li>You must be able to explain what are the issues with this infrastructure:<ul><li>Where are SPOF</li><li>Security issue (no firewall, no HTTPS)</li><li>No monitoring</li></ul></li></ul> | [1-distributed_web_infrastructure](./1-distributed_web_infrastructure)
2 | **Mandatory** |<p>On a whiteboard, design a three servers web infrastructure that host the website <code>www.foobar.com</code>, it must be secured, serve encrypted traffic and be monitored.</p><p>Requirements:</p><ul><li> You must add:<ul><li>3 firewalls </li><li>1 SSL certificate to serve <code>www.foobar.com</code> over HTTPS</li><li>3 monitoring clients (data collector for Sumologic or other monitoring services)</li></ul></li><li>You must be able to explain some specifics about this infrastructure:<ul><li>For every additional element, why you are adding it</li><li>What are firewalls for</li><li>Why is the traffic served over HTTPS</li><li>What monitoring is used for</li><li>How is the monitoring tool collecting data</li><li>Explain what to do if you want to monitor your web server QPS</li></ul></li><li>You must be able to explain what are the issues with this infrastructure:<ul><li>Why terminating SSL at the load balancer level is an issue</li><li>Why having only one MySQL server capable of accepting writes is an issue</li></ul></li></ul> | [2-secured_and_monitored_web_infrastructure](./2-secured_and_monitored_web_infrastructure)
3 | *Advanced* |  <p>Readme</p>    <ul>  <li><a href="https://www.nginx.com/resources/glossary/application-server-vs-web-server/">Application server vs web server</a></li>  </ul>    <p>Requirements:</p>    <ul>  <li> You must add:    <ul>  <li>1 server</li>  <li>1 load-balancer (HAproxy) configured as cluster with the other one</li>  <li>2 web application servers (Gunicorn)</li>  </ul></li>  <li>You must be able to explain some specifics about this infrastructure:    <ul>  <li>For every additional element, why you are adding it</li>  </ul></li>  </ul> | [3-scale_up](./scale_up)
