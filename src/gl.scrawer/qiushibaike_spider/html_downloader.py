# -*- coding: utf-8 -*-
import urllib2

# 下载器
class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        try:
            # response = urllib2.urlopen(url)
            request = urllib2.Request(url);
            request.add_header('user-agent', 'Mozilla/5.0')
            response = urllib2.urlopen(request)
        except Exception, e:
            print e
            if hasattr(e, 'code'):
                print 'Error code: ', e.code
            elif hasattr(e, 'reason'):
                print 'Reason: ', e.reason
        else:
            return response.read()

    def download_debug(self, url):
        httpHandler = urllib2.HTTPHandler(debuglevel = 1)
        httpsHanler = urllib2.HTTPSHandler(debuglevel = 1)
        opener = urllib2.build_opener(httpHandler, httpsHanler)
        urllib2.install_opener(opener)

        #response = urllib2.urlopen(url)
        request = urllib2.Request(url);
        request.add_header('user-agent', 'Mozilla/5.0')
        response = urllib2.urlopen(request)


        return response.read()
