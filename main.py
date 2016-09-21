#!/usr/bin/python
#-*-coding:utf-8-*-

from flask import Flask, g, request
from weixin.micros import WeixinAPI
from transaction.robot import RobotAPI
from jinja2 import Environment, FileSystemLoader
import logging
import os
import commands

app = Flask(__name__)

TOKEN = 'wexin123'

@app.route('/')
def hello():
    msg = request.args.get('name', 'bob')
    return "Hello, %s! - Flask" % msg

@app.route('/status')
def check_status():
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(THIS_DIR))
    template = env.get_template('weixin/template/status.tpl')
    items = []
    
    result= commands.getstatusoutput('supervisorctl status wxpub')
    print result
    up = True if 'RUNNING' in result[1] else False
    it = {'service': u'公众号服务', 'up': up}
    items.append(it)
    result= commands.getstatusoutput('supervisorctl status wxschtask')
    print result
    up = True if 'RUNNING' in result[1] else False
    it = {'service': u'公众号定时推送', 'up': up}
    items.append(it)
    result= commands.getstatusoutput('supervisorctl status iss')
    print result
    up = True if 'RUNNING' in result[1] else False
    it = {'service': u'虚拟网服务', 'up': up}
    items.append(it)
    return template.render(items=items)

@app.route('/weixin', methods = ['GET', 'POST'])
def wechat():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    echostr = request.args.get('echostr', '')

    wxapi = WeixinAPI(TOKEN)

    if not wxapi.validate(signature, timestamp, nonce):
        logging.error("signature checking failed")
        return "validate fail"
    if echostr:
        # WeiXin authentication required
        return echostr

    msgbody = wxapi.paser(request.data)
    
    bot = RobotAPI()
    res = bot.responder(msgbody)
    return wxapi.reply(res['msgtype'], res['content'], msgbody['from'], msgbody['to'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)
