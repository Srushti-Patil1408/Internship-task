from flask import Flask, render_template, request, redirect, flash, session, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
from werkzeug.security import generate_password_hash
import os
from werkzeug.utils import secure_filename
from datetime import datetime
from flask import jsonify


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'drive1'

mysql = MySQL(app)
app.secret_key = 'vck'



@app.route('/')
def home():
    return render_template('homes.html')

@app.route('/task1')
def task1():
    return render_template('sss.html')

@app.route('/task2')
def task2():
    return render_template('landing.html')

@app.route('/task3')
def task3():
    return render_template('calculato.html')

if __name__ == '__main__':
    app.run(debug=True)