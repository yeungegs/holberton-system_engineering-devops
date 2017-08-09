*User types https://www.holbertonschool.com into your browser and press Enter.*
*Browser splits what you type (the URL) into a hostname and a path.
*Browser forms an HTTP request to ask for the data at the given hostname and path.
*Browser performs DNS lookup to resolve the hostname into an IP address.
* The browser checks the cache for a DNS record to find the corresponding IP address of holbertonschool.com.
  * 
  * DNS(Domain Name System) is a database that maintains the name of the website (URL) and the particular IP address it links to. Every single URL on the internet has a unique IP address assigned to it. The IP address belongs to physical server that hosts the server of the website we are requesting to access. 
  * If the requested URL is not in the cache, ISP’s DNS server initiates a DNS query to find the IP address of the server that hosts www.holbertonschool.com
  
Browser forms a TCP/IP connection to the computer specified via the IP address. (This connection is actually formed out of many computers, each passing the data along to the next.)


  * After receiving the correct IP address, the browser builds a connection with the server that matches the IP address to transfer information. The protocol to build this connection is called TCP.
  * In order to transfer data packets between your computer(client) and the server, it is important to have a TCP connection established. This connection is established using a process called the TCP/IP three-way handshake. This is a three step process where the client and the server exchange SYN(synchronize) and ACK(acknowledge) messages to establish a connection.
  * Client machine sends a SYN packet to the server over the internet asking if it is open for new connections.
  * If the server has open ports that can accept and initiate new connections, it’ll respond with an ACKnowledgment of the SYN packet using a SYN/ACK packet.
  * The client will receive the SYN/ACK packet from the server and will acknowledge it by sending an ACK packet.
  * Then a TCP connection is established for data transmission!

*Browser sends the HTTP request down the connection to the given IP address.
*That computer receives the HTTP request from the TCP/IP connection and passes it to the web server program.
*Web server reads the hostname and path and finds or generates the data that you've asked for.
*Web server generates an HTTP response containing that data.
*Web server sends that HTTP response back down the TCP/IP connection to your machine.
*Browser receives the HTTP response and splits it into headers (describing the data) and the body (the data itself).
*Browser interprets the data to decide how to display it in the browser - typically this is HTML data that specifies types of information and their general form.
*Some of the data will be metadata that specifies further resources that need to be loaded, such as style sheets for detailed layout, or inline images, or Flash movies. This metadata is specified again as a URL, and this whole process repeats for each one until all are loaded.


* The server sends out an HTTP response.
  * The server response contains the web page you requested as well as the status code, compression type (Content-Encoding), how to cache the page (Cache-Control), any cookies to set, privacy information, etc.

* A load balancer acts as the “traffic cop” sitting in front of your servers and routing client requests across all servers capable of fulfilling those requests in a manner that maximizes speed and capacity utilization and ensures that no one server is overworked, which could degrade performance. If a single server goes down, the load balancer redirects traffic to the remaining online servers. When a new server is added to the server group, the load balancer automatically starts to send requests to it.

In this manner, a load balancer performs the following functions:

* Distributes client requests or network load efficiently across multiple servers
* Ensures high availability and reliability by sending requests only to servers that are online
* Provides the flexibility to add or subtract servers as demand dictates
	  
8. The browser displays the HTML content (for HTML responses which is the most common).
The browser displays the HTML content in phases. First, it will render the bare bone HTML skeleton. Then it will check the HTML tags and sends out GET requests for additional elements on the web page, such as images, CSS stylesheets, JavaScript files etc. These static files are cached by the browser so it doesn’t have to fetch them again the next time you visit the page. At the end, you’ll see www.holbertonschool.com appearing on your browser.

