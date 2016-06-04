import tushare as ts
from pymongo import MongoClient
import json

if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    df = ts.get_hist_data('000001')
    print type(df)
    db = client.get_database('STOCK_TICK')
    print type(db)
    db.tickdata.insert(json.loads(df.to_json(orient='records')))
    print 'hello'
    
