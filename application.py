from flask import Flask, request
from flask_cors import CORS
import joblib
import pandas as pd
import numpy as np
import gradio as gr

app = Flask(__name__)
cors = CORS(app)
pipeline_model = joblib.load('pipeline_model.joblib')

car = pd.read_csv('Cleaned_Car_data.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()

    companies.insert(0, 'Select Company')
    return render_template('index.html', companies=companies, car_models=car_models, years=year, fuel_types=fuel_type)

def predict(company, car_model, year, fuel_type, driven):
    prediction = pipeline_model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                                     data=np.array([car_model, company, year, driven, fuel_type]).reshape(1, 5)))
    return str(np.round(prediction[0], 2))

iface = gr.Interface(fn=predict, 
                     inputs=["text", "text", "number", "text", "number"], 
                     outputs="text",
                     title="Car Price Prediction",
                     description="Enter the details of the car to predict its price.")

if __name__ == '__main__':
    iface.launch()
