#!/usr/bin/python
#-*-coding:utf-8-*-
import urllib2
import json
import requests

YOUDAO_URL = r'http://fanyi.youdao.com/openapi.do?keyfrom=fuzzingman&key=1996695737&type=data&doctype=json&version=1.1&q='

class YouDaoAPI():
    def __init__(self):
        pass

    def translator(self, word):
        if type(word).__name__ == "unicode":
            word = word.encode('UTF-8')
        qword = urllib2.quote(word)

        url = YOUDAO_URL + qword
        r = requests.get(url)
        resp = json.loads(r.text)

        if resp['errorCode'] == 0:
            if 'basic' in resp.keys():
                trans = u"%(query)s:\n%(translation)s\n\n%(explains)s\n" \
                    % {'query':resp['query'], 'translation':''.join(resp['translation']), \
                    'explains':' '.join(resp['basic']['explains'])}
            else:
                trans = u'%s:\n基本翻译:%s\n'%(resp['query'],''.join(resp['translation']))
        elif resp['errorCode'] == 20:
            trans = u'对不起，要翻译的文本过长'
        elif resp['errorCode'] == 30:
            trans = u'对不起，无法进行有效的翻译'
        elif resp['errorCode'] == 40:
            trans = u'对不起，不支持的语言类型'
        else:
            trans = u'对不起，您输入的单词%s无法翻译,请检查拼写'% word
        return 'text', trans