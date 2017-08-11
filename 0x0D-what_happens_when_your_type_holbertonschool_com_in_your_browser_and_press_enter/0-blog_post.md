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

*   **Round-robin DNS** is a solution where the DNS lookup returns multiple IP addresses, rather than just one. For example, facebook.com actually maps to four IP addresses.
*   **Load-balancer** is the piece of hardware that listens on a particular IP address and forwards the requests to other servers. Major sites will typically use expensive high-performance load balancers.
*   **Geographic DNS** improves scalability by mapping a domain name to different IP addresses, depending on the client’s geographic location. This is great for hosting static content so that different servers don’t have to update shared state.
*   **Anycast** is a routing technique where a single IP address maps to multiple physical servers. Unfortunately, anycast does not fit well with TCP and is rarely used in that scenario.

Most of the DNS servers themselves use anycast to achieve high availability and low latency **of the DNS lookups**.



### The browser sends a HTTP request to the web server

You can be pretty sure that Facebook’s homepage will not be served from the browser cache because dynamic pages expire either very quickly or immediately (expiry date set to past).

So, the browser will send this request to the Facebook server:

<pre class="code">GET http://facebook.com/ HTTP/1.1
Accept: application/x-ms-application, image/jpeg, application/xaml+xml, <font style="color: lightblue">[...]</font>
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; <font style="color: lightblue">[...]</font>
Accept-Encoding: gzip, deflate
Connection: Keep-Alive
Host: facebook.com
Cookie: datr=1265876274-<font style="color: lightblue">[...]</font>; locale=en_US; lsd=WW<font style="color: lightblue">[...]</font>; c_user=2101<font style="color: lightblue">[...]</font></pre>

The GET request names the **URL** to fetch**:** “http://facebook.com/”. The browser identifies itself (**User-Agent** header), and states what types of responses it will accept (**Accept** and **Accept-Encoding** headers). The **Connection** header asks the server to keep the TCP connection open for further requests.

The request also contains the **cookies** that the browser has for this domain. As you probably already know, cookies are key-value pairs that track the state of a web site in between different page requests. And so the cookies store the name of the logged-in user, a secret number that was assigned to the user by the server, some of user’s settings, etc. The cookies will be stored in a text file on the client, and sent to the server with every request.

There is a variety of tools that let you view the raw HTTP requests and corresponding responses. My favorite tool for viewing the raw HTTP traffic is [fiddler](http://www.fiddler2.com/fiddler2/), but there are many other tools (e.g., FireBug) These tools are a great help when optimizing a site.
<hr>
In addition to GET requests, another type of requests that you may be familiar with is a POST request, typically used to submit forms. A GET request sends its parameters via the URL (e.g.: http://robozzle.com/puzzle.aspx**?id=85**). A POST request sends its parameters in the request body, just under the headers.

The trailing slash in the URL “http://facebook.com/” is important. In this case, the browser can safely add the slash. For URLs of the form http://example.com/folderOrFile, the browser cannot automatically add a slash, because it is not clear whether folderOrFile is a folder or a file. In such cases, the browser will visit the URL without the slash, and the server will respond with a redirect, resulting in an unnecessary roundtrip.

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
	
### 6\. The server ‘handles’ the request
	
The server will receive the GET request, process it, and send back a response.
							
This may seem like a straightforward task, but in fact there is a lot of interesting stuff that happens here – even on a simple site like my blog, let alone on a massively scalable site like facebook.
							
*   **Web server software** The web server software (e.g., IIS or Apache) receives the HTTP request and decides which request handler should be executed to handle this request. A request handler is a program (in ASP.NET, PHP, Ruby, …) that reads the request and generates the HTML for the response.
    In the simplest case, the request handlers can be stored in a file hierarchy whose structure mirrors the URL structure, and so for example [http://example.com/folder1/page1.aspx](http://example.com/folder1/page1.aspx) URL will map to file /httpdocs/folder1/page1.aspx. The web server software can also be configured so that URLs are manually mapped to request handlers, and so the public URL of page1.aspx could be [http://example.com/folder1/page1](http://example.com/folder1/page1).
*   **Request handler** The request handler reads the request, its parameters, and cookies. It will read and possibly update some data stored on the server. Then, the request handler will generate a HTML response.
										
One interesting difficulty that every dynamic website faces is how to store data. Smaller sites will often have a single SQL database to store their data, but sites that store a large amount of data and/or have many visitors have to find a way to split the database across multiple machines. Solutions include sharding (splitting up a table across multiple databases based on the primary key), replication, and usage of simplified databases with weakened consistency semantics.

One technique to keep data updates cheap is to defer some of the work to a batch job. For example, Facebook has to update the newsfeed in a timely fashion, but the data backing the “People you may know” feature may only need to be updated nightly (my guess, I don’t actually know how they implement this feature). Batch job updates result in staleness of some less important data, but can make data updates much faster and simpler.
										
										
## Web server generates an HTTP response containing that data.
										
## Web server sends that HTTP response back down the TCP/IP connection to your machine.

## Browser receives the HTTP response and splits it into headers (describing the data) and the body (the data itself).

### 7\. The server sends back a HTML response

![image](http://igoro.com/wordpress/wp-content/uploads/2010/02/image10.png "image")

Here is the response that the server generated and sent back:
	
	```
	HTTP/1.1 200 OK
	Cache-Control: private, no-store, no-cache, must-revalidate, post-check=0,
    pre-check=0
	Expires: Sat, 01 Jan 2000 00:00:00 GMT
	P3P: CP="DSP LAW"
	Pragma: no-cache
	Content-Encoding: gzip
	Content-Type: text/html; charset=utf-8
	X-Cnection: close
	Transfer-Encoding: chunked
	Date: Fri, 12 Feb 2010 09:05:55 GMT
	
	2b3  
	��������T�n�@����<font style="color: lightblue">[...]</font>
	```
The entire response is 36 kB, the bulk of them in the byte blob at the end that I trimmed.
		
The **Content-Encoding** header tells the browser that the response body is compressed using the gzip algorithm. After decompressing the blob, you’ll see the HTML you’d expect:
											
	<pre><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"   
		"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" 
	lang="en" id="facebook" class=" no_js">
	<head>
	<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
	<meta http-equiv="Content-language" content="en" />
	...</pre>
	
In addition to compression, headers specify whether and how to cache the page, any cookies to set (none in this response), privacy information, etc.
														
Notice the header that sets **Content-Type** to **text/html**. The header instructs the browser to render the response content as HTML, instead of say downloading it as a file. The browser will use the header to decide how to interpret the response, but will consider other factors as well, such as the extension of the URL.
														

## Browser interprets the data to decide how to display it in the browser - typically this is HTML data that specifies types of information and their general form.

### 8\. The browser begins rendering the HTML

Even before the browser has received the entire HTML document, it begins rendering the website:

### 9\. The browser sends requests for objects embedded in HTML
														 
![image](http://igoro.com/wordpress/wp-content/uploads/2010/02/image11.png "image")
														 
As the browser renders the HTML, it will notice tags that require fetching of other URLs. The browser will send a GET request to retrieve each of these files.
														 
Here are a few URLs that my visit to facebook.com retrieved:

 *   **Images**http://static.ak.fbcdn.net/rsrc.php/z12E0/hash/8q2anwu7.gif  
	     http://static.ak.fbcdn.net/rsrc.php/zBS5C/hash/7hwy7at6.gif  
		     …
 *   **CSS style sheets**http://static.ak.fbcdn.net/rsrc.php/z448Z/hash/2plh8s4n.css  
 http://static.ak.fbcdn.net/rsrc.php/zANE1/hash/cvtutcee.css  
 …
 *   **JavaScript files** http://static.ak.fbcdn.net/rsrc.php/zEMOA/hash/c8yzb6ub.js  
							     http://static.ak.fbcdn.net/rsrc.php/z6R9L/hash/cq2lgbs8.js  
																						     …
Each of these URLs will go through process a similar to what the HTML page went through. So, the browser will look up the domain name in DNS, send a request to the URL, follow redirects, etc.

However, static files – unlike dynamic pages – allow the browser to cache them. Some of the files may be served up from cache, without contacting the server at all. The browser knows how long to cache a particular file because the response that returned the file contained an Expires header. Additionally, each response may also contain an ETag header that works like a version number – if the browser sees an ETag for a version of the file it already has, it can stop the transfer immediately.

Can you guess what **“fbcdn.net”** in the URLs stands for? A safe bet is that it means “Facebook content delivery network”. Facebook uses a content delivery network (CDN) to distribute static content – images, style sheets, and JavaScript files. So, the files will be copied to many machines across the globe.

Static content often represents the bulk of the bandwidth of a site, and can be easily replicated across a CDN. Often, sites will use a third-party CDN provider, instead of operating a CND themselves. For example, Facebook’s static files are hosted by Akamai, the largest CDN provider.

As a demonstration, when you try to ping static.ak.fbcdn.net, you will get a response from an akamai.net server. Also, interestingly, if you ping the URL a couple of times, may get responses from different servers, which demonstrates the load-balancing that happens behind the scenes.

### 10\. The browser sends further asynchronous (AJAX) requests

![image](http://igoro.com/wordpress/wp-content/uploads/2010/02/image12.png "image")

In the spirit of Web 2.0, the client continues to communicate with the server even after the page is rendered.

For example, Facebook chat will continue to update the list of your logged in friends as they come and go. To update the list of your logged-in friends, the JavaScript executing in your browser has to send an asynchronous request to the server. The asynchronous request is a programmatically constructed GET or POST request that goes to a special URL. In the Facebook example, the client sends a POST request to http://www.facebook.com/ajax/chat/buddy_list.php to fetch the list of your friends who are online.

This pattern is sometimes referred to as “AJAX”, which stands for “Asynchronous JavaScript And XML”, even though there is no particular reason why the server has to format the response as XML. For example, Facebook returns snippets of JavaScript code in response to asynchronous requests.

Among other things, the fiddler tool lets you view the asynchronous requests sent by your browser. In fact, not only you can observe the requests passively, but you can also modify and resend them. The fact that it is this easy to “spoof” AJAX requests causes a lot of grief to developers of online games with scoreboards. (Obviously, please don’t cheat that way.)

Facebook chat provides an example of an interesting problem with AJAX: pushing data from server to client. Since HTTP is a request-response protocol, the chat server cannot push new messages to the client. Instead, the client has to poll the server every few seconds to see if any new messages arrived.

[Long polling](http://en.wikipedia.org/wiki/Push_technology#Long_polling) is an interesting technique to decrease the load on the server in these types of scenarios. If the server does not have any new messages when polled, it simply does not send a response back. And, if a message for this client is received within the timeout period, the server will find the outstanding request and return the message with the response.



# Sources






[What really happens when you navigate to a URL](http://igoro.com/archive/what-really-happens-when-you-navigate-to-a-url)

As a software developer, you certainly have a high-level picture of how web apps work and what kinds of technologies are involved: the browser, HTTP, HTML, web server, request handlers, and so on.

In this article, we will take a deeper look at the sequence of events that take place when you visit a URL.

https://stackoverflow.com/questions/5165310/what-is-the-complete-process-from-entering-a-url-to-the-browsers-address-bar-to

https://stackoverflow.com/questions/2092527/what-happens-when-you-type-in-a-url-in-browser
																							 
