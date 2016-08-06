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
HAM_RESULT_PATH = "ham_result.pkl"
SPAM_RESULT_PATH = "SPAM_result.pkl"

#把单词回到map里面去
def add_to_map(map,word):
    try:
       map[word] = map[word] + 1
    except KeyError:
       map[word] = 1
    try:
       map['total_of_word'] = map['total_of_word'] + 1
    except KeyError:
      map['total_of_word'] = 1

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
        for line in open(mail_file):  
            f = open(mail_file,'r')
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
#def start_test():
    

if __name__ == '__main__':
    #read_from_file(HAM_PATH,__mail_ham_map)
    #print __mail_ham_map
    #save_train_to_file("result.pkl",__mail_ham_map)
    #obj = read_train_from_file("result.pkl")
    #print obj['spoke']
    start_train()
    

