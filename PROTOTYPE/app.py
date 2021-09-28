# save this as app.py
from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Feed')

@app.route('/post')
def post():
    return render_template('post.html', title='Post')

@app.route('/chat')
def chat():
    return render_template('chat.html', title='Chat')

@app.route('/login')
def login():
    return render_template('login.html' , title='Login')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')