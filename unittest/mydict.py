#!/usr/bin/env python
#-*-coding:utf-8-*-

class Dict(dict):
	def __init__(self, **kw):
		#super(Dict, self).__init__(**kw) #method 1
		dict.__init__(self, **kw) #method 2
	
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict'object has no attribute '%s'"%key)
		
	def __setattr__(self, key, value):
		self[key] = value 
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		