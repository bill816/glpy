#-*- coding: UTF-8 -*-
from decimal import Decimal as D
import time
from random import uniform

if __name__ == '__main__':
    a = 2**10
    b = 2**100
    c = 2**1000
    print type(a)
    print type(b)
    print type(c)
    
    a = 'i like you'
    print a.count('i')
    print a.__class__
    print a.__doc__
    
    a=[1,2,3]
    print a.count('i')
    print a.__class__
    print a.__doc__
    
        
    print 0.3*3
    
    d = 1/2**1000
    print d
    print type(d)
    
    print 10/3
    print 10.0/3
    
    print time.time()
    print D(1)/D(3**1000) #UDecimal speed slow
    print time.time()
    
    import math
    x=3
    y=2
    print math.pi
    print math.sqrt(80)
    print math.log10(2**1000)
    print math.pow(x,y)
    print math.factorial(x) #阶乘
    
    #help for math package
    #print dir(math)
    #print help(math)
    
    import random
    print random.random()
    print random.choice([1,2,4])#随机选
    print random.randint(1,10)#在1-10之间随机
    
    #random.uniform(x,y) #实数
    #random.gauss(x,y) #以高斯分布形式生成
    
    





