#!/usr/bin/env python3
#-*-coding:utf-8-*-

from socket import *
from time import ctime

HOST = ''
PORT = 5000
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM) #创建数据报套接字
udpSerSock.bind(ADDR) #绑定地址和端口号到套接字

while True:
	data, addr = udpSerSock.recvfrom(BUFSIZE) #从服务器接收数据
	if not data:
		break
	print('recv data from  ',addr)
	print('The data is: ',data.decode())
	udpSerSock.sendto(('[%s] %s'%(ctime(), data.decode())).encode(),addr) #发送数据到端口

udpSerSock.close() #关闭套接字