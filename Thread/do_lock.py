#!/usr/bin/env python3
#-*-coding:utf-8-*-

import threading, time, os


balance = 0
lock = threading.Lock()

def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n
	print("balance is :", balance)

def run_thread(n):
	for i in range(100):
		lock.acquire()
		#try……finally…… 保证每次都能释放lock，让别的线程有机会获取锁
		try:
			change_it(n)
		finally:
			lock.release()
			
def main():
	print("main test")
	t1 = threading.Thread(target = run_thread, args = (5, ))
	t2 = threading.Thread(target = run_thread, args = (8, ))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print(balance)

if __name__ == '__main__':
	main()