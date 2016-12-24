#-*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import tushare as ts
from pymongo import MongoClient
import json
import csv
import re 

threadList=[]
dataList1=[]
dataList2=[]

def main():
  # 颜色列表
    colorList = ['b','g','r','c','m','y','k']
  # 共用的横坐标
#    threadList = [1,2,4,8,10]
  # 设置横坐标和纵坐标的名称
    plt.xlabel('threads')
    plt.ylabel('concurrent')
     # 图的标题
    plt.title('concurrent test')
     # 要绘制的线的列表
    lines = []
    # 对应的线的名称
    titles = []
    # 第一根线的纵坐标
#    dataList1 = [2,5,7,15,30]
    # 根据横坐标和纵坐标画第一根线
    line1 = plt.plot(threadList, dataList1)
    # 设置线的颜色宽度等
    plt.setp(line1, color=colorList[0], linewidth=2.0)
    # 线的名称
    titles.append('Linux')
    lines.append(line1)
     # 同理画第二根线
#    dataList2 = [2,4,6,18,35]
    line2 = plt.plot(threadList, dataList2)
    plt.setp(line2, color=colorList[1], linewidth=2.0)
    titles.append('FreeBSD')
    lines.append(line2)
    plt.legend(lines, titles)
    plt.show()
#    plt.savefig('test.png', dpi=120)
    
def show_data(data):
    close_data = data['close']
    plt.autoscale(True, 'both', None)
    #绘制方格
    plt.rc('axes', grid=True)
    plt.rc('grid', color='0.75', linestyle='-', linewidth=0.5)
    plt.plot(data['date'], close_data)
    #设置坐标标签
    plt.xlabel('Date')
    plt.ylabel('Close')
    #将x坐标日期进行倾斜
    plt.setp(plt.gca().get_xticklabels(), rotation=20, horizontalalignment='right')
    plt.show()

if __name__ == '__main__':
        
    #################read EURAUD240 csv file
    csvfile = open('EURAUD240.csv','r')
    reader = csv.reader(csvfile)
    column1 = [row[5] for row in reader]
    csvfile.close()
    
    #################read EURAUD240 csv file
    csvfile = open('GBPUSD240.csv','r')
    reader = csv.reader(csvfile)
    column2 = [row[5] for row in reader]
    csvfile.close()
    
    #####生成时间
    time=[5748]
    x = 5747
    while x:
        time.append(x)
        x=x-1
    
    
    threadList = time
    dataList1 = column1
    dataList2 = column2
    
    print len(time)
    print len(column1)
    print len(column2)
    
    main()
    
#    data={"close":column,"date":time}
#    show_data(data)
    
    ############show data############
    data1=[10,12,13,14]
    data3=[11,12,14,15]
    data2=["20161203","20161204","20161205","20161206"]
    data={"close":data1,"date":data2}
#    show_data(data)
    
