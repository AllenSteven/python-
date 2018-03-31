#!/usr/bin/env python3
#-*-coding:utf-8-*-

from socket import *

HOST = 'localhost'
PORT = 5000
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM) #创建数据报套接字

while True:
	data = input('>') #接收输入数据
	if not data:
		break
	print(data)
	udpCliSock.sendto(data.encode(), ADDR) #发送数据
	data, ADDR = udpCliSock.recvfrom(BUFSIZE) #接收数据
	if not data:
		break
	print(data.decode())
udpCliSock.close()

