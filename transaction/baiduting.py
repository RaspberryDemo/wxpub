#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import requests
import json

BASE_URL = 'http://tingapi.ting.baidu.com/v1/restserver/ting?'
RATING_URL = 'method=baidu.ting.billboard.billList&type=2&size=1&offset=%d'
PLAY_URL = 'method=baidu.ting.song.play&songid=%s'

class BaiDuTingAPI():
    def __init__(self):
        pass

    def get(self):
        idx = random.randint(1, 100)
        content = requests.get(BASE_URL+RATING_URL % idx).content
        data = content.decode("utf8", "ignore")

        music = {}
        js = json.loads(data)
        if js['error_code'] != 22000:
            return 'text', u'系统繁忙，请稍后重试'
        song_id = js['song_list'][0]['song_id']
        music['description'] = js['song_list'][0]['language'] + \
                js['song_list'][0]['country'] + \
                js['song_list'][0]['style']

        content = requests.get(BASE_URL+PLAY_URL % song_id).content
        data = content.decode("utf8", "ignore")
        js = json.loads(data)
        if js['error_code'] != 22000:
            return 'text', u'系统繁忙，请稍后重试'
        
        
        music['title'] = js['songinfo']['title'] + ' - ' + js['songinfo']['author']
        music['url'] = js['bitrate']['file_link']
        music['mediaid'] = 'p74M3H5EToLcIKFRUOZKJymD8I7MM8_T51LZA7Z8wTo2p3u4fPPoHwwEYc-rUcPJ'

        return 'music', music

if __name__ == '__main__':
    bdapi = BaiDuTingAPI()
    print bdapi.get()
        