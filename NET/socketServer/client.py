#!/usr/bin/env python3
#-*-coding:utf-8-*-

from socket import *

HOST = 'localhost'
PORT = 5000
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
	tcpCliSock = socket(AF_INET, SOCK_STREAM) #因为服务器的SocketServer处理器的默认行为是接受连接，得到请求，
	#关闭连接，所以客户端不能一直保持连接状态，每次发送数据到服务器都得重新创建套接字
	tcpCliSock.connect(ADDR)
	data = input('>')
	if not data:
		break
	tcpCliSock.send(('%s\r\n'%data).encode())#因为服务器的文件处理类像文件操作套接字，所以需要添加回车换行符。
	data = tcpCliSock.recv(BUFSIZE)
	if not data:
		break
	print(data.decode().strip()) #去掉接收到的回车换行
	tcpCliSock.close()