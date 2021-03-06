# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

# 创建项目对象
app = Flask(__name__)


# 加载配置文件
app.config.from_object('faceService.config')     #模块下的config文件名，不用加py后缀
app.config.from_envvar('FLASK_SETTINGS')   #环境变量，指向配置文件setting的路径
# ubuntu: export FLASK_SETTINGS=config.py

NUMBER_OF_FEATURE = 0
tolerance = 0
with open('faceService/parameters.json', 'r') as parameters:
    parameters_dic = json.load(parameters)

'''parameters variable'''
NUMBER_OF_FEATURE = 128 #特征维度个数，是个常数，由算法决定
NUMBER_OF_PERSON_PER_PAGE = 12
tolerance = 1 - float(parameters_dic['sim_threshold'])
login_image_root = parameters_dic['login_image_root']
check_image_root = parameters_dic['check_image_root']
save_img_option = parameters_dic['save_img_option'] # 0表示不存，1表示存，2表示暂时放入存出队列，后面再存入磁盘

#创建数据库对象
db = SQLAlchemy(app)

from faceService.model import Face, Log

from faceService.controller import faceService
