#!/usr/bin/env python
#-*-coding:utf-8-*-

from socket import *

HOST = 'localhost'
PORT = 5000
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data = input('>')
	if not data:
		break
	print(data)
	tcpCliSock.send(data.encode())
	data = tcpCliSock.recv(BUFSIZE).decode()
	if not data:
		break
	print(data)

tcpCliSock.close()


#ERROR:
#Traceback (most recent call last):
#  File "F:\workspace\python\NET\tcp\client.py", line 19, in <module>
#    tcpCliSock.send(data)
#TypeError: a bytes-like object is required, not 'str'
