Web Server

Description:
This is a simple web server written in vanilla Python, without using frameworks like Flask or Django.
Using BaseHTTPServer, BaseHTTPRequestHandler and HTTPServer libraries to deal with HTTP requests.

Basic Structure:
Web Sever Code consists of two main parts:
1)	Handler Class
2)	Main

The Handler Class indicates which code needs to be executed, based on HTTP request types like GET, POST, DELETE, etc.
The main method is responsible for instantiating the server, specify the port number to listen (in case of local host), and start the server.

See the example code in webserver.py which runs a simple server locally and handles multiple GET and POST requests.
To run the server, file webserver.py on command prompt and open the browser and navigate to http://localhost:8080/hello . The page should display Hello and a small input box and sample messages.
