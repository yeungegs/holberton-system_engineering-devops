[![Holberton logo](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)](https://www.holbertonschool.com/)
# 0x12. Firewall

### Author: Elaine Yeung [<img src="https://user-images.githubusercontent.com/23224088/27935507-4e614b68-6260-11e7-8b20-d0352ef3ff53.png" height="18px"/>](https://twitter.com/egsy) 

## Synopsis
This project introduces and applies concept of firewalls in network security.

![Firewall project](http://i.imgur.com/V1HjQ1Y.png)
Your servers without a firewall...

![When your firewall is OFF](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif)

### At the end of this project students should be able to explain to anyone, **without the help of Google**:

### Resources

*   [What is a firewall](https://en.wikipedia.org/wiki/Firewall_(computing))

As explained in the [web stack debugging guide](https://intranet.hbtn.io/concepts/68), `telnet` is a very good tool to check if sockets are open with `telnet IP PORT`. For example, if you want to check if port 22 is open on `web-02`:

```
sylvain@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is '^]'.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.
sylvain@ubuntu$

```

We can see for this example that the connection is successful: `Connected to web-02.holberton.online.`

Now let's try connecting to port 2222:

```
sylvain@ubuntu$ telnet web-02.holberton.online 2222
Trying 54.89.38.100...
^C
sylvain@ubuntu$

```

We can see that the connection never succeeds, so after some time I just use `cltr+c` to kill the process.

This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.

Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on `web-01`, please perform the test from outside of the school network, like from your `web-02` server. If you SSH into your `web-02` server, the traffic will be originating from `web-02` and not from the school's network, bypassing the firewall.

**Be very careful with firewall rules! For instance, if you ever deny port `22/TCP` you will not be able to connect to your server via SSH, and we will not be able to recover it.**

## Project Breakdown
Task # | Type | Short description | File name and link |
---: | --- | --- | --- |
0 | **Mandatory** |<p>Pick one answer for every question.</p><p>What is a firewall?</p><ol><li>A hardware security system</li><li>A hardware or software security system</li><li>A software security system</li></ol><p>What are the 2 types of firewall:</p><ol><li>Soft and hard firewall</li><li>Incoming and outgoing firewall</li><li>Network and host-based firewall</li></ol><p>What is the main function of a firewall?</p><ol><li>To filter incoming and outgoing network traffic</li><li>To filter  incoming and outgoing TCP traffic</li><li>To  filter outgoing traffic</li></ol> | [0-firewall_ABC](./0-firewall_ABC)
1 | **Mandatory** |<p>Let&#39;s install the <code>ufw</code> firewall and setup a few rules on <code>web-01</code>.</p><p>Requirements:</p><ul><li>The requirements below must be applied to <code>web-01</code> (feel free to do it on <code>lb-01</code> and <code>web-02</code>, but it won&#39;t be checked)</li><li>Configure <code>ufw</code> so that it blocks all incoming traffic, except the following TCP ports:<ul><li><code>22</code> (SSH)</li><li><code>443</code> (HTTPS SSL)</li><li><code>80</code> (HTTP)</li></ul></li><li>Share the <code>ufw</code> commands that you used in your answer file</li></ul> | [1-block_all_incoming_traffic_but](./1-block_all_incoming_traffic_but)
2 | **Mandatory** |<p>Firewalls can not only filter requests, they can also forward them.</p><p>Requirements:</p><ul><li>Configure <code>web-01</code> so that its firewall redirects port <code>8080/TCP</code> to port <code>80/TCP</code>.</li><li>Your answer file should be a copy of the <code>ufw</code> configuration file that you modified to make this happen</li></ul><p>Terminal in <code>web-01</code>:</p> | [2-port_forwarding](./2-port_forwarding)





