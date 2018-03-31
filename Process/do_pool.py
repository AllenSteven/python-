#!/usr/bin/env python
#-*-coding:utf-8-*-

from multiprocessing import Pool
import time, os, random

def long_time_task(name):
	print("Run the task %s (%s)"%(name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print("run %s seconds"%(end - start))
	print("The task %s run %f seconds"%(name, (end - start)))

def main():
	print("Parent process %s"%os.getpid())
	p = Pool(4) #创建线程池
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print("waiting for all subprocess over")
	p.close()
	p.join()
	print("Parent finished")

if __name__ == '__main__':
	print("Pool testing")
	main()