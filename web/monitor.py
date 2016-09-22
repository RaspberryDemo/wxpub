#!/usr/bin/python
#-*-coding:utf-8-*-

from flask import Blueprint
from jinja2 import Environment, FileSystemLoader
import os
import commands

monitor = Blueprint('monitor', __name__,
                        template_folder='templates')

@monitor.route('/status')
def check_status():
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(THIS_DIR))
    template = env.get_template('templates/status.tpl')
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
