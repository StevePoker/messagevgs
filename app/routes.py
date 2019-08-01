from app import app
from flask import render_template, redirect, url_for, request


message = ['']


@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', message=message)


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    message[0] = text
    return redirect(url_for('index'))
