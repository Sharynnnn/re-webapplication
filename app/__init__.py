# import pymysql
import os
from flask import Flask, url_for, request, redirect, render_template
from config import DefaultConfig
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
 # define system file 
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# define static file
static_dir = os.path.join(BASE_DIR, 'static')
# define templates file
templates_dir = os.path.join(BASE_DIR, 'templates')

app = Flask(__name__,
            static_url_path="/static",  
            static_folder=static_dir,     
            template_folder=templates_dir     
            )
app.config.from_object(DefaultConfig)
# db = pymysql.connect(host=app.config.get("HOST"), user=app.config.get("USERNAME"), password=app.config.get("PASSWORD"),
#                      db=app.config.get("DATABASE"), charset=app.config.get("CHARSET"),port=app.config.get("PORT"))
db = SQLAlchemy(app)

# from app import models,views

