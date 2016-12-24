# -*- coding: utf-8 -*-     
 #mysqldb    
import time, MySQLdb

def databaseConnect():
    conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="123456",db="trading",charset="utf8")
    return conn

def databaseInsert(cursor,dataArray):
    sql = "insert into trading(id,deal_able,currentcy_pair,rate_datetime,rate_bid,rate_ask) values(%s,%s,%s,%s,%s,%s)" 
    param = (dataArray[0],dataArray[1],dataArray[2],dataArray[3][0:23],dataArray[4],dataArray[5][0:7])
    n = cursor.execute(sql,param)

#def trading():
    #in = cursor.execute("select * from trading")    
    #for row in cursor.fetchall():    
    #    for r in row:    
    #        print r
