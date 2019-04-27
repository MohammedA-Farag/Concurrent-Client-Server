# -*- coding: utf-8 -*-
"""

@author: mohmd farag
"""
from socket import socket, AF_INET, SOCK_STREAM
from threading import *

def receive_thread(s):
    while True:
        x=s.recv(500)
        print("server: ",x.decode('UTF-8'))

s=socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1',7002))
receive=Thread(target=receive_thread,args=(s,))
receive.start()
while True:
    s.send(input("==> ").encode('UTF-8'))
