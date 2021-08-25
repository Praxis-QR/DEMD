# https://pythonspot.com/flask-web-app-with-python/

from sys import argv
from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)
scriptName = argv[0]

@app.route("/")
def hello():
    retString = 'WebApp 03 now running ... '+scriptName
    return retString

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/datatext/<inputText>')
def say_hello(inputText):
    return render_template('work01.html',text_data=inputText)

@app.route('/datanumber/<int:inputInt>')
def data_input(inputInt):
    newVar = 2 * inputInt
    return render_template('work02.html',int_data=newVar)


if __name__ == "__main__":
    app.run(host="0.0.0.0")