# https://pythonspot.com/flask-web-app-with-python/

from sys import argv
from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)
scriptName = argv[0]

@app.route("/")
def hello():
    retString = 'WebApp02 now running ... '+scriptName
    return retString

@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")