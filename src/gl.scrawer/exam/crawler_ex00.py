# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2, urlparse, re

def spider_main(base_url):
    try:
        print base_url
        request = urllib2.Request(base_url)
        request.add_header('user-agent', 'Mozilla/5.0')
        response = urllib2.urlopen(request)
    except urllib2.URLError, e:
        if hasattr(e, 'code'):
            print 'Error code: ', e.code
        elif hasattr(e, 'reason'):
            print 'Error reason: ', e.reason
    else:
        content = response.read()
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        text = soup.find('body').find('h3').get_text()

        # extract number
        pattern = re.compile(r'\D*(\d+)\D*')
        nums = pattern.match(text)
        num_str = ''
        if nums:
            num_str = nums.group(1)
            #print num_str
        else:
            print 'not match'

        if len(num_str) == 0:
            print 'this is the last url.'
            print text
            return
        new_url = urlparse.urljoin(base_url, num_str)
        spider_main(new_url)


if __name__ == '__main__':
    base_url = 'http://www.heibanke.com/lesson/crawler_ex00/'
    spider_main(base_url)
