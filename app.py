# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 01:43:55 2021

@author: ankita
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("page1.html")

@app.route('/9months')
def months():
    return render_template("page2.html")

@app.route('/1month')
def months():
    return render_template("page3.html")

@app.route('/100days')
def months():
    return render_template("page4.html")

@app.route('/invite')
def months():
    return render_template("page5.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
