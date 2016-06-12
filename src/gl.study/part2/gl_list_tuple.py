#-*- coding: UTF-8 -*-
import datetime
import time

if __name__ == '__main__':
    
   a=[1,2,3,4,5]
   print a[0]
   print a[-1]
   print a[0:4]
   b = a[:] #拷贝
   c = a    #引用
   a[1] = 10
   print a
   print b
   print c
   d = [a,b,c]
   print d
   a.append(300)
   print "after apppend:" + str(a)
   a.insert(1,50)
   print "after insert:" + str(a)
   a.pop()
   print "after pop:" + str(a)
   a.sort()
   print "after sort:" + str(a)
   a.reverse()
   print "after reverse:" + str(a)
   del a[0]
   print "after del:" + str(a)
   print b
   print c
   
   print d
    
   print id(a)
   print id(b)
   print id(c)
   print a+[10,11]
   print a.count(10)
   
#元组不能原处修改
   t=tuple(a)
   print t[0]
   #t[0] = 11  #TypeError: 'tuple' object does not support item assignment
   print t+(1,2)
   print t*2
   help(t)
    
    
    
    