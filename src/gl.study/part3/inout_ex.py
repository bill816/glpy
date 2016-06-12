#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

#不做转换，x为字符串
x=raw_input("please input your name:")
print type(x)
print "Hello",x

y=input("please calculate 2^100:")
print type(y)
print "2^100 = %d"%(y)

a,b=1,2
print a,b

print "{name} have input {number}".format(name=x,number=y)
print "{0}like{1}".format('I','python')
print '%d,%d'%(a,b)