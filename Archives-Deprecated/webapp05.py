# https://pythonspot.com/flask-web-app-with-python/

from sys import argv
from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)
scriptName = argv[0]

@app.route("/")
def hello():
    retString = 'now running ... '+scriptName
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

@app.route('/multidata/<inputString>')
def multidata(inputString):
    str1 = inputString
    text_list = str1.split(",")
    num_array = list(map(lambda x : float(x), text_list))
    return render_template('work03.html',**locals())

@app.route('/readfile/<readfilename>')
def readfile(readfilename):
    filename = 'datafiles/'+readfilename
    txt = open(filename)
    filecontents = txt.read()
    txt.close()
    return render_template('work04.html',**locals())


if __name__ == "__main__":
    app.run(host="localhost", port=5010)