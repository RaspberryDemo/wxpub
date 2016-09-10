#!/usr/bin/python
#-*-coding:utf-8-*-

from flask import Flask, g, request
from weixin.micros import WeixinAPI
from transaction.robot import RobotAPI
import logging

app = Flask(__name__)

TOKEN = 'wexin123'

@app.route('/')
def hello():
    msg = request.args.get('name', 'bob')
    return "Hello, %s! - Flask" % msg

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
    app.run(host='0.0.0.0', port=8080, debug=False)
