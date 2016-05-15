#-*-coding:utf-8-*-
__author__ = 'rrming'

from flask import Flask,Blueprint,request,make_response,redirect,url_for,abort,render_template,session,redirect,url_for
from flask.ext.script import Manager
# from flask.ext.moment import Moment
from application import app
from flask_login import current_user
from models.post import Post
from models.user import User
from datetime import datetime

from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required
from flask.ext.wtf import Form

indexBp = Blueprint('indexBp',__name__)

class contentForm(Form):
    commandInConfig = StringField(u'内置命令')
    commandInWrite = TextAreaField(u'写入Python代码', default=u"写入Python代码")
    userName = StringField(u'用户名', validators=[Required()])
    password = StringField(u'密码', validators=[Required()])
    sendCommand = SubmitField(u'发送命令' )
    clearCommand = SubmitField(u'清空命令')

@indexBp.route('/login', methods=['GET'])
def index():
    form = contentForm()
    return render_template('login.html', form=form)

@indexBp.route('/register', methods=['GET'])
def register():
    form = contentForm()
    return render_template('register.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500