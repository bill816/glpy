#-*- coding: UTF-8 -*-

if __name__ == '__main__':
    
    #切片 索引
    s = "use python do something "
    print s[1]
    print s[-1]
    print s[:-1]
    print s[1:]
    print s[0:3]
    print s[1:6:2]  #2为步长
    s[:]

    #常用方法集合
    print s.upper()
    print  s.find('pa')
    print s.replace('python','java')
    print "%s like %s" %('we','python')
    print len(s)
    s1 = s.split(' ')
    print s1
    s2 =', '.join(s1)
    print s2
    print s.upper()
    print s[0:4]*5
    print s.strip()
    
    #转义r' '
    s = 'c:\newpython'
    print s
    s = r'c:\newpython'
    print s
    s = 'c:\\newpython'
    print s
    s = 'let\'s have fun'
    print s

    #Unicode u' ' 用unicode不容易出错
    s = '用python做些事'
    print s
    s = u'用python做些事'
    print s
    

