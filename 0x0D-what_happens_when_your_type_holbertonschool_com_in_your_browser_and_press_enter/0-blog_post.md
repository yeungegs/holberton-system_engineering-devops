**Requirements, your post must cover:**
  * DNS request
  * TCP/IP
  * Firewall
  * HTTPS/SSL
  * Load-balancer
  * Web server
  * Application server
  * Database
								
*User types https://www.holbertonschool.com into your browser and press Enter.*

## 1. The browser checks the cache for a DNS record to find the corresponding IP address of holbertonschool.com.

  * DNS(Domain Name System) is a database that maintains the name of the website (URL) and the particular IP address it links to. Every single URL on the internet has a unique IP address assigned to it. The IP address belongs to physical server that hosts the server of the website we are requesting to access. 
  * If the requested URL is not in the cache, ISP’s DNS server initiates a DNS query to find the IP address of the server that hosts www.holbertonschool.com

##	2. TCP/IP

  * After receiving the correct IP address, the browser builds a connection with the server that matches the IP address to transfer information. The protocol to build this connection is called TCP.
  * In order to transfer data packets between your computer(client) and the server, it is important to have a TCP connection established. This connection is established using a process called the TCP/IP three-way handshake. This is a three step process where the client and the server exchange SYN(synchronize) and ACK(acknowledge) messages to establish a connection.
  * Client machine sends a SYN packet to the server over the internet asking if it is open for new connections.
  * If the server has open ports that can accept and initiate new connections, it’ll respond with an ACKnowledgment of the SYN packet using a SYN/ACK packet.
  * The client will receive the SYN/ACK packet from the server and will acknowledge it by sending an ACK packet.
  * Then a TCP connection is established for data transmission!

##	3. Firewall
##	4. HTTPS/SSL
##	5. Load-balancer
##	6. Web server
##	7. Application server
##	8. Database
					   
