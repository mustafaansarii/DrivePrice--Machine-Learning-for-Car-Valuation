import joblib
import pandas as pd
import numpy as np
import gradio as gr

pipeline_model = joblib.load('pipeline_model.joblib')

car = pd.read_csv('Cleaned_Car_data.csv')

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

iface.launch()
