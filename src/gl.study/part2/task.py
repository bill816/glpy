#-*- coding: UTF-8 -*-

'''
1 邮箱验证：英文+数字+ - + _@英文+数字.(com,org,edu) 
  chu-tian_1981@hebk2016.com

2 利用随机数产生一个用户名，密码，并利用文件 将用户名密码保存下来

3 将上面文件中的密码读取出来加密后再保存通过md5加密库加密
import hashlib
hashlib.md5(password).hexdigest()
'''
if __name__ == '__main__':
    #1 mail
    mail1 = 'aaa@163.com chu-tian_1981@hebk2016.com tt@sdlfj'
    mail2 = 'chu-tian_1981@hebk2016.org'
    mail3 = 'chu-tian_1981@hebk2016.edu'
    
    #1邮箱验证
    import re
    print re.findall(r'(\w+[-\w]*)@(\w+).(com|org|edu)', mail1)
    
    
    #2 利用随机数产生一个用户名，密码，并利用文件 将用户名密码保存下来
    charactor='abcdefghijklmnopqrstuvwxyz012345678'
    a=charactor=[random.randomint(0,len(charactor)-1)]
    
    