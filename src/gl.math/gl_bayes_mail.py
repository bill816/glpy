# encoding: UTF-8

'''
利用正则对邮件进行分类 
统计单词在垃圾邮件和正常邮件出现次数
将上面的数据存下来备用，相当于P(X=某单词|Y=垃圾邮件)
利用全概率公司计算P(x=某单词)
其中先验概率P(Y=垃圾邮件)可以假定为50%
选一封邮件，分词后，计算P(Y=垃圾邮件|X=某单词)
对上面结果排序，选择前15个相加得到该邮件属于垃圾邮件的概率
'''
import re
import glob
import cPickle

# 垃圾邮件字典
# 其中每个键对应的值是一个列表，列表中保存了该单词的次数
__mail_spam_map = {}

# 正常邮件字典
# 其中每个键对应的值是一个列表，列表中保存了该单词的次数
__mail_ham_map = {}


HAM_PATH = 'D:/workspace/git_project/email/train/ham/*.txt'
SPAM_PATH = 'D:/workspace/git_project/email/train/spam/*.txt'
HAM_TEST_PATH = 'D:/workspace/git_project/email/test/ham/*.txt'
SPAM_TEST_PATH = 'D:/workspace/git_project/email/test/spam/*.txt'


HAM_RESULT_PATH = "ham_result.pkl"
SPAM_RESULT_PATH = "SPAM_result.pkl"
TOTAL_OF_WORD = "total_of_word"

#把单词回到map里面去
def add_to_map(map,word):
    try:
       map[word] = map[word] + 1
    except KeyError:
       map[word] = 1
    try:
       map[TOTAL_OF_WORD] = map[TOTAL_OF_WORD] + 1
    except KeyError:
      map[TOTAL_OF_WORD] = 1

#对一行进行切割保存到map
def split_word(map,str):
    #test_word = 'helo this this this sfsd sfs V.S Lily is test helo is this is test helo is this is test'
    split_word = re.split(r'\W+',str)
    for word in split_word:
        if word == '':
            continue
        add_to_map(map,word)

def read_from_file(path,map):
    #从文件里读取内容保存到map
    for mail_file in glob.glob(path):
        f = open(mail_file,'r')
        for line in open(mail_file):  
            line = f.readline()
            split_word(map,line)  

def save_train_to_file(file_path,obj):
    fp=open(file_path,'w')
    cPickle.dump(obj, fp)
    fp.close()
   
def read_train_from_file(file_path): 
    fp=open(file_path,'r')
    obj1_r = cPickle.load(fp)
    return obj1_r

def start_train():
    #读取ham所有单词并保存成文件
    read_from_file(HAM_PATH,__mail_ham_map)
    save_train_to_file(HAM_RESULT_PATH,__mail_ham_map)
    print __mail_ham_map
    #读取ham所有单词并保存成文件
    read_from_file(SPAM_PATH,__mail_spam_map)
    save_train_to_file(SPAM_RESULT_PATH,__mail_spam_map)
    print __mail_spam_map
    
    
def test_a_file(path):
    test_map={}
    f = open(path,'r')
    for line in open(path):  
        line = f.readline()
        split_word(test_map,line)
    return test_map
        
def start_test(path):
    
    #p(y|x)=p(x|y)*p(y)/p(x)
    #y垃圾邮件 x某个单词
    #p(y|x)：  当y邮件出现了x单词，这个邮件y是垃圾邮件的概率
    #p(x|y): 当y为垃圾邮件时，x单词出现的概率
    #p(y)为50%
    #p(x)=
    
    __mail_spam_map = read_train_from_file(SPAM_RESULT_PATH)
    __mail_ham_map = read_train_from_file(HAM_RESULT_PATH)
    print __mail_spam_map
    print __mail_ham_map
    
    #从文件里读取内容保存到map
    for mail_file in glob.glob(path):
        #print mail_file
        test_map = test_a_file(mail_file)
        #print test_map
        for item in test_map:
            spam_count=0
            ham_count=0
            
            try:
                spam_count = __mail_spam_map[item]
            except KeyError:
                spam_count = 0
            try:
                ham_count = __mail_ham_map[item]
            except KeyError:
                ham_count = 0
                   
            item_count = spam_count + ham_count
            px = 0.0
            if item_count > 0:
                word_count = __mail_spam_map[TOTAL_OF_WORD] + __mail_ham_map[TOTAL_OF_WORD]
                #print item
                #print item_count
                #print word_count
                px =float(float(item_count)/float(word_count))
            print px
        break
        

if __name__ == '__main__':
    #start_train()
    start_test(SPAM_TEST_PATH)

