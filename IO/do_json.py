#!/usr/bin/env python3
#-*-coding:utf-8-*-

import json

d = dict(name = 'Bob', age = 20, score = 88)
print(d)
print(json.dumps(d))#把dict转换为字符串

print(json.loads(json.dumps(d)))
json_str = '{"age":20, "score":88, "name":"Bob"}'
print(json_str)
print(json.loads(json_str)) #把字符串转换为dict


class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score
		
	def __str__(self):
		return 'Student object (%s, %s, %s)'%(self.name, self.age, self.score)
	
	__repr__ = __str__
		
		
s = Student('Bob', 20 ,99)

#方法一
print("method first")
#把student对象转换为dict
def student2dict(std):
	return{
		'name':std.name,
		'age':std.age,
		'score':std.score
	}
#利用default参数和student2dict把student实例序列化为json对象	
print(json.dumps(s,default = student2dict))

#把dict转换为student实例
def dict2student(d):
	return Student(d['name'], d['age'], d['score'])
#利用object_hook参数和dict2student把json字符串转换为student实例
json_str = '{"age":20, "name":"Bob", "score":88}'
print(json.loads(json_str, object_hook = dict2student))
		

#方法二
print("method second")
#利用匿名函数lambda和__dict__函数将类实例序列化为json对象。
student_data = json.dumps(s, default = lambda obj:obj.__dict__)
print('Dump Student:', student_data)
#利用lambda函数和Student实例化将json对象反序列化为类对象。
rebuild = json.loads(student_data, object_hook = lambda d:Student(d['name'],d['age'], d['score']))
print(rebuild)

#总结：通常采用方法2，代码简单，可复用性强
		