# -*- coding: utf-8 -*-
# using Requests
import requests

username = 'xxx'
password = 'xxx'

def spider_main(login_url, base_url):
    try:
        s = requests.Session()
        r = s.get(login_url)
        cookie_str = r.cookies['csrftoken']
        print cookie_str

        # login
        login_info = {
            'csrfmiddlewaretoken': cookie_str,
            'username': username,
            'password': password
        }
        r = s.post(login_url, data=login_info)

        #  try password
        csrftoken_str = s.cookies['csrftoken']
        for i in range(30):
            print i, csrftoken_str
            postdata = {
                'csrfmiddlewaretoken': csrftoken_str,
                'username': 'mrknight',
                'password': i
            }

            r = s.post(base_url, data=postdata)
            #print r.cookies # post, cookie = none
            #print r.text.encode('utf-8')

            if u'错误' in r.text: # r.text <type 'unicode'>
                print i, '密码错误'
                continue
            else:
                print i, '密码确认'
                break

    except requests.exceptions.RequestException, e:
        print e


if __name__ == '__main__':
    login_url = 'http://www.heibanke.com/accounts/login/'
    base_url = 'http://www.heibanke.com/lesson/crawler_ex02/'
    spider_main(login_url, base_url)
