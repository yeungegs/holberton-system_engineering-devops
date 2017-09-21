[![Holberton logo](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)](https://www.holbertonschool.com/)
# 0x10. HTTPS SSL

### Author: Elaine Yeung [<img src="https://user-images.githubusercontent.com/23224088/27935507-4e614b68-6260-11e7-8b20-d0352ef3ff53.png" height="18px"/>](https://twitter.com/egsy) 

## Synopsis
This project introduces and applies concept of HTTPS protocol.

### At the end of this project students should be able to explain to anyone, **without the help of Google**:

- What is HTTPS SSL 2 main roles
- What is the purpose encrypting traffic
- What SSL termination means

### Resources

- [What is HTTPS?](https://www.instantssl.com/ssl-certificate-products/https.html)
- [What are the 2 main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)
- [HAproxy SSL termination on Ubuntu14.04](https://www.digitalocean.com/community/tutorials/how-to-secure-haproxy-with-let-s-encrypt-on-ubuntu-14-04)
- [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)
- [Bash function](http://tldp.org/LDP/abs/html/complexfunct.html)

man: `awk`, `dig`

Don't be lame, secure your website traffic.

![When HTTPS SSL is not enabled](https://i.imgur.com/xCmOCgw.gif)

## Project Requirements

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted on Ubuntu 14.04 LTS
*   All your files should end with a new line
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   All your Bash script files must be executable
*   Your Bash script must pass `Shellcheck` (version `0.3.3-1~ubuntu14.04.1` via `apt-get`) without any error
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
*   The second line of all your Bash scripts should be a comment explaining what is the script doing

## Project Breakdown
Task # | Type | Short description | File name and link |
---: | --- | --- | --- |
0 | **Mandatory** |<p>As for project <a href="https://intranet.hbtn.io/projects/259">0x07</a>, use numbers in your answer file.</p><p>What is HTTPS?</p><ol><li>A secure version of HTTP</li><li>A faster version of HTTP</li><li>A superior version of HTTP</li></ol><p>Why do you need HTTPS?</p><ol><li>To encrypt credit card and social security number information going between the client and the website servers</li><li>To encrypt all communication between the client and the website servers</li><li>To accelerate the communication between the client and the website servers</li></ol><p>You want to setup HTTPS on your website, where shall you place the certificate?</p><ol><li>In a secure location where nobody can access it</li><li>You can host it anywhere but you have to share the link to it on your website</li><li>On your website web server(s)</li></ol> | [0-https_abc](./0-https_abc)                            
1 | **Mandatory** |<p>Configure your domain zone so that the subdomain <code>www</code> points to your load-balancer IP (<code>lb-01</code>).Let&#39;s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.</p><p>Requirements:</p><ul><li>Add the subdomain <code>www</code> to your domain, point it to your <code>lb-01</code> IP (your domain name might  be configured with default subdomains, feel free to remove them)</li><li>Add the subdomain <code>lb-01</code> to your domain, point it to your <code>lb-01</code> IP</li><li>Add the subdomain <code>web-01</code> to your domain, point it to your <code>web-01</code> IP</li><li>Add the subdomain <code>web-02</code> to your domain, point it to your <code>web-02</code> IP</li><li>Your Bash script must accept 2 arguments:<ol><li><code>domain</code>:<ul><li> type: string</li><li> what: domain name to audit</li><li>mandatory: yes</li></ul></li><li><code>subdomain</code>:<ul><li>type: string</li><li>what: specific subdomain to audit</li><li>mandatory: no</li></ul></li></ol></li><li>Output:  <code>The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]</code></li><li>When only the parameter <code>domain</code> is provided, display information for its subdomains <code>www</code>, <code>lb-01</code>, <code>web-01</code> and <code>web-02</code></li><li>When passing <code>domain</code> and <code>subdomain</code> parameters, display information for the specified subdomain</li><li>Ignore <code>shellcheck</code> case <code>SC2086</code></li><li>Must use: <ul><li><code>awk</code></li><li>at least one Bash function</li></ul></li><li>You do not need to handle edge cases such as:<ul><li>Empty parameters </li><li>Nonexistent domain names</li><li>Nonexistent subdomains</li></ul></li></ul><p>Example:</p> | [1-world_wide_web](./1-world_wide_web)                  
2 | **Mandatory** |<p>&quot;Terminating SSL on HAproxy&quot; means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to the next hope.</p><p>Create a certificate using <code>certbot</code> and configure <code>HAproxy</code> to accept encrypted traffic for your subdomain <code>www.</code>.</p><p>Requirements:</p><ul><li>HAproxy must be listening on port TCP 443</li><li>HAproxy must be accepting SSL traffic</li><li>HAproxy must serve encrypted traffic that will return the <code>/</code> of your web server</li><li>When querying the root of your domain name, the page returned must contain <code>Holberton School</code></li><li>Share your HAproxy config as an answer file (<code>/etc/haproxy/haproxy.cfg</code>)</li></ul><p>Make sure to install HAproxy 1.5 or higher, <a href="https://en.wikipedia.org/wiki/TLS_termination_proxy">SSL termination</a> is not available before v1.5.</p><p>Example:</p> | [2-haproxy_ssl_termination](./2-haproxy_ssl_termination)
3 | **Mandatory** |<p><img src="https://i.imgur.com/XMAT5aE.gif" alt="HTTP to HTTPS without a glitch"></p>    <p>A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.</p>    <p>Requirements:</p>    <ul>  <li>This should be transparent to the user</li>  <li>HAproxy should return a <a href="https://en.wikipedia.org/wiki/HTTP_301">301</a></li>  <li>HAproxy should redirect HTTP traffic to HTTPS</li>  <li>Share your HAproxy config as an answer file (<code>/etc/haproxy/haproxy.cfg</code>)</li>  </ul> | [3-redirect_http_to_https](./3-redirect_http_to_https)
