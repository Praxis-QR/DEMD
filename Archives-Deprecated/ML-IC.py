# https://pythonspot.com/flask-web-app-with-python/
# https://blog.hyperiondev.com/index.php/2018/02/01/deploy-machine-learning-model-flask-api/
# COLAB for train, test, model build https://colab.research.google.com/drive/1JuTezUiqM0Cj_m-FmmeBzw_88xZlYeK-
# docker build -t calcutta/de-appimc02 .
# docker run --rm --name praxisimc -p 5000:5000 calcutta/de-appimc02

# test images available at https://github.com/elliebirbeck/model-deployment-flask/tree/master/test-imgs


from sys import argv
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for

import pickle
from sklearn import linear_model
#from sklearn.externals import joblib
import joblib
from sklearn.ensemble import *

import numpy as np
import imageio


app = Flask(__name__)
scriptName = argv[0]

@app.route("/")
def hello():
    retString = 'now running ... '+scriptName
    return retString

@app.route('/home')
def home():
    return render_template('IC_index.html')

@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method=='POST':
        file = request.files['image']
        if not file: 
            return render_template('IC_index.html', label="No file")
        #f = 'datafiles/'+str(file.filename)
        #file.save(f)
        
        img = imageio.imread(file)
        img = img[:,:,:3]
        img = img.reshape(1, -1)
        prediction = model.predict(img)
        label = str(np.squeeze(prediction))
        if label=='10': 
            label='0'
        return render_template('IC_index.html', label=label, file=file)

if __name__ == "__main__":
    model = joblib.load('datafiles/imClass-model-18032020.pkl')
    app.run(host="localhost", port=5010)