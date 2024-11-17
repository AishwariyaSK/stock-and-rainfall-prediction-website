import json
from flask import Flask, render_template, request
from models.amazonstock import amazon_stock, predict_amazon_stock
from models.rainfall import rainfall, predict_rainfall


app = Flask(__name__)

# Load sample test cases from JSON file
# def load_sample_cases():
#     with open('samples.json') as f:
#         return json.load(f)

# Home page route
@app.route('/')
def home():
    return render_template('home.html')


app.add_url_rule('/amazon_stock', 'amazon_stock', amazon_stock, methods=['GET', 'POST'])
app.add_url_rule('/predict_amazon_stock', 'predict_amazon_stock', predict_amazon_stock, methods=['POST'])

# Register routes for Rainfall Prediction
app.add_url_rule('/rainfall', 'rainfall', rainfall, methods=['GET', 'POST'])
app.add_url_rule('/predict_rainfall', 'predict_rainfall', predict_rainfall, methods=['POST'])


# # Amazon Stock Prediction route
# @app.route('/amazon_stock')
# def amazon_stock():
#     sample_cases = load_sample_cases().get("amazon_stock", [])
#     return render_template('amazon_stock.html', sample_cases=sample_cases)

# # Rainfall Prediction route
# @app.route('/rainfall')
# def rainfall():
#     sample_cases = load_sample_cases().get("rainfall", [])
#     return render_template('rainfall.html', sample_cases=sample_cases)

if __name__ == "__main__":
    app.run(debug=True)
