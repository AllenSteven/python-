#!/usr/bin/env python3
#-*-coding:utf-8-*-

from socket import *
from time import ctime

HOST = ''
PORT = 5000
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
while True:
	print('waiting for client connection request')
	tcpCliSock, addr = tcpSerSock.accept()
	print('...connection from ',addr)
	while True:
		data = tcpCliSock.recv(BUFSIZE).decode()
		if not data:
			break
		else:
			print("recv data from data:",data)
			tcpCliSock.send(('[%s] %s'%(ctime(), data)).encode())
	tcpCliSock.close()
tcpSerSock.close()	