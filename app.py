from flask import Flask, render_template, url_for, redirect, jsonify, request
from pycaret.regression import *
import pandas as pd
import pickle
import numpy as np

# name of flask app
app = Flask(__name__)

# create model object
model = load_model('deployment_model')
pedictor_col = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']


# run the server
# this line of code is not needed when running the flask run command in terminal
# app.run(debug= True)


# defining static app routes
@app.route("/")  # decorator
def home():  # route handler function
    # returning a response
    return render_template('index.html')


# create prediction function
@app.route("/predict", methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns=pedictor_col)
    prediction = predict_model(model, data=data_unseen, round=0)
    prediction = int(prediction.Label[0])
    return render_template('index.html', pred='Expected insurance bill will be around ${}'.format(prediction))
