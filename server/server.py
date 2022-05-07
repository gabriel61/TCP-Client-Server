# Author: Gabriel Sampaio de Oliveira

import socket
import os
import pickle
import sys
import threading

# List of global variables

cache = { }

cacheSize = 0

bufferSize = 1024

# Max size of the cache memory => 64mb
cacheMax = 64*(1024*1024)


# Client to server connection
def connection(direc, conn, addr, lock):
   
   os.chdir(direc)

   request = conn.recv(bufferSize).decode()
   
   print(f'Client {addr} is requesting file {request}')
   
   global cache
   global cacheSize

   if(request == 'list'):
      conn.send(pickle.dumps(getFiles()))
      conn.close()
      print('Cache request sent to the client')
   
   else:
      lock.acquire()
      if(cache.get(str(request))):
         print(f'{request} sent to client.')
         payloadFile = cache.get(str(request))
         data = pickle.loads(payloadFile['data'])
         conn.send(data)
         conn.close()
   
      else:
         if(os.path.isfile(request)):        
            with open(request, 'rb') as file:
                
               fileSize = os.path.getsize(request)
               payloadFile = file.read()
               
               if(fileSize <= cacheMax):

                  payloadCache = b''
                  
                  while(payloadFile):
                      
                     conn.send(payloadFile)
                     payloadCache += payloadFile
                     payloadFile = file.read(bufferSize)
                  
                  payload = pickle.dumps(payloadCache)
                  
                  while(cacheSize + fileSize > cacheMax):
                      
                     cacheSize = remove(fileSize)
                  
                  toCache = {str(request): {'size': fileSize, 'data': payload}}
                  cacheSize += fileSize
                  cache.update(toCache)
                  
               else:
                  while(payloadFile):
                      
                     conn.send(payloadFile)
                     payloadFile = file.read(bufferSize)
                     
            file.close()
            conn.close()
            print(f'Cache miss. File {request} sent to client')
         
         else:
            conn.send(b'File not found')
            conn.close()
            print(f'File {request} not found.')
   
   lock.release()
   
# Functions of remove and get files

def remove(size_file):
   removeSize = 0
   removeKey = ''
   count = 0
   
   for key in cache:
       
      file = cache.get(key)
      currentKey = key
      currentSize = file['size']
      
      if(file['size'] >= size_file):
         removeSize = currentSize
         removeKey = currentKey
         break
     
      else:
         if(removeSize >= count):
            count = currentSize
            removeSize = count
            removeKey = currentKey
            
   cache.pop(removeKey)
   
   return (cacheSize - removeSize)

def getFiles():
   list = []
   for key in cache.keys(): 
      list.append(key) 
   return list

# main

if __name__ == "__main__":
    
   print("Server starting...")

   host = 'localhost'
   port = sys.argv[1]
   directory = sys.argv[2]

   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   s.bind((host, int(port)))

   while True:
      s.listen()
      conn, addr = s.accept()
      lock = threading.Semaphore()
      client = threading.Thread(target=connection, args=(directory, conn, addr, lock))
      client.start()
   
   s.close()