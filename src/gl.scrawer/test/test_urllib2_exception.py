# -*- coding: utf-8 -*-
import urllib2

bad_url = 'http://www.bad_url.com'

# urllib2.HTTPError is subclass of urllib2.URLError
try:
    response = urllib2.urlopen(bad_url)
except urllib2.URLError, e:

    # HTTPError
    if hasattr(e, 'code'):
        print 'Error code: ', e.code
    # URLError
    elif hasattr(e, 'reason'):
        print 'Reason: ', e.reason
else:
    print 'No exception was raised.'
    print response.getcode()
