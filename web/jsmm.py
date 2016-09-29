#!/usr/bin/python
#-*-coding:utf-8-*-

from flask import Blueprint
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
