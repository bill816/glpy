# -*- coding: utf-8 -*-
import urllib2

httpHandler = urllib2.HTTPHandler(debuglevel = 1)
httpsHanler = urllib2.HTTPSHandler(debuglevel = 1)
opener = urllib2.build_opener(httpHandler, httpsHanler)
urllib2.install_opener(opener)
reponse = urllib2.urlopen('http://www.baidu.com')
