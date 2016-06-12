#-*- coding: UTF-8 -*-
import re
if __name__ == '__main__':
    
    #11个元字符\ ^ $ . | ? * + () [] {}
    '''
        特殊 \ .
       可选 | []
        重复 * + ? {}
    6个字符 \d \D \s \S \w \W(\d数字 w字母数字组合 
    4个位置 \b \B \A \Z(^ $)
       分组 ()
       编译选项I L M S U X
    '''
    #re.match
    #re.search
    #re.findall
    #re.split
    #re.sub
    s = 'c## python2 python3 perl lus c++ p javascript java ccc'
    s1 = 'c++ python2 python3 ruby perl c-- lus c-- java ccc'
    print re.match(r'java',s)  #从头开始找（第一个不匹配就不行）
    m=re.search(r'java',s) #从任意位置开始找
    print m
    print m.start()
    print m.end()
    print m.group()
    print re.match(r'c\+\+',s)
    print re.findall(r'python',s)
    print re.split(r' perl ',s)
    print re.sub(r'ruby','lus',s) #替换


    #^ start
    #$ end
    #. except \n 除了回车以外所有字符
    print re.findall(r'^c..',s) #^ 从第一个位置开始匹配
    print re.findall(r'^c..',s1)
    
    #+ 1-inf
    #* 0-inf
    #? 0-1
    #[] or
    #{} repeat
    #[^] not
    print re.findall(r'c+',s)
    print re.findall(r'c\++',s)
    print re.findall(r'cc+',s)
    
    print re.findall(r'c$',s)
    
    print re.findall(r'p+',s)
    #[a-zA-Z]代表所有英文 +代表与前面字符相匹配的，整句代表p开关后面是字母的字符串
    print re.findall(r'p[a-zA-Z]+',s)
    print re.findall(r'p[a-zA-Z]*',s)
    print re.findall(r'p[a-zA-Z]?',s)
    
    #3个字母以上
    print re.findall(r'p[a-zA-Z0-9]{3,}',s)
    #4个字母以上
    print re.findall(r'p[a-zA-Z0-9]{4,}',s)
    
    print re.findall(r'c[a-zA-Z]*',s)
    print re.findall(r'c[^a-zA-Z]*',s)
    print re.findall(r'c[^a-zA-Z]{3,}',s)
    
    print re.findall(r'[pj][a-zA-Z]+',s)
    print re.findall(r'[pj][^a-zA-Z]+',s)
    
    #| 或意思p开头或j开头(19:00)
    print re.findall(r'p|j[a-zA-Z]+',s)  
    
    #大写所有的非
    #\w [a-zA-Z0-9_], \W
    #\d [0-9],  \D
    #\s [\t\n\r\f\v], \S  
    print re.findall(r'p\w+',s)
    print re.findall(r'p[a-zA-Z0-9_]+',s)
    
    # \b word boundary(有没空格空白符）
    # \B not \b
    # \A input start,^
    # \Z input end,$
    print re.findall(r'\bp[^0-9]',s)
    
    #*? 0-inf non-greedy
    #+? 1-inf non-greedy
    print re.findall(r'p[a-z]*',s)
    print re.findall(r'p[a-z]*?',s)
    print re.findall(r'p[a-z]+\b',s)
    print re.findall(r'p[a-z]+?\b',s)
    
    
    #() group
    a=re.search(r'(p[a-z]+)([0-9])','python2')
    print a.group(1),a.group(2)
    
    #编译选项
    
    
    
    
    
    
