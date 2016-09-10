#!/usr/bin/python
#-*-coding:utf-8-*-
import hashlib
from lxml import etree
from jinja2 import Environment, FileSystemLoader
import time
import os

class WeixinAPI():
    def __init__(self, token):
        self.token = token

    def validate(self, signature, timestamp, nonce):
        return True
        list=[self.token, timestamp, nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update, list)
        hashcode=sha1.hexdigest()
        if hashcode == signature:
            return True
        return False

    def paser(self, xml_str):
        body = {'eventkey': ''}
        try:
            xml = etree.fromstring(xml_str)
            body['msgtype'] = xml.find("MsgType").text
            body['from'] = xml.find("FromUserName").text
            body['to'] = xml.find("ToUserName").text

            if body['msgtype'] == 'text':
                body['content'] = xml.find("Content").text
            elif body['msgtype'] == 'event':
                body['event'] = xml.find('Event').text
                body['eventkey'] = xml.find('EventKey').text
        except:
            pass
        return body

    def _get_template(self, type):
        THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        env = Environment(loader=FileSystemLoader(THIS_DIR))
        template = None
        if type == 'text':
            template = env.get_template('template/text.tpl')
        elif type == 'news':
            template = env.get_template('template/news.tpl')
        elif type == 'music':
            template = env.get_template('template/music.tpl')
        return template

    def replytext(self, respdata, toUser, fromUser):
        createtime = int(time.time())
        template = self._get_template('text')
        return template.render(toUser=toUser, fromUser=fromUser,
                createtime=createtime, msg=respdata)

    def replynews(self, items, toUser, fromUser):
        createtime = int(time.time())
        template = self._get_template('news')
        return template.render(toUser=toUser, fromUser=fromUser,
                createtime=createtime, items=items, count=len(items))

    def replymusic(self, music, toUser, fromUser):
        createtime = int(time.time())
        template = self._get_template('music')
        return template.render(toUser=toUser, fromUser=fromUser,
                createtime=createtime, music=music)

    def reply(self, type, respdata, toUser, fromUser):
        if type == 'text':
            return self.replytext(respdata, toUser, fromUser)
        if type == 'news':
            return self.replynews(respdata, toUser, fromUser)
        if type == 'music':
            return self.replymusic(respdata, toUser, fromUser)
        else:
            return self.replytext(u'服务暂未开通', toUser, fromUser)
