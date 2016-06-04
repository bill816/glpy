# -*- coding: utf-8 -*-
# using Requests
import requests
import threading, time
from bs4 import BeautifulSoup

g_mutex = threading.Condition()
g_pwdbook = {}
username = 'xxx'
password = 'xxx'

class MyThread(threading.Thread):
  def __init__(self, func, args):
    threading.Thread.__init__(self)
    self.args = args
    self.func = func

  def run(self):
    apply(self.func, self.args)

def find_password(url, s):
    global g_mutex
    global g_pwdbook

    r = s.get(url)
    pwd_book = {}
    soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
    tr_nodes = soup.findAll('tr')
    for tr_node in tr_nodes:
        nodes = tr_node.findAll('td', attrs={'data-toggle': 'tooltip'})
        if len(nodes) == 0:
            #print tr_node.get_text()
            pass
        if len(nodes) == 2:
            pos = nodes[0].get_text()
            val = nodes[1].get_text()
            pwd_book[pos] = val

    g_mutex.acquire()
    #print '\t', url
    #print s.cookies
    #print '\t', len(pwd_book), pwd_book
    g_pwdbook.update(pwd_book)
    g_mutex.release()

    return pwd_book

def spider_main(login_url, base_url, pwd_url):
    try:
        s = requests.Session()
        r = s.get(login_url)
        cookie_str = s.cookies['csrftoken']
        print cookie_str

        # login
        login_info = {
            'csrfmiddlewaretoken': cookie_str,
            'username': username,
            'password': password
        }
        r = s.post(login_url, data=login_info)
        print s.cookies['csrftoken']

        # find password
        pwdurl_list = []
        for i in range(1, 14):
            pwdurl_list.append(pwd_url + '?page='+str(i))
        t_start = time.time()

        # single thread
        iter_num = 0
        while len(g_pwdbook) < 100:
            iter_num = iter_num + 1
            for url in pwdurl_list:
                find_password(url, s)
                if len(g_pwdbook) == 100:
                    break
            print 'iter %d, gwdbook size: %d' % (iter_num, len(g_pwdbook))

        '''
        # multi-thread
        threadList = [MyThread(find_password, (url, s,)) for url in pwdurl_list]
        for t in threadList:
            t.setDaemon(True)
            t.start()
        for t in threadList:
            t.join()
        #print 'iter %d, gwdbook size: %d' % (1, len(g_pwdbook))
        '''

        t_end = time.time()
        print 'start: %s, end: %s, cost: %s' % (t_start, t_end, t_end - t_start)
        print g_pwdbook

        # construct password
        pos = 1
        password = ''
        while True:
            if not g_pwdbook.has_key(str(pos)):
                break
            password = password + g_pwdbook[str(pos)]
            pos = pos + 1
        print 'password: ', password

        csrftoken_str = s.cookies['csrftoken']
        print csrftoken_str
        postdata = {
                'csrfmiddlewaretoken': csrftoken_str,
                'username': 'mrknight',
                'password': password
            }

        r = s.post(base_url, data=postdata)
        #print r.cookies # post, cookie = none
        #print r.text.encode('utf-8')

        if u'错误' in r.text:
            print '错误'
        else:
            print '密码确认'

    except requests.exceptions.RequestException, e:
        print e


if __name__ == '__main__':
    login_url = 'http://www.heibanke.com/accounts/login/'
    base_url = 'http://www.heibanke.com/lesson/crawler_ex03/'
    pwd_url = 'http://www.heibanke.com/lesson/crawler_ex03/pw_list/'
    spider_main(login_url, base_url, pwd_url)
