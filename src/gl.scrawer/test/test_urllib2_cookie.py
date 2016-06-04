# -*- coding: utf-8 -*-
import urllib2, cookielib

print u'测试Cookie'
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = ' + item.name,
    print 'Value = ' + item.value
