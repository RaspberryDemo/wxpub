#!/usr/bin/python
#-*-coding:utf-8-*-

from flask import Blueprint,request,url_for,render_template, make_response
from pymongo import *
import datetime
import random

jsmm = Blueprint('jsmm', __name__,
                        template_folder='templates')

@jsmm.route('/jsmm')
def get_mm_images():
    client = MongoClient("localhost", 27017)
    db = client.mmdb
    mmc = db.mmc

    images = mmc.find(sort=[('_id', DESCENDING)], limit=10)
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    imgs = list(images)
    covers = [random.sample(img['alias'], 1)[0] for img in imgs]
    resp =make_response(render_template('jsmm.tpl', images=imgs, covers=covers, dt=dt))
    resp.headers['Cache-Control'] = 'no-cache'
    return resp

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
    aliaslist = images[0]['alias']
    alt = images[0]['alt']
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    resp = make_response(render_template('mmlist.tpl', mmlist=mmlist, aliaslist=aliaslist, dt=dt, alt=alt))
    resp.headers['Cache-Control'] = 'no-cache'
    return resp

