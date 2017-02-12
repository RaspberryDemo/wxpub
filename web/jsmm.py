#!/usr/bin/python
#-*-coding:utf-8-*-

from flask import Blueprint,request,url_for,render_template, make_response, jsonify
from pymongo import *
import datetime
import random
import time
import math
from PIL import Image

jsmm = Blueprint('jsmm', __name__,
                        template_folder='templates')
size = 15
basepath = '/home/pi/www/wxpub/static/'

@jsmm.route('/jsmm.json')
def get_mm_images_json():
    client = MongoClient("localhost", 27017)
    db = client.mmdb
    mmc = db.mmc
    
    total = mmc.count()
    skip = random.randint(0, total-size-1)
    images = mmc.find(sort=[('_id', DESCENDING)], skip=skip, limit=size)
    imgs = list(images)
    #covers = [random.sample(img['alias'], 1)[0] for img in imgs]
    print imgs
    for i in imgs:
        del i['_id']
    return jsonify(data=imgs)

@jsmm.route('/jsmm2.json')
def get_mm_images_json2():
    client = MongoClient("localhost", 27017)
    db = client.mmdb
    mmc = db.mmc
    
    total = mmc.count()
    skip = random.randint(0, total-size-1)
    images = mmc.find(sort=[('_id', DESCENDING)], skip=skip, limit=size)
    imgs = list(images)
    print imgs
    for i in imgs:
        del i['_id']
    for img in imgs:
        newimgs = []
        for a in img['alias']:
            try:
                sz = Image.open(basepath+a).size
                iminfo = {'name': a, 'width': sz[0], 'height': sz[1]}
                newimgs.append(iminfo)
            except:
                print 'open image %s failed' % a
        img['alias'] = newimgs
    for img in imgs:
        print img['alias']
    return jsonify(data=imgs)

@jsmm.route('/jsmm')
def get_mm_images():
    p = request.args.get('p')
    p = int(p) if p else 1
    
    client = MongoClient("localhost", 27017)
    db = client.mmdb
    mmc = db.mmc

    total = mmc.count()
    total = int(math.ceil(total/(size+0.0)))
    images = mmc.find(sort=[('_id', DESCENDING)], skip=(p-1)*size, limit=size)
    imgs = list(images)
    covers = [random.sample(img['alias'], 1)[0] for img in imgs]
    dts = [time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(img['record'])) for img in imgs]
    sources = [img['source'] for img in imgs]
    pre = p-1
    nxt = 0 if p==total else p+1
    resp =make_response(render_template('jsmm.tpl', images=imgs, covers=covers,
        dts=dts, sources=sources, page=p, pre=pre, nxt=nxt, total=total))
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
    aliaslist = images[0]['alias']
    alt = images[0]['alt']
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(images[0]['record']))
    source = images[0]['source'] if 'source' in images[0].keys() else '99mm'

    resp = make_response(render_template('mmlist.tpl', aliaslist=aliaslist, dt=dt, alt=alt, source=source))
    resp.headers['Cache-Control'] = 'no-cache'
    return resp

