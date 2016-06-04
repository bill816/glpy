# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urlparse
import re

# 解析器
class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        # <ul class="pagination">
        # <li>
        # <a href="/8hr/page/35?s=4872269" rel="nofollow">
        links = soup.find('ul', class_=re.compile(r'pagination')).\
            find_all('a', href=re.compile(r'\/8hr/page/\d*'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(seft, page_url, soup):
        articles = {}

        article_nodes = soup.find_all('div', class_='article block untagged mb15')
        for article_node in article_nodes:
            # article_id
            article_id = article_node['id']

            # usename
            user_node = article_node.find('div', class_='author clearfix').\
                find('h2')
            user_name = user_node.get_text()

            # content
            content_node = article_node.find('div', class_='content')
            content = content_node.get_text()

            articles[article_id] = {'article_id': article_id, 'user_name':user_name, \
                'content':content}

        return articles

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data
