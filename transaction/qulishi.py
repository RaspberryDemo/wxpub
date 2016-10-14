#!/usr/bin/python
# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser
import random
import requests

QULISHI_URL = 'http://m.qulishi.com/yeshi/index_%d.htm'
QULISHI_URL_BASE = 'http://m.qulishi.com'

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.art_links = []
        self.img_links = []
        self.alt = []

    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "a":
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == "href" and 'news' in value:
                        self.art_links.append(value)
        elif tag == "img":
            if len(attrs) == 0: pass
            else:
                for (variable, value) in attrs:
                    if variable == "src":
                        self.img_links.append(value)
                    elif variable == "alt":
                        self.alt.append(value)

class QulishiAPI():
    def __init__(self):
        pass

    def getJson(self, cnt=5):
        while True:
            try:
                page = random.randint(1, 200)
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/    537.36'}
                content = requests.get(QULISHI_URL % page, headers=headers).content
                print content
                data = content.decode("utf8", "ignore")
                break
            except:
                pass

        hp = MyHTMLParser()
        hp.feed(data)
        hp.close()

        selected = random.sample(range(0, 20), cnt)

        items = []
        for i in selected:
            it = {}
            it['title'] = hp.alt[i]
            it['picurl'] = QULISHI_URL_BASE+hp.img_links[i]
            it['url'] = hp.art_links[i]
            it['description'] = ''
            items.append(it)
        return items

    def get(self):
        items = self.getJson()
        return 'news', items

if __name__ == "__main__":
    qapi = QulishiAPI()
    print qapi.get()
