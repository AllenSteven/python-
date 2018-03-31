#!/usr/bin/env python3
#-*-coding:utf-8-*-

import time , threading

def loop():
	print("Thread %s is running"%threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print("Thread %s is running >> %s"%(threading.current_thread().name, n))
		time.sleep(5)
	print("Thread %s end."%threading.current_thread().name)

def main():
	print("Thread %s is running"%threading.current_thread().name)
	#创建线程，传入loop函数
	t = threading.Thread(target = loop, name = "SubLoop")
	t.start()
	t.join()
	print("Thread %s is ended."%threading.current_thread().name)
	
if __name__ == '__main__':
	print("test thread")
	main()