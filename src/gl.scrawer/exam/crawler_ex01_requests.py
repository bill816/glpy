# -*- coding: utf-8 -*-
# using Requests
import requests

def spider_main(base_url):
    try:
        for i in range(30):
            postdata = {
                'username': 'mrknight-cn',
                'password': str(i)
            }
            r = requests.post(base_url, data=postdata)
            # print r.cookie # post, cookie = none
            # print r.text

            if u'错误' in r.text: # r.text <type 'unicode'>
                print i, '密码错误'
                continue
            else:
                print i, '密码确认'
                break
    except requests.exceptions.RequestException, e:
        print e


if __name__ == '__main__':
    base_url = 'http://www.heibanke.com/lesson/crawler_ex01/'
    spider_main(base_url)
