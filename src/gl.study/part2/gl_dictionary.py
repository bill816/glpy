#-*- coding: UTF-8 -*-

if __name__ == '__main__':
    
   #keys,values  get update del clear 嵌套
   dict1 = {"xm":30,"xh":33,'xg':60,'xl':54}
   print dict1
   print dict1['xm']
#   print help(dict)
   copy_d = dict1.copy()
   ref_d = dict1.clear()
   print copy_d
   print ref_d
   
   b=dict(xx=1,xg=2)
   print b
   print dict1.get("tt",'aa') #如果没有这个索引返回aa
   
   index = 'c++ python shell ruby java c'
   data=[112,113,114,115,116,117]
   index_list = index.split(' ')
   data_dict=dict(zip(index_list,data)) #两个list合成一个元组
   print data_dict
     
   print data_dict.keys()
   print data_dict.values()
   print data_dict.items()
    
   #sort keys and values
   print [(k,copy_d[k]) for k in sorted(copy_d.keys())]
    
    
    