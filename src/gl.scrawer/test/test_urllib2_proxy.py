# -*- coding: utf-8 -*-
import urllib2
import socks, socket

print u'测试Proxy代理设置'
enable_proxy = True
proxy_hander = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_hander = urllib2.ProxyHandler({})

if enable_proxy:
    opener = urllib2.build_opener(proxy_hander)
else:
    opener = urllib2.build_opener(null_proxy_hander)

#urllib2.install_opener(opener)


# 不使用SOCKS5代理无法访问
# 需要在使用urllib2之前完成socks设置
url = 'http://www.google.com.hk'
print u'测试socks代理'

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 1080)
socket.socket = socks.socksocket
response = urllib2.urlopen(url)
print response.getcode()
