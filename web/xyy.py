#!/usr/bin/python
#-*-coding:utf-8-*-

from flask import Blueprint,request,url_for,render_template, make_response, jsonify
from pymongo import *
import datetime
import random

xyy = Blueprint('xyy', __name__,
                        template_folder='templates')

size = 20

@xyy.route('/xyy.json')
def get_xyy_json():
    client = MongoClient("localhost", 27017)
    db = client.xyydb
    cols = db.cols

    findings = cols.find(sort=[('_id', DESCENDING)], limit=size)
    findings = list(findings)
    findings = [{'title': f['title'], 'content': f['content']} for f in findings]
    return jsonify(data=findings)

@xyy.route('/xyy')
def get_xyy_article():
    client = MongoClient("localhost", 27017)
    db = client.xyydb
    cols = db.cols

    findings = cols.find(sort=[('_id', DESCENDING)], limit=size)
    findings = list(findings)
    findings = [{'title': f['title'], 'content': f['content'].replace('\n', '<br/>')} for f in findings]
    resp =make_response(render_template('xyy.tpl', findings=findings))
    resp.headers['Cache-Control'] = 'no-cache'
    return resp

