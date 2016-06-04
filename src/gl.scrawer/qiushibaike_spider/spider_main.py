# -*- coding: utf-8 -*-
import url_manager, html_downloader, html_parser, html_outputer,os

count_max = 200
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                #print 'craw  %s' % new_url

                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)

                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if self.outputer.count_article() >= count_max:
                    self.outputer.output_article(count_max)
                    break
            except:
                print 'craw failed'
        self.outputer.output_html()

if __name__ == '__main__':
    root_url = 'http://www.qiushibaike.com'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    raw_input()
    