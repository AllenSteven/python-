#!/usr/bin/env python3
#-*-coding:utf-8-*-

try:
	f = open('test', 'rw')
	print(f.read())
	f.write("hello world!")
finally:
	if f:
		f.close()
		
with open('test', 'rw') as f:
	print(f.read())
	f.write("hello, python!")