#!/usr/bin/python
#-*-coding:utf-8-*-

from flask import Blueprint, render_template, jsonify
import sys
sys.path.append('..')
from transaction.qiubai import QbAPI
from transaction.qulishi import QulishiAPI

api = Blueprint('api', __name__,
                        template_folder='templates')

@api.route('/api/qulishi.json')
def get_qulishi():
    lishi = QulishiAPI()
    return jsonify(data=lishi.getJson(10))

@api.route('/api/humor.json')
def get_humor():
    qb = QbAPI()
    return jsonify(data=qb.getJson(10))

