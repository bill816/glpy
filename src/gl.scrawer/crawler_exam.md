# 爬虫闯关

## 1. [爬虫闯关第一关](http://www.heibanke.com/lesson/crawler_ex00/)

第一关任务：数字传送，无尽之门。

实际就是爬取数字，构造新的url。

使用urllib2和BeautifulSoup完成，基本的urlopen操作，提取内容，使用BeautifulSoup加正则表达式提取数字，构造新的url。

关于正则表达式：

``` Python
pattern = re.compile(r'\D*(\d+)\D*')
nums = pattern.match(text)
num_str = ''
if nums:
  num_str = nums.group(1)
  #print num_str
else:
  print 'not match'
```

## 2. [爬虫闯关第二关](http://www.heibanke.com/lesson/crawler_ex01/)

第二关任务：简单密码尝试。

不用添加cookie验证，使用POST方法提交表单内容即可。

### 2.1 使用urllib2

每次使用urllib2创建`request`，使用`add_data`后自动变为POST方法。

注意，每次需要新创建`request = urllib2.Request(base_url)`，否则密码尝试可能失败，如果缩小范围比如`range(14,20)`又会成功，没弄明白机理。

``` Python
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
response = opener.open(request)
```

### 2.2 使用Requests
使用urllib2已经感到繁琐，尝试使用[Requests](http://www.python-requests.org/en/master/)，号称“safe for human consumption”，确实精简好用。

``` Python
for i in range(30):
  postdata = {
    'username': 'mrknight-cn',
    'password': str(i)
  }
  r = requests.post(base_url, data=postdata)
```

## 3. [爬虫闯关第三关](http://www.heibanke.com/lesson/crawler_ex02/)

第三关任务：两层保护，密码尝试。

两层保护涉及到[csrftoken](http://baike.baidu.com/view/1609487.htm)，首先需要登录时设置`csrfmiddlewaretoken`，其次尝试密码时设置`csrfmiddlewaretoken`，两次`csrftoken`不同。

``` Python
# login
s = requests.Session()
r = s.get(login_url)
cookie_str = r.cookies['csrftoken']

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
```

## 4. [爬虫闯关第四关](http://www.heibanke.com/lesson/crawler_ex03/)

第四关任务：两层把关，捞取密码。

两层把关，和第三关一样，使用`cfrftoken`登录，使用`cfrftoken`提交密码，两次`csrftoken`不同。

捞取密码，需要在[密码列表页面](http://www.heibanke.com/lesson/crawler_ex03/pw_list/)耐心捞取。

密码列表页面一共13个页面，每个页面随机显示密码不同位置对应的密码，前12个页面每个页面显示8个位置，最后一个页面显示了4个位置，所以密码长度为100。

注意：

* 密码页面的位置是随机生成，13个页面则可能存在重复密码位置，所以需要重复访问这些页面直到获取得到100位的密码。
* 密码页面载入缓慢，考虑使用多线程，但是该网站限制了访问数目，最多只能2个线程同时访问，其他线程会得到404。所以最后在代码中还是使用的单线程来处理。

代码输出结果：
```
jbFEsgdYkgAQlRC695U739AAgNxhwgFU
OUswR2q1NPnQGhL2hq7rio77lCvsOAz1
iter 1, gwdbook size: 65
iter 2, gwdbook size: 92
iter 3, gwdbook size: 98
iter 4, gwdbook size: 98
iter 5, gwdbook size: 100
start: 1462525532.6, end: 1462526346.19, cost: 813.589999914
{u'60': u'9', u'61': u'3', u'62': u'6', u'63': u'7', u'64': u'0', u'65': u'2', u'66': u'8', u'67': u'3', u'68': u'1', u'69': u'0', u'24': u'4', u'25': u'8', u'26': u'4', u'27': u'3', u'20': u'3', u'21': u'2', u'22': u'6', u'23': u'0', u'28': u'7', u'29': u'1', u'2': u'8', u'4': u'4', u'6': u'1', u'8': u'6', u'99': u'1', u'98': u'9', u'91': u'3', u'90': u'6', u'93': u'6', u'92': u'9', u'95': u'2', u'94': u'4', u'97': u'6', u'96': u'9', u'11': u'9', u'10': u'7', u'13': u'0', u'12': u'9', u'59': u'9', u'58': u'8', u'17': u'8', u'16': u'4', u'55': u'0', u'54': u'7', u'57': u'4', u'56': u'6', u'51': u'2', u'50': u'3', u'53': u'4', u'52': u'6', u'19': u'4', u'18': u'7', u'15': u'9', u'88': u'3', u'89': u'9', u'82': u'3', u'83': u'5', u'80': u'6', u'81': u'1', u'86': u'4', u'87': u'3', u'84': u'7', u'85': u'9', u'48': u'1', u'49': u'6', u'46': u'4', u'47': u'9', u'44': u'3', u'45': u'4', u'42': u'9', u'43': u'6', u'40': u'3', u'41': u'6', u'1': u'4', u'3': u'9', u'5': u'6', u'7': u'3', u'9': u'4', u'77': u'9', u'76': u'1', u'75': u'8', u'74': u'3', u'73': u'3', u'72': u'5', u'71': u'2', u'70': u'5', u'100': u'1', u'79': u'1', u'78': u'0', u'39': u'1', u'38': u'8', u'14': u'3', u'33': u'7', u'32': u'8', u'31': u'4', u'30': u'3', u'37': u'1', u'36': u'6', u'35': u'6', u'34': u'7'}
password:  4894613647990394874326048437134877661813696344916326470648993670283105253381901613579433963964296911
OUswR2q1NPnQGhL2hq7rio77lCvsOAz1
密码确认
```
