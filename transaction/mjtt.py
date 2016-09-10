#!/usr/bin/python
# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser
import requests

MJTT_URL = 'http://www.meijutt.com/'

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.img_flag = 0
        self.find_desc = 0
        self.titles = []
        self.images = []
        self.intros = []
        self.dlinks = []
 
    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "a":
            if len(attrs) == 0: pass
            else:
                for (variable, value) in attrs:
                    if variable == "class" and value == "channel-silder-img":
                        self.img_flag = 1
                        self.dlinks.append(MJTT_URL+attrs[1][1])
        elif tag == "img":
            if self.img_flag:
                for (variable, value) in attrs:
                    if variable == "src":
                        self.images.append(value)
                    elif variable == "title":
                        self.titles.append(value)
                self.img_flag = 0
        elif tag == "p":
            if len(attrs) == 0: pass
            else:
                for (variable, value) in attrs:
                    if variable == "class" and value == "channel-silder-desc":
                        self.find_desc = 1

    def handle_data (self, data):
        if self.find_desc == 1:
            self.intros.append(data)
            self.find_desc = 0

class MjttAPI():
    def __init__(self):
        pass

    def get(self):
        while True:
            try:
                content = requests.get(MJTT_URL).content
                data = content.decode("gb2312", "ignore")
                data = data.replace('<span>', '')
                data = data.replace('</span>', '')
                break
            except:
                pass

        hp = MyHTMLParser()
        hp.feed(data)
        hp.close()

        items = []
        for i in range(len(hp.images)):
            it = {}
            it['title'] = hp.titles[i]+' - ' + hp.intros[i][:50] + '...'
            it['picurl'] = hp.images[i]
            it['url'] = hp.dlinks[i]
            it['description'] = hp.intros[i]
            items.append(it)
        return 'news', items


if __name__ == "__main__":
    mjapi = MjttAPI()
    print mjapi.get()