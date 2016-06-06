import tushare as ts
from pymongo import MongoClient
import json



if __name__ == '__main__':
    
    
    client = MongoClient('localhost', 27017)
    db = client.get_database('STOCK_TICK')
    
    #for item in db["sh"].find():
    #    print item
    #sh_df = ts.get_h_data('sh', start='2009-01-01', end='2011-06-3')
    #print type(sh_df)
    #db.sh.insert(json.loads(sh_df.to_json(orient='records')))
    '''
    sh_df = ts.get_h_data('sh', start='2011-06-04', end='2013-06-3')
    print type(sh_df)
    db.sh.insert(json.loads(sh_df.to_json(orient='records')))
    
    sh_df = ts.get_h_data('sh', start='2013-06-04', end='2015-06-3')
    print type(sh_df)
    db.sh.insert(json.loads(sh_df.to_json(orient='records')))
    '''
    
    sh_df = ts.get_hist_data('600848',ktype='W')
    print sh_df
    for item in json.loads(sh_df.to_json(orient='records')):
        print item
    #db['sh'].drop()
    
    #db.sh.insert(json.loads(sh_df.to_json()))
    sh_df.to_json('d:/600848.json',orient='records')
  #  print sh_df
    print '------------------------------------------'
    print '------------------------------------------'
    print '------------------------------------------'
  #  print sh_df.to_json
    
    print 'hello'
    
