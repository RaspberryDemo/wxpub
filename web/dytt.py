#!/usr/bin/python
#-*-coding:utf-8-*-

from flask import Blueprint, render_template, jsonify
from pymongo import *

dytt = Blueprint('dytt', __name__,
                        template_folder='templates')

@dytt.route('/api/dytt.json')
def get_latest_movies():
    client = MongoClient("localhost", 27017)
    db = client.dydb
    cols = db.cols
    movies = cols.find(sort=[('timestamp', DESCENDING)], limit=15)
    movies = list(movies)
    for m in movies:
        del m['_id']
        del m['timestamp']
    print movies
    return jsonify(data=movies)

