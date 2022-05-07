<h1 align="center">Implementation of a TCP client-server</h1>
<br>

## 💻 Challenge
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
The server creates a Thread for each connection made, being able to be accessed by several different ports, so the client can pass the port it wants to access if it is not in use. In the while loop, the accept method receives the conn and addr. Thus starting new threads as requested, directing to the connection function passing the directory, conn, addr and the lock variable lock.

The connection function handles requests made by the client, which returns the list of files requested if the client uses the 'list' method, so the server checks if the file is present in the cache. If it exists, the server first checks if the file is compatible with the cache size, if so, the server sends the file to the client, followed by the termination of the connection; If supported, the server serializes the payload of the file and caches it. If the file is not present in the cache, the server sends a message to the client stating that the file does not exist in the directory.
	
To store the payload of the file, we use the FIFO method of data structure, where first in is first out, that is, if the cache exceeds the size of 64MB, then the first file will leave the cache to make room for the new file and so on.
	
It is worth mentioning that our cache memory also has a registry key for each file, containing the size of the file and the date that is the payload of the file.

```python
#To start the server just run the code:
python server.py [port] ./
```
</p>
<br>


### Client
<p align="justify">
In the client code we also make use of the socket and sys library, sys allows us to receive the arguments that are passed in the execution. Thus, we have the implementation of a TCP client that takes as a parameter the server, the port, the file and the location where the file will be saved.
	
```python
#To resquest the file:
python client.py localhost [server port] [file name]./
	
#To resquest the list of files:
python client.py localhost [server port] list
```
	
</p>
<br>

### ⚒ Technologies used

-   **[Python](https://www.python.org/)**
-   **[Git](https://git-scm.com/)**

### ⚒ Packages needed
- os
- pickle
- socket
- sys
- threading

</br>

---

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

