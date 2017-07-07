[![Holberton logo](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)](https://www.holbertonschool.com/)
# 0x07. Networking basics #0

### Author: Elaine Yeung [<img src="https://user-images.githubusercontent.com/23224088/27935507-4e614b68-6260-11e7-8b20-d0352ef3ff53.png" height="18px"/>](https://twitter.com/egsy) 

## Synopsis
This project introduces the concepts of **server management** in software development.

### At the end of this project students should be able to explain to anyone, **without the help of Google**:
-   OSI model
    -   What it is
	-   How many layers it has
	-   How it organized
-   What is a LAN
	-   Typical usage
		-   Typical geographical size
-   What is a WAN
	-   Typical usage
	-   Typical geographical size
-   What is the Internet
-   IP address
	-   What is it
	-   What are the 2 types of IP address
	-   What is `localhost`
	-   What is a subnet
	-   Why IPv6 was created
-   TCP/UDP
	-   What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
	-   What is the main difference between TCP and UDP
-   TCP/UDP Ports
	-   What is a port
	-   Memorize SSH, HTTP and HTTPS port numbers
-   What tool/protocol is often used to check if a device is connected to a network


### Resources
Task #0:

-   [OSI model](http://searchnetworking.techtarget.com/definition/OSI)

Task #1:

-   [Different types of network](https://www.lifewire.com/lans-wans-and-other-area-networks-817376)
-   [LAN network](http://searchnetworking.techtarget.com/definition/local-area-network-LAN)
-   [WAN network](http://searchenterprisewan.techtarget.com/definition/WAN)
-   [Internet](https://en.wikipedia.org/wiki/Internet)

Task #2:

-   [MAC address](http://whatismyipaddress.com/mac-address)
-   [What is an IP address](https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/)
-   [Private and public address](https://www.iplocation.net/public-vs-private-ip-address)
-   [IPv4 and IPv6](http://www.webopedia.com/DidYouKnow/Internet/ipv6_ipv4_difference.html)
-   [Localhost](https://en.wikipedia.org/wiki/Localhost)

Task #3:

-   [TCP and UDP](http://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)

Task #4:

-   [TCP/UDP ports List](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)

Task #5:

-   [What is `ping`/ICMP](https://en.wikipedia.org/wiki/Ping_(networking_utility))
-   [Positional parameters](http://wiki.bash-hackers.org/scripting/posparams)

man: `netstat`, `ping`

### Project Requirements
#### Bash 
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
0 | **Mandatory** | | [0-OSI_model](./0-OSI_model)
1 | **Mandatory** | | [1-types_of_network](./1-types_of_network)
2 | **Mandatory** | | [2-MAC_and_IP_address](./2-MAC_and_IP_address)
3 | **Mandatory** | | [3-UDP_and_TCP](./3-UDP_and_TCP)
4 | **Mandatory** | | [4-TCP_and_UDP_ports](./4-TCP_and_UDP_ports)
5 | **Mandatory** | | [5-is_the_host_on_the_network](./5-is_the_host_on_the_network)

