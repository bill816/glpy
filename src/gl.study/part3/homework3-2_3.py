# coding: utf-8
#copyRight by guoxiao
import codecs
import re
import random
import math

def auto_gene_user_pwd():
     #1 生成用户名密码
    charactor='abcdefghijklmnopqrstuvwxyz0123456789'
    
    len_char = len(charactor)-1
    # generate name 4-10
    num_of_name = random.randint(4,10)
    a=[0]*num_of_name
    for i in range(0,num_of_name):
        a[i]=charactor[random.randint(0,len_char)]
    
    name=''.join(a)
    print name
    
    # generate password 4-10
    num_of_pwd = random.randint(6,15)
    a=[0]*num_of_pwd
    for i in range(0,num_of_pwd):
        a[i]=charactor[random.randint(0,len_char)]
    
    password=''.join(a)
    print password
    #write file
    f=open('a.txt','a')
    f.write(name+','+password+'\n')
    f.close()
    
    #print re.findall(r'(\w+[-\w]*)@([a-zA-Z0-9]+)\.(com|org|edu)',text)
def is_user_not_in_file(username):
    #check the username
    if len(username) < 4:
        print "user less 4 chars"
        return False;
    res = re.match(r'[a-zA-Z]',username)
    if res == None:
        print "user name is inlegal"
        return False
    #read file
    f=open('a.txt','r')
    read_tmp_total=f.readlines()
    print read_tmp_total
    for item in read_tmp_total:
        name_pwd = item.strip().split(',')
        if username == name_pwd[0]:
            print "user name is repeat"
            f.close()
            return False
    f.close()
    return True

def is_pwd_inlegal(pwd):
    if len(pwd) < 6:
        return False
    res = re.match(r'^[-\w]',pwd)
    if res == None:
        print 'pwd is not inlegal'
        return False
    return True

def save_user_pwd(name,pwd):
    #write file
    # md5 process
    import hashlib
    password_md5 = hashlib.md5(name).hexdigest()
    f=open('a.txt','a')
    f.write(name+','+password_md5+'\n')
    f.close()

if __name__ == '__main__':
    
    #auto_gene_user_pwd()
    while True:
       name = raw_input('please input a user name:')
       print name
       if name == 'exit':
           break
       ret = is_user_not_in_file(name)
       if ret:
           pwd = raw_input('please input a pwd:')
           if is_pwd_inlegal(pwd):
               save_user_pwd(name,pwd)
   
   