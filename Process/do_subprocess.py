#!/usr/bin/env python3
#-*-coding:utf-8-*-

import subprocess

def test1_subprocess():
	print('$ nslookup www.python.org')
	r = subprocess.call(['nslookup', 'www.python.org'])
	print('Exit code:',r)
	
if __name__ == '__main__':
	test1_subprocess()