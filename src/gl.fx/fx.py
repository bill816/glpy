import zipfile
import csv
import mysqldb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


'''data format
lTid,cDealable,CurrencyPair,RateDateTime,RateBid,RateAsk
4227591665,D,AUD/USD,2015-08-02 17:00:07.633000000,.731840,.732280
4227591675,D,AUD/USD,2015-08-02 17:00:11.633000000,.731820,.732280
4227591678,D,AUD/USD,2015-08-02 17:00:11.883000000,.731820,.732240
4227591725,D,AUD/USD,2015-08-02 17:00:24.633000000,.731760,.732100
4227591812,D,AUD/USD,2015-08-02 17:00:30.633000000,.731760,.732110
'''
def insertDataFromZip(path):
    a = 0;
    conn = mysqldb.databaseConnect();
    cursor = conn.cursor()
    z = zipfile.ZipFile(path,"r")
    first_file_name = z.namelist()[0]
    content = z.read(first_file_name)
    conArr = content.split('\n')
    for strData in conArr:
        if len(strData) < 10:
    	    continue
        lineArr = strData.split(',')
        if lineArr[0] == 'lTid':
    	    continue
        mysqldb.databaseInsert(cursor,lineArr)
        print lineArr
        a = a+1
        if a > 9000:
            conn.commit()
            a = 0
    conn.commit()
    cursor.close();
    conn.close()

if __name__=="__main__":
    print "hello start!!!!!!!!!!!!!!!"
    #insertDataFromZip("AUD_USD_Week1.zip")
    #insertDataFromZip("AUD_USD_Week2.zip")
    #insertDataFromZip("AUD_USD_Week3.zip")
    #insertDataFromZip("AUD_USD_Week4.zip")
    #insertDataFromZip("AUD_USD_Week5.zip")
    print "bye end!!!!!!!!!!!!!!!!!!!"
     
	#-----------------------pandas----------------------
    s = pd.Series([1,3,5,np.nan,6,8])
    print s
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()
