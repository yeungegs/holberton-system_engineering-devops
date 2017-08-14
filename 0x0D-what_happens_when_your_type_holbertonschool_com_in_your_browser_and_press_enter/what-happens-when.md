# What happens when a URL is entered into a browser?
## Browser splits what you type (the URL) into a hostname and a path.

The URL is typed into the browser and the `Enter` key is pressed.

![image](https://user-images.githubusercontent.com/23224088/29146814-28356582-7d18-11e7-91cf-160661210161.png)

## Browser forms an HTTP request to ask for the data at the given hostname and path.

### The browser looks up the IP address for the domain name


The first step in the navigation is to figure out the IP address for the visited domain. The DNS lookup proceeds as follows:

*   **Browser cache –** The browser caches DNS records for some time. Interestingly, the OS does not tell the browser the time-to-live for each DNS record, and so the browser caches them for a fixed duration (varies between browsers, 2 – 30 minutes).
*   **OS cache** – If the browser cache does not contain the desired record, the browser makes a system call (gethostbyname in Windows). The OS has its own cache.
*   **Router cache** – The request continues on to your router, which typically has its own DNS cache.
*   **ISP DNS cache** – The next place checked is the cache ISP’s DNS server. With a cache, naturally.
*   **Recursive search** – Your ISP’s DNS server begins a recursive search, from the root nameserver, through the .com top-level nameserver, to Holberton School's nameserver. Normally, the DNS server will have names of the .com nameservers in cache, and so a hit to the root nameserver will not be necessary.

Here is a diagram of what a recursive DNS search looks like:
![image](https://user-images.githubusercontent.com/23224088/29202749-deeb63f0-7e1f-11e7-8662-a5addceaa5ca.png)

Aspects to consider about managing traffic: 

*   **Round-robin DNS** is a solution where the DNS lookup returns multiple IP addresses, rather than just one.
*   **Load-balancer** is the piece of hardware that listens on a particular IP address and forwards the requests to other servers. Major sites will typically use expensive high-performance load balancers.
*   **Geographic DNS** improves scalability by mapping a domain name to different IP addresses, depending on the client’s geographic location. This is great for hosting static content so that different servers don’t have to update shared state.
*   **Anycast** is a routing technique where a single IP address maps to multiple physical servers. Unfortunately, anycast does not fit well with TCP and is rarely used in that scenario.

Most of the DNS servers themselves use anycast to achieve high availability and low latency **of the DNS lookups**.



### The browser sends a HTTP request to the web server

So, the browser will send this request to the Holberton school server:

```
Request URL:https://www.holbertonschool.com/
Request Method:GET
Status Code:200 OK
Remote Address:52.206.180.197:443
Referrer Policy:no-referrer-when-downgrade
```

Using Chrome developer tools, you can see the GET request:
```
GET / HTTP/1.1
Host: www.holbertonschool.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.8
Cookie: _ga=GA1.2.327418229.1502432403; _gid=GA1.2.1988454284.1502432403; _holberton_session=S1Y4WkJuMWJCTG[...]
DNT: 1
If-None-Match: W/"84d46cf170956ba8f[...]"
```

The GET request names the **URL** to fetch**:** “www.holbertonschool.com”. The browser identifies itself (**User-Agent** header), and states what types of responses it will accept (**Accept** and **Accept-Encoding** headers). The **Connection** header asks the server to keep the TCP connection open for further requests.

The request also contains the **cookies** that the browser has for this domain. Cookies are key-value pairs that track the state of a web site in between different page requests. And so the cookies store the name of the logged-in user, a secret number that was assigned to the user by the server, some of user’s settings, etc. The cookies will be stored in a text file on the client, and sent to the server with every request.

## Browser performs DNS lookup to resolve the hostname into an IP address.

* The browser checks the cache for a DNS record to find the corresponding IP address of holbertonschool.com.
* DNS(Domain Name System) is a database that maintains the name of the website (URL) and the particular IP address it links to. Every single URL on the internet has a unique IP address assigned to it. The IP address belongs to physical server that hosts the server of the website we are requesting to access. 
* If the requested URL is not in the cache, ISP’s DNS server initiates a DNS query to find the IP address of the server that hosts www.holbertonschool.com
	
## Browser forms a TCP/IP connection to the computer specified via the IP address. (This connection is actually formed out of many computers, each passing the data along to the next.)
				
	* After receiving the correct IP address, the browser builds a connection with the server that matches the IP address to transfer information. The protocol to build this connection is called TCP.
	* In order to transfer data packets between your computer(client) and the server, it is important to have a TCP connection established. This connection is established using a process called the TCP/IP three-way handshake. This is a three step process where the client and the server exchange SYN(synchronize) and ACK(acknowledge) messages to establish a connection.
	* Client machine sends a SYN packet to the server over the internet asking if it is open for new connections.
	* If the server has open ports that can accept and initiate new connections, it’ll respond with an ACKnowledgment of the SYN packet using a SYN/ACK packet.
	* The client will receive the SYN/ACK packet from the server and will acknowledge it by sending an ACK packet.
	* Then a TCP connection is established for data transmission!
							
## Browser sends the HTTP request down the connection to the given IP address.

### The browser follows the redirect
							
The browser now knows that “http://www.holbertonschool.com” is the correct URL to go to, and so it sends out another GET request:
							
The meaning of the headers is the same as for the first request.
	
## That computer receives the HTTP request from the TCP/IP connection and passes it to the web server program.
	
## Web server reads the hostname and path and finds or generates the data that you've asked for.
	
### The server ‘handles’ the request
	
The server will receive the GET request, process it, and send back a response.
							
*   **Web server software** The web server software (e.g., IIS or Apache) receives the HTTP request and decides which request handler should be executed to handle this request. A request handler is a program (in ASP.NET, PHP, Ruby, …) that reads the request and generates the HTML for the response.
    In the simplest case, the request handlers can be stored in a file hierarchy whose structure mirrors the URL structure, and so for example [http://example.com/folder1/page1.aspx](http://example.com/folder1/page1.aspx) URL will map to file /httpdocs/folder1/page1.aspx. The web server software can also be configured so that URLs are manually mapped to request handlers, and so the public URL of page1.aspx could be [http://example.com/folder1/page1](http://example.com/folder1/page1).
*   **Request handler** The request handler reads the request, its parameters, and cookies. It will read and possibly update some data stored on the server. Then, the request handler will generate a HTML response.
										
## Web server generates an HTTP response containing that data.
										
## Web server sends that HTTP response back down the TCP/IP connection to your machine.

## Browser receives the HTTP response and splits it into headers (describing the data) and the body (the data itself).

### The server sends back a HTML response

Here is the response that the server generated and sent back:
	
	```
	HTTP/1.1 200 OK
	Cache-Control: max-age=0, private, must-revalidate
	Content-Type: text/html; charset=utf-8
	Date: Fri, 11 Aug 2017 06:44:25 GMT
	ETag: W/"[...]"
	Server: nginx/1.10.2
	Set-Cookie: [...]; path=/; HttpOnly
	X-Content-Type-Options: nosniff
	X-Frame-Options: SAMEORIGIN
	X-Request-Id: [...]
	X-Runtime: 0.036422
	X-XSS-Protection: 1; mode=block
	Content-Length: 38278
	Connection: keep-alive
	```	
In addition to compression, headers specify whether and how to cache the page, any cookies to set (none in this response), privacy information, etc.
														
Notice the header that sets **Content-Type** to **text/html**. The header instructs the browser to render the response content as HTML, instead of say downloading it as a file. The browser will use the header to decide how to interpret the response, but will consider other factors as well, such as the extension of the URL.
														

## Browser interprets the data to decide how to display it in the browser - typically this is HTML data that specifies types of information and their general form.

### The browser begins rendering the HTML

Even before the browser has received the entire HTML document, it begins rendering the website:

### The browser sends requests for objects embedded in HTML
														 
As the browser renders the HTML, it will notice tags that require fetching of other URLs. The browser will send a GET request to retrieve each of these files.
														 
Here are a few URLs that my visit to www.holbertonschool.com retrieved:

 *   **Images**
	 https://holbertonschool.s3.amazonaws.com/mentors/photos/000/000/066/regular/0b81ca9.jpg?1442537878
	 https://www.holbertonschool.com/assets/staticmap-37b8960d592c4756da67a68d019b3d8315cf51479bba144692b68a04682cc12f.png
 *   **CSS style sheets**
	 https://www.holbertonschool.com/assets/application-77b63277231a8c975fa6578252cf414063e1d522a73096fc9c493e3d7d70963e.css
	 https://fonts.googleapis.com/css?family=Lora:400,700
	 https://maxcdn.bootstrapcdn.com/font-awesome/4.6.0/css/font-awesome.min.css
 *   **JavaScript files**
	 https://www.google-analytics.com/analytics.js
	 https://connect.facebook.net/en_US/sdk.js
																						     …
Each of these URLs will go through process a similar to what the HTML page went through. So, the browser will look up the domain name in DNS, send a request to the URL, follow redirects, etc.

# Sources
[What really happens when you navigate to a URL](http://igoro.com/archive/what-really-happens-when-you-navigate-to-a-url)

As a software developer, you certainly have a high-level picture of how web apps work and what kinds of technologies are involved: the browser, HTTP, HTML, web server, request handlers, and so on.

In this article, we will take a deeper look at the sequence of events that take place when you visit a URL.

https://stackoverflow.com/questions/5165310/what-is-the-complete-process-from-entering-a-url-to-the-browsers-address-bar-to

https://stackoverflow.com/questions/2092527/what-happens-when-you-type-in-a-url-in-browser
																							 
