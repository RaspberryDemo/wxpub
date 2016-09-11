#!/usr/bin/python
#-*-coding:utf-8-*-
from youdao import YouDaoAPI
from bsbdj import BsAPI
from qiubai import QbAPI
from qulishi import QulishiAPI
from baiduting import BaiDuTingAPI
from mjtt import MjttAPI
import os

class RobotAPI():
    def __init__(self):
        pass

    def responder(self, msgbody):
        res = {'msgtype': '', 'content': ''}
        try:
            if msgbody['msgtype'] == 'text':
                res['msgtype'], res['content'] = RobotService.translator(msgbody['content'])
            if msgbody['msgtype'] == 'event':
                if msgbody['event'] == 'subscribe':
                    res['msgtype'], res['content'] = RobotService.welcome()
                elif msgbody['eventkey'] == 'MY_JOKE':
                    #res['msgtype'], res['content'] = RobotService.bsjoke()
                    res['msgtype'], res['content'] = RobotService.qbjoke()
                elif msgbody['eventkey'] == 'MY_HISTORY':
                    res['msgtype'], res['content'] = RobotService.qulishi()
                elif msgbody['eventkey'] == 'MY_MUSIC':
                    res['msgtype'], res['content'] = RobotService.ting()
                elif msgbody['eventkey'] == 'MY_MEIJU':
                    res['msgtype'], res['content'] = RobotService.meiju()
        except:
            res['msgtype'], res['content'] = 'text', u'系统繁忙，请稍后重试'
            if os.getenv('APP_DEBUG') == 'True':
                raise
        return res

class RobotService():
    def __init__(self):
        pass

    # print welcome message
    @classmethod
    def welcome(cls):
        return 'text', u'欢迎关注!'

    # translator from youdao API
    @classmethod
    def translator(cls, word):
        youdao = YouDaoAPI()
        return youdao.translator(word)

    # get joke from budejie
    @classmethod
    def bsjoke(cls):
        bs = BsAPI()
        return bs.get()

    # get QiuBai
    @classmethod
    def qbjoke(cls):
        qb = QbAPI()
        return qb.get()

    # get history from qulishi
    @classmethod
    def qulishi(cls):
        qulishi = QulishiAPI()
        return qulishi.get()

    # get music from baidu ting
    @classmethod
    def ting(cls):
        bdapi = BaiDuTingAPI()
        return bdapi.get()

    # get meiju intro from meijutt
    @classmethod
    def meiju(cls):
        mjapi = MjttAPI()
        return mjapi.get()
