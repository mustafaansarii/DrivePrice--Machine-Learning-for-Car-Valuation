from flask import Flask, render_template, request, redirect
from flask_cors import CORS, cross_origin
import pandas as pd
import numpy as np
import modelbit

app = Flask(__name__)
cors = CORS(app)

def get_prediction(name, company, year, kms_driven, fuel_type):
    result = modelbit.get_inference(
        region="ap-south-1",
        workspace="mustafaansari",
        deployment="predict_car_price",
        data=[name, company, year, kms_driven, fuel_type]
    )
    prediction = result['data']
    rounded_prediction = round(float(prediction), 2)
    return str(rounded_prediction)

car = pd.read_csv('Cleaned_Car_data.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()

    companies.insert(0, 'Select Company')
    return render_template('index.html', companies=companies, car_models=car_models, years=year, fuel_types=fuel_type)

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_models')
    year = request.form.get('year')
    fuel_type = request.form.get('fuel_type')
    driven = float(request.form.get('kilo_driven'))  # Convert to float

    prediction = get_prediction(car_model, company, year, driven, fuel_type)
    # Return the prediction as a response
    return prediction

if __name__ == '__main__':
    app.run()
