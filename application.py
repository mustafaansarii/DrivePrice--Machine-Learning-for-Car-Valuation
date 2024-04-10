from flask import Flask, render_template, request
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
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = car['fuel_type'].unique()

    companies.insert(0, 'Select Company')
    car_models.insert(0, 'Select Model')
    years.insert(0, 'Select Year')
    fuel_types.insert(0, 'Select Fuel Type')
    return render_template('index.html', companies=companies, car_models=car_models, years=years, fuel_types=fuel_types)

def predict(company, car_model, year, fuel_type, driven):
    prediction = pipeline_model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                                     data=np.array([car_model, company, year, driven, fuel_type]).reshape(1, 5)))
    return str(np.round(prediction[0], 2))

# Convert numpy array to list of tuples
company_choices = [(company, company) for company in car['company'].unique()]
car_model_choices = [(model, model) for model in car['name'].unique()]
year_choices = [(str(year), year) for year in car['year'].unique()]
fuel_type_choices = [(fuel_type, fuel_type) for fuel_type in car['fuel_type'].unique()]

iface = gr.Interface(fn=predict, 
                     inputs=[gr.Dropdown(choices=company_choices, label="Company"), 
                             gr.Dropdown(choices=car_model_choices, label="Car Model"), 
                             gr.Dropdown(choices=year_choices, label="Year"), 
                             gr.Dropdown(choices=fuel_type_choices, label="Fuel Type"), 
                             "number"], 
                     outputs="text",
                     title="Car Price Prediction",
                     description="Enter the details of the car to predict its price.")

if __name__ == '__main__':
    iface.launch()
