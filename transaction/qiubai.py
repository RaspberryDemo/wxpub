#!/usr/bin/python
#-*-coding:utf-8-*-
from HTMLParser import HTMLParser
import random
import requests
from bs4 import BeautifulSoup

base_url = "http://www.qiushibaike.com/text/page/%d"
class QbAPI():
    def __init__(self):
        pass

    def get(self, cnt=5):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
        page = random.randint(1,30)
        r = requests.get(base_url % page, headers=headers)
        
        r.encoding = 'utf-8'
        html = r.text
        html = html.replace('<span>', '').replace('</span>', '').replace('<br/>', '') 
        soup = BeautifulSoup(html, 'html.parser')
        data = ''
        jokes = []
        for link in soup.find_all("div", class_="content"):
            if link.string:
                txt = link.string.strip('\n').strip('\r\n')
                jokes.append(txt)
        sa = random.sample(jokes, cnt)
        idx = 1
        for item in sa:
            data = data + '[%d]' % idx + item + '\n\n'
            idx = idx + 1
        return 'text', data+'Page-%s' % page

if __name__ == '__main__':
    qb = QbAPI()
    qb.get()
