solutions 0x09-web_infrastructure_design </topic>

---

Application Server vs Web Server
Overview
This README outlines the setup of an infrastructure with separate components for an application server and a web server. The infrastructure includes a single server, a load balancer (HAProxy) configured as a cluster, and components split across multiple servers.

---

Components
Server
Purpose: Hosts the infrastructure components.
Reason for Addition: Provides computing resources for running the web server, application server, and database.
Load Balancer (HAProxy)
Purpose: Distributes incoming traffic across multiple servers.
Reason for Addition: HAProxy is configured as a cluster for high availability and fault tolerance.
Web Server
Purpose: Handles HTTP requests and serves static content.
Reason for Addition: Separates static content serving from dynamic content processing for better resource management.
Application Server
Purpose: Executes application logic, processes dynamic requests, and generates dynamic content.
Reason for Addition: Isolates application-specific tasks for security and scalability.
Database
Purpose: Stores and manages application data.
Reason for Addition: Provides dedicated resources and enhanced security for data storage.
Conclusion
This setup of separate components for the application server and web server, along with a load balancer and database, improves resource management, scalability, and security. Utilizing HAProxy as a cluster ensures high availability and fault tolerance for the infrastructure.

---

key concept:

0.Simple web stack
Requirements:
- 1 server
- 1 web server (Nginx)
- 1 application server
- 1 application files (your code base)
- 1 database (MySQL)
- 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

---

1.Distributed web infrastructure

Requirements:
- 2 servers
- 1 web server (Nginx)
- 1 application server
- 1 load-balancer (HAproxy)
- 1 set of application files (your code base)
- 1 database (MySQL)

---

2.Secured and monitored web infrastructure

Requirements:
- 3 firewalls
- 1 SSL certificate to serve www.foobar.com over HTTPS
- 3 monitoring clients (data collector for Sumologic or other monitoring services)

---

3.Scale up

Requirements:
- 1 server
- 1 load-balancer (HAproxy) configured as cluster with the other one
Split components (web server, application server, database) with their own server
You must be able to explain some specifics about this infrastructure:
For every additional element, why you are adding it

Thank You </topic>
