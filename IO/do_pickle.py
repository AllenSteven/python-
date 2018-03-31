#!/usr/bin/env python3
#-*-coding:utf-8-*-

import pickle

f = open('dump.txt','wb')
d = dict(name = 'Bob', age = 20, score = 88)
print(pickle.dumps(d))
f.write(pickle.dumps(d))

pickle.dump(d, f)
f.close()

print("dump over, load start")

f = open('dump.txt', 'rb')
d = pickle.load(f)
print(d)
f.close()