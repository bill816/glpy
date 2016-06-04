# -*- coding: utf-8 -*-
import urllib2

print '测试Redirect重定向'
my_url = 'http://xuxian.me'
response = urllib2.urlopen(my_url)
new_url = response.geturl()
redirected = new_url == my_url
if ~redirected:
    print '%s -> %s' % (my_url, new_url)
else:
    print 'No Redirect'

print '测试手动处理重定向'
class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        print '301'
        pass

    def http_error_302(self, req, fp, code, msg, headers):
        print '303'
        pass

try:
    opener = urllib2.build_opener(RedirectHandler)
    opener.open(my_url)
except urllib2.URLError, e:
    # HTTPError
    if hasattr(e, 'code'):
        print 'Error code: ', e.code
    # URLError
    elif hasattr(e, 'reason'):
        print 'Reason: ', e.reason
