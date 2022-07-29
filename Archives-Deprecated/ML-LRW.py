# https://pythonspot.com/flask-web-app-with-python/
# COLAB where model is trained, tested
# Train : https://colab.research.google.com/drive/1G3VUKVUspcoDnLRobuUfsGTswpCMkU8W
# Predict : https://colab.research.google.com/drive/1gF9DI4NT5tH_9lcbVth-kVEZ9sO7wnhU
# docker build -t calcutta/de-applrw02 .
# docker run --rm --name praxislrw -p 5002:5000 calcutta/de-applrw02
# to read JSON output see https://github.com/Praxis-QR/DEMD/blob/0c035dfad1319fe592e32b9f990ab6c746baa18b/LRWApiCall.ipynb

from sys import argv
from flask import Flask, flash, redirect, render_template, request, session, abort
import json
import pickle
from sklearn import linear_model

app = Flask(__name__)
scriptName = argv[0]

@app.route("/")
def hello():
    retString = 'ML LRW now running ... '+scriptName
    return retString

@app.route('/home')
def home():
    return render_template('LR_home.html')

@app.route('/predict1/<featureString>')
def multidata(featureString):
    str1 = featureString
    feature_list = featureString.split(",")
    feature_array = list(map(lambda x : float(x), feature_list))

    model = pickle.load(open("datafiles/lrw-model.pkl","rb"))

    #our model rates the wine based on the input array
    prediction = model.predict([feature_array]).tolist()

    return render_template('LR_predict1.html',**locals())

@app.route('/lrwapi/<featureString>')
def multidata2(featureString):
    str1 = featureString
    feature_list = featureString.split(",")
    feature_array = list(map(lambda x : float(x), feature_list))

    model = pickle.load(open("datafiles/lrw-model.pkl","rb"))

    #our model rates the wine based on the input array
    prediction = model.predict([feature_array]).tolist()
    outDict = {}
    outDict['Prediction'] = str(prediction[0])
    outJSON = json.dumps(outDict)
    return outJSON


if __name__ == "__main__":
    app.run(host="localhost", port=5010)