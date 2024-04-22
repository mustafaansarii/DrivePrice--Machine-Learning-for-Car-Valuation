import pandas as pd
import numpy as np
import streamlit as st
import modelbit


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

def main():
    
    st.title("Car Price Prediction")

    st.sidebar.image("src/style.gif", use_column_width=True)
    st.sidebar.image("src/car.jpg", use_column_width=True)
    st.sidebar.title("Developer Contact")
    st.sidebar.info(
        """
        
        **Email:** mustafaansari@mail.com  
    **LinkedIn:** [LinkedIn/mustafaansaari/](https://www.linkedin.com/in/mustafaansaari/)  
    **GitHub:** [github/mustafaansaari/](https://github.com/mustafaansarii)  
        """
    )



    # Main content
    st.write("""
    ## Fill Car Details
    """)

    # Car company selection
    companies = sorted(car['company'].unique())
    company = st.selectbox("Select Company", companies)

    car_models = sorted(car[car['company'] == company]['name'].unique())

    car_model = st.selectbox("Select Car Model", car_models)
    year = sorted(car['year'].unique(), reverse=True)
    year_val = st.slider("Select Year", 1995,2019)
    fuel_type = car['fuel_type'].unique()
    fuel_type_val = st.selectbox("Select Fuel Type", fuel_type)
    driven = st.number_input("Enter Kilometers Driven")

    if st.button("Predict"):
        prediction = get_prediction(car_model, company, year_val, driven, fuel_type_val)
        st.write(f"Predicted Price: ₹{prediction}")

if __name__ == "__main__":
    main()
