# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2, urllib, cookielib, time

def spider_main(base_url):
    try:
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

        request = urllib2.Request(base_url)
        request.add_header('user-agent', 'Mozilla/5.0')
        response = opener.open(request)
        cookie_token = ''
        for item in cookie:
            if item.name == 'csrftoken':
                cookie_token = item.value
                break

        for i in range(30):
            # construct data
            postdata = urllib.urlencode({
                #'csrfmiddlewaretoken': cookie_token,
                'username': 'mrknight-cn',
                'password': str(i)
            })

            request = urllib2.Request(base_url)
            request.add_data(postdata)
            print request.data
            #print cookie
            #print request.get_method()
            response = opener.open(request)

            content = response.read() # <type 'str'>
            '''
            soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
            text = soup.find('h3').get_text()
            if u'错误' in text:
                print text
            else:
                print text
                print '密码确认'
                break
            '''
            if '错误' in content:
                print i, '密码错误'
                continue
            else:
                print i, '密码确认'
                break

    except urllib2.URLError, e:
        if hasattr(e, 'code'):
            print 'Error code: ', e.code
        elif hasattr(e, 'reason'):
            print 'Error reason: ', e.reason

if __name__ == '__main__':
    base_url = 'http://www.heibanke.com/lesson/crawler_ex01/'
    spider_main(base_url)
