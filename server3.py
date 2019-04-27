# -*- coding: utf-8 -*-
"""

@author: mohmd farag
"""
#socket module
from socket import socket, AF_INET, SOCK_STREAM
from _thread import *
from threading import *

#fun to handling receive of message 
def receive_thread(c):
    while True:
        x = c.recv(500) 
        print("client : ",x.decode('UTF-8'))

#fun to create thread for receive and handle sending
def client_thread(c): 
    #create a new thread.
    receive=Thread(target= receive_thread, args=(c,))
    receive.start()
    while True:
        c.send(input("==> ").encode('UTF-8'))
#Initiate (family(IPV4) , Type of protocol(TCP))       
s=socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 7002
s.bind((host, port))
s.listen(5)
print ("Server established")
while True:
    # the connection, and the address of the client.(hostaddr, port)
    c, add=s.accept()
    print("connection from", add[0])
    #create thread for serving that session.
    start_new_thread(client_thread,(c,))
