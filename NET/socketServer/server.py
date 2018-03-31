#!/usr/bin/env python3
#-*-coding:utf-8-*-

#python2中使用SocketServer, python3使用socketserver
from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH) 
from time import ctime

HOST = ''
PORT = 5000
ADDR = (HOST, PORT)

#由StreamRequestHandler派生一个MyRequestHandler类，并重写了handle()函数
class MyRequestHandler(SRH):
	def handle(self):
		print('...connected from :',self.client_address)
		#像操作文件一样操作套接字，并注意编码问题
		self.wfile.write(('[%s] %s'%(ctime(),self.rfile.readline().decode())).encode())
#根据地址和请求处理类创建tcp服务器
tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection....')
#循环等待客户请求并处理请求。
tcpServ.serve_forever()