# https://pythonspot.com/flask-web-app-with-python/

from sys import argv
from flask import Flask
app = Flask(__name__)
scriptName = argv[0]

@app.route("/")
def hello():
    retString = 'Praxis Web App 01 now running ... '+scriptName
    return retString
 
if __name__ == "__main__":
    app.run(host="0.0.0.0")