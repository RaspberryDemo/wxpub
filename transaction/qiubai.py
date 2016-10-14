#!/usr/bin/python
#-*-coding:utf-8-*-
import random
from soup import SoupX

base_url = "http://www.qiushibaike.com/text/page/%d"
class QbAPI():
    def __init__(self):
        pass

    def getJson(self, cnt=5, reqp=False):
        page = random.randint(1,30)
        url = base_url % page

        soup = SoupX(url, 'utf-8').get()
        data = ''
        jokes = []
        for link in soup.find_all("div", class_="content"):
            if link.string:
                txt = link.string.strip('\n').strip('\r\n')
                jokes.append(txt)
        sa = random.sample(jokes, cnt)
        if reqp:
            return sa, page
        return sa

    def get(self, cnt=5):
        sa, page = self.getJson(cnt=cnt, reqp=True)
        idx = 1
        data=''
        for item in sa:
            data = data + '[%d]' % idx + item + '\n\n'
            idx = idx + 1
        return 'text', data+'Page %s' % page

if __name__ == '__main__':
    qb = QbAPI()
    qb.get()
