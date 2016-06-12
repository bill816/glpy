#-*- coding: UTF-8 -*-

if __name__ == '__main__':
    
    #open read readline write close
    #path = 'file.txt'
    #f = open(path,'r') #r w a

    #中文支持
    import codecs
    fc = codecs.open("file_ch.txt", 'w', 'utf-8')
    fc.write(u'用python做此事事')
    fc.write(u'黑板客')
    fc.close()
    
    fc = codecs.open("file_ch.txt", 'r', 'utf-8')
    print fc.read(1)
    print fc.read(1)
    print fc.readline()
    fc.close()
    
    import os
#    print os.path.exists('file_ch.txt')
#    os.rename('file_ch.txt', "file_test.txt")
#    print os.path.exists('file_ch.txt')
    
    import shelve
    fs = shelve.open('file_test.shelve')
    fs['baidu'] = 'www.baidu.com'
    fs['qq'] = 'www.qq.com'
    fs['163'] = 'www.163.com'
    print fs
    fs.close()
    g = shelve.open('file_test.shelve')
    print g
    
    import cPickle
    fp=open('file_test.pkl','w')
    obj1 = 2015,'hello',[1,2],{'py':19}
    obj2 = ['he','ju']
    cPickle.dump(obj1, fp)
    cPickle.dump(obj2, fp)
    fp.close()
    
    fp=open('file_test.pkl','r')
    obj1_r = cPickle.load(fp)
    print obj1_r
    obj2_r = cPickle.load(fp)
    print obj2_r
    
    
    
    