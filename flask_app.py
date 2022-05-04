from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

#creating flask instance
app=Flask(__name__)

#Adding Database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Tables.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Secret Key
app.config['SECRET_KEY']='password'

#Initialize the DB
db=SQLAlchemy(app)


