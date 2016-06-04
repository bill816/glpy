# -*- coding: utf-8 -*-

class HtmlOutputer(object):
    def __init__(self):
        self.datas = {}
        self.article_count = 0

    def count_article(self):
        return self.article_count

    def collect_data(self, new_data):
        if new_data is None:
            return

        for article_id, article in new_data.items():
            if article_id not in self.datas:
                self.datas[article_id] = article
                self.article_count = self.article_count + 1

    def output_article(self, count_max):
        count = 0
        for article in self.datas.values():
            print 'user_name = %s, article_id = %s: ' % (article['user_name'], article['article_id']),
            print article['content']

            count = count + 1
            if count >= count_max:
                break

    def output_html(self):
        print 'total number = %d' % len(self.datas)
        fout = open('output2.html', 'w')

        fout.write('<html>')
        fout.write('<head>')
        fout.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">')
        fout.write('</head>')
        fout.write('<body>')
        fout.write('<table>')

        # ascii -> utf-8
        for data in self.datas.values():
            print 'article_id: %s' % data['article_id']
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['article_id'])
            fout.write('<td>%s</td>' % data['user_name'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['content'].encode('utf-8'))
            fout.write('/<tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()
