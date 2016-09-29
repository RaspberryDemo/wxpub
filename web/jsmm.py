#!/usr/bin/python
#-*-coding:utf-8-*-

from flask import Blueprint,request
from jinja2 import Environment, FileSystemLoader
from pymongo import *
import os
import datetime

jsmm = Blueprint('jsmm', __name__,
                        template_folder='templates')

@jsmm.route('/jsmm')
def get_mm_images():
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(THIS_DIR))
    template = env.get_template('templates/jsmm.tpl')
    items = []
    
    client = MongoClient("localhost", 27017)
    db = client.mmdb
    mmc = db.mmc

    images = mmc.find(limit=10)
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return template.render(images=images, dt=dt)

@jsmm.route('/immall')
def get_mm_all_images():
    key = request.args.get('key')

    client = MongoClient("localhost", 27017)
    db = client.mmdb
    mmc = db.mmc

    images = mmc.find({'img':key}, limit=1)
    
    if not images.count():
        return 'not found'
    mmlist = images[0]['images']
    alt = images[0]['alt']
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(THIS_DIR))
    template = env.get_template('templates/mmlist.tpl')
    items = []
    
    return template.render(mmlist=mmlist, dt=dt, alt=alt)

