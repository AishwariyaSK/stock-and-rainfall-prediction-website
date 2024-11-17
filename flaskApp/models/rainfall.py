import joblib
import pandas as pd
from flask import render_template, request
import json


# Load your trained unsupervised models (KMeans and Gaussian Mixture)
km_model = joblib.load('models/kmeans_model.pkl')
gm_model = joblib.load('models/gaussian_mixture_model.pkl')

def load_sample_cases():
    with open('samples.json') as f:
        return json.load(f)

# Define the route for Rainfall Prediction
def rainfall():
    sample_cases = load_sample_cases().get("rainfall", [])
    return render_template('rainfall.html',sample_cases=sample_cases)

# Define the prediction logic for Rainfall using unsupervised models
def predict_rainfall():
    sample_cases = load_sample_cases().get("rainfall", [])
    pressure_val = float(request.form['pressure'])
    maxtemp_val = float(request.form['maxtemp'])
    temp_val = float(request.form['temparature'])
    mintemp_val = float(request.form['mintemp'])
    dewpoint_val = float(request.form['dewpoint'])
    humidity_val = float(request.form['humidity'])
    cloud_val = float(request.form['cloud'])
    windspeed_val = float(request.form['windspeed'])

    # Prepare the data for prediction
    input_data = pd.DataFrame({
        'pressure ': [pressure_val],
        'maxtemp': [maxtemp_val],
        'temparature': [temp_val],
        'mintemp': [mintemp_val],
        'dewpoint': [dewpoint_val],
        'humidity ': [humidity_val],
        'cloud ': [cloud_val],
        'windspeed': [windspeed_val]
    })

    print(input_data)
    # Predict using KMeans and Gaussian Mixture models
    km_prediction = km_model.predict(input_data)
    gm_prediction = gm_model.predict(input_data)

    mapping = {0: 'no', 1: 'yes'}   
    km_prediction = mapping[km_prediction[0]]
    gm_prediction = mapping[gm_prediction[0]]
    

    return render_template('rainfall.html', km_prediction=km_prediction, gm_prediction=gm_prediction,sample_cases=sample_cases)
