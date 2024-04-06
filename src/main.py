import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

model = pickle.load(open('file.pkl', 'rb'))

standard_to = StandardScaler()

def predict_car_price(Year, Present_Price, Kms_Driven, Owner, Fuel_Type, Seller_Type, Transmission_Type):
    Fuel_Type_Diesel = 0
    Fuel_Type_Petrol = 0

    if Fuel_Type == 'Petrol':
        Fuel_Type_Petrol = 1
    elif Fuel_Type == 'Diesel':
        Fuel_Type_Diesel = 1

    Year = 2024 - Year

    if Seller_Type == 'Individual':
        Seller_Type_Individual = 1
    else:
        Seller_Type_Individual = 0

    if Transmission_Type == 'Manual':
        Transmission_Manual = 1
    else:
        Transmission_Manual = 0

    prediction = model.predict([[Present_Price, Kms_Driven, Owner, Year, Fuel_Type_Diesel, Fuel_Type_Petrol,
                                  Seller_Type_Individual, Transmission_Manual]])
    output = round(prediction[0], 2)

    if output < 0:
        return 'Sorry! You cannot sell this car'
    else:
        return 'You can sell this car at Rs.{} lakhs'.format(output)

# Example usage:
Year = 2018
Present_Price = 7.5
Kms_Driven = 70000
Owner = 1
Fuel_Type = 'Diesel'
Seller_Type = 'Dealer'
Transmission_Type = 'Manual'

prediction_result = predict_car_price(Year, Present_Price, Kms_Driven, Owner, Fuel_Type, Seller_Type, Transmission_Type)
print(prediction_result)
