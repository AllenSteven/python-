#!/usr/bin/env python3
#-*-coding:utf-8-*-

from multiprocessing import Process
import os

#进程函数
def run_proc(name):
	print("Run child process %s(%s)"%(name, os.getpid()))

def main():
	print("Parent process %s"%os.getpid())
	p = Process(target = run_proc, args=('test',)) #创建进程
	print("Child process will start")
	p.start()#启动进程
	p.join()#等待子进程结束
	print("Child process end")

if __name__== '__main__':
	print("test mutilprocessing")
	main()
	
	