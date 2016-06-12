#-*- coding: UTF-8 -*-
import datetime
import time

if __name__ == '__main__':
    
    #datetime
    print datetime.date.today()
    print datetime.datetime.now()
    print datetime.timedelta(days=100)
    a=datetime.date.today()
    b=datetime.datetime.now()
    d1 = datetime.timedelta(days=100)
    d2 = datetime.timedelta(hours=100)
    print (a-d1).isoformat()
    print (a-d2).strftime('%m/%d/%Y')
    print b.isoformat()
    print datetime.time(12,11,30)
    
    #time
    print time.time()
    a=input('input 0 or 1:')
    start_time = time.time()
    start_clock = time.clock()
    if a:
        sum_i=0
        for i in range(100000):
            sum_i+=i
    else:
        sum_i=sum(range(100000))
    print sum_i
    end_time = time.time()
    end_clock = time.clock()
    
    print end_time-start_time
    print end_clock-start_clock
    
    
    
    
    
    
    
    