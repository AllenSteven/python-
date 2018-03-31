#!/usr/bin/env python3
#-*-coding:utf-8-*-

from multiprocessing import Process, Queue
import os, time, random

def write(q):
	print('Process to write: %s'%os.getpid())
	for value in ['A','B','C']:
		q.put(value)
	time.sleep(random.random())

def read(q):
	print('Process to read: %s'%os.getpid())
	while True:
		value = q.get(True)
		print('read value: %s'%value)

def main():
	print('parent process (%s)run'%os.getpid())
	q = Queue()
	pw = Process(target = write, args = (q,))
	pr = Process(target = read, args = (q,))
	pw.start()
	pr.start()
	pw.join() #等待pw线程结束
	pr.terminate()#pr线程中是死循环，无法等待结束，只能强行终止
	
if __name__ == '__main__':
	print("test queue")
	main()