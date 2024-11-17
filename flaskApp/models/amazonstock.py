import joblib
import pandas as pd
from flask import render_template, request
import json

# Load the trained model for Amazon stock prediction
dtr_model = joblib.load('models/decision_tree_regressor_model.pkl')
lr_model = joblib.load('models/linear_regressor_model.pkl')

def load_sample_cases():
    with open('samples.json') as f:
        return json.load(f)

# Define the route for Amazon Stock Prediction
def amazon_stock():
    sample_cases = load_sample_cases().get("amazon_stock", [])
    return render_template('amazon_stock.html',sample_cases=sample_cases)

# Define the prediction logic for Amazon stock
def predict_amazon_stock():
    sample_cases = load_sample_cases().get("amazon_stock", [])
    open_val = float(request.form['open'])
    close_val = float(request.form['close'])
    low_val = float(request.form['low'])
    high_val = float(request.form['high'])

    # Prepare the data for prediction
    input_data = pd.DataFrame({
        'open': [open_val],
        'close': [close_val],
        'low': [low_val],
        'high': [high_val]
    })
    # print(input_data)
    # Predict using the Decision Tree Regressor model
    dtr_prediction = dtr_model.predict(input_data)
    lr_prediction = lr_model.predict(input_data)

    return render_template('amazon_stock.html',dtr_prediction=dtr_prediction[0] ,lr_prediction=lr_prediction[0],sample_cases=sample_cases)
