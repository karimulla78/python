# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:23:27 2019

@author: ASUS
"""

c=0x10
print(c)
print(oct(10))

print(float(10.5))
print(int(True))
a=10
b=11
print(a is b)
x=[10,20,30,40]
c=bytes(x)
#print(c[-1])
b=bytearray(x)
for i in b:print(i)

r=range(5,10,2)
for j in r:print(j)

s={20,10,200,"abc"}
#print(s[0])
s.add(100)
print(s)
s.remove('abc')
print(s)

s1={11,21,31,41}
fs=frozenset(s1)

for i in fs:print(i)

def a():
  b=10
    
print(a())


k="hello\nworld"
print(k)


t="hello\tworld"
print(t)

r="hello \"world\""
r="hello\rworld"
r="hello\bworld"
print(r)

print(10 and 20)

print(not 10)
print(not 0)
000100000



