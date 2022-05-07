# Author: Gabriel Sampaio de Oliveira

import socket
import os
import pickle
import sys

bufferSize = 1024

# Functions of request and listing of files

def requestFile(directory, r, request):
    
    os.chdir(directory)
    r.send(request.encode())

    with open(request, 'wb') as file:
        
        have = True
        
        while True:
            
            data = r.recv(bufferSize)
            
            if(data == b'File not found'):
                
                print('File not found.')
                os.remove(request)
                have = False
                break
            
            if not data:
                break
            file.write(data)
            
    file.close()
    
    if(have):
        print(f'File {request} saved.')
    r.close()
    
def listRequest(r, request):
    
    r.send(request.encode())
    filesCache = r.recv(bufferSize)
    print(pickle.loads(filesCache))
    
# main

if __name__ == "__main__":
    
    host = sys.argv[1]
    port = sys.argv[2]
    request = sys.argv[3]

    r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r.connect((host, int(port)))

    if(request == 'list'):
        listRequest(r, request)
    else:
        directory = sys.argv[4]
        requestFile(directory, r, request)