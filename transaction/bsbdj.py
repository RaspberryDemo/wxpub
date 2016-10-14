#!/usr/bin/python
#-*-coding:utf-8-*-
from HTMLParser import HTMLParser
import random
import requests

BS_URL = 'http://www.budejie.com/text/%d'

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = 0
        self.links = []
        self.cnt = 0

    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "div":
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == "class" and value == "j-r-list-c-desc":
                        #self.links.append(value)
                        self.flag = 1

    def handle_data (self, data):
        if self.flag == 1:
            self.cnt += 1
            self.links.append(data)
            self.flag = 0

class BsAPI():
    def __init__(self):
        pass

    def getJson(self, cnt=5):
        if cnt > 10:
            cnt = 10
        page = random.randint(1,100)
        url = BS_URL % page
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
        content = requests.get(url, headers=headers).content
        data = content.decode("utf8", "ignore")
        data = data.replace('<br />', '')
        hp = MyHTMLParser()
        hp.feed(data)
        hp.close()
        data = ''
        ll = range(len(hp.links))
        s = random.sample(ll, cnt)
        return s

    def get(self, cnt=5):
        s = self.getJson(cnt)
        for i in s:
            data = data + '[%d]' % i + hp.links[i] + '\n\n'
        return 'text', data+'Page %s' %page

if __name__ == '__main__':
    bs = BsAPI()
    print bs.get()
