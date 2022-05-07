<h1 align="center">Implementation of a TCP client-server</h1>
<br>

## Challenge
<p align="justify">
The project consists of building a TCP server where the client requests files from the server.
	
- The server must return to the client a list of all the files contained in its cache memory.
- The cache must have a maximum size of 64MB.
- The server must be multi-threaded.
- There must be a function that allows the client to get a list containing the names of files in the server's cache that must follow the following command line pattern: ./tcp_client server_host server_port list
</p>
<br>

### Server
<p align="justify">
The server, being Multi-Thread, creates a Thread for each connection made.

</p>
<br>


#### Server

The server consists of a server-TCP Multi-Thread implementation, in which, for each connected client, a Thread is created, executing the flow of its requests in parallel, with concurrent control over the read / write in the cache memory.

The cache memory is implemented as a hash table, in which the registry key for each element is the name of the file, and the properties, file_size: containing the file size and date: payload of the file. Example:

```python
CACHE = {
	file_name = {file_size: 'Size', data: 'Payload file'},
	.
	.
	.
}
```
##### Features
When establishing the connection with the client, the server starts to wait for your request, which can be:

1. List of files present in the server's cache

Upon receiving this request, the server sends the client a list with the name of the files that are allocated in the cache memory of the server, afterwards it closes the connection.

2. Request for files located in the server directory

File requests follow the following flows:

Initially the server checks whether the requested file is allocated in its cache memory. If so, the file's payload goes through the deserialization process, followed by sending it to the client. When finished, the connection is ended.
If the requested file is not in the cache memory of the server, the following are the flows:

```python
if The file exists on the server {
  Check if the file size is bigger than the cache memory size {
	  The server sends the file to the client, followed by the connection termination
  } 
  else {
	The server opens the file, followed by sending, according to the size specified for the buffer. 
	At the end of the sending, the server serializes the payload of the file and stores it in the cache 
	memory, in order to provide the file more quickly in the next requests.
  }
} 
else {
	The server sends a message to the client stating that the file does not exist in its current directory.
} 
```
In the stage of storing the payload of the file, a check is made of the available space in the cache memory, which has a size limitation of 64 MB. If the size of the file in question exceeds the limit value of the cache memory, there is a process of reallocation of the files present in the cache.

The strategy used for the relocation process is to check if there are any files in cache memory, which are larger in size than the file being requested, so remove this file and store the new one.
If none of the files are larger than the requested file, a cycle of removing the files follows until the cache has enough space to allocate the new file.

<p align="center">
  <img src="assets/server-actions.gif" />
</p>

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

1. ##### Windows
	**Install Python3 or higher**
	[Python Releases](https://www.python.org/downloads/windows/)
	
	* To manage packages in Python3
		Download  [get-pip.py](https://bootstrap.pypa.io/get-pip.py)  to a folder on your computer.
		Open a command prompt and navigate to the folder containing the get-pip.py installer.
		Run the following command:

	```sh
	python get-pip.py
	```
	* Packages needed
	```sh
	pip3 install os, pickle, socket, sys, threading
	```
2. ##### Linux Systems
	**Install Python3 or higher**
	```sh
	sudo apt-get install python3.6
	```

	* Update your system
	```sh
	sudo apt update
	sudo apt -y upgrade
	```

	* To manage packages in Python3
	```sh
	sudo apt install -y python3-pip
	```

	* Packages needed
	```sh
	pip3 install os, pickle, socket, sys, threading
	```

### Execution

* Server
	```sh
	python3 server.py port_to_listen directory
	```

* Client
	```sh
	python3 client.py host_server server_port_listen file_name directory #for file request
	
	python3 client.py host_server server_port_listen list #for information on files in cache memory
	```
	

### ✒️ Autor

</br>

<a href="https://github.com/gabriel61">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/gabriel61" width="100px;" alt=""/>
 <br />
 
 [![Linkedin Badge](https://img.shields.io/badge/-gabrielsampaio-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/gabriel-oliveira-852759190/)](https://www.linkedin.com/in/gabriel-oliveira-852759190/)
<br>
sogabris@gmail.com
<br>

---

