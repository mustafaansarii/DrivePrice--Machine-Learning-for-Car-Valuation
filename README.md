
# Car Price Prediction Model 
## Introduction
[live on render](https://driveprice-machine-learning-for-car.onrender.com/)
[live Car Price Prediction Model here](https://huggingface.co/spaces/Mustafaansari/CAR-PRICE-PREDICTION)


## Machine Learning Model

### Overview

The machine learning model used for car price prediction is trained on historical data containing information about various car features and their corresponding prices. The model employs a regression algorithm to learn the relationship between the input features and the target variable (car prices).

### Features

The model takes the following features as input:

- **Year**: The manufacturing year of the car.
- **Present_Price**: The current price of the car.
- **Kms_Driven**: The distance traveled by the car in kilometers.
- **Number of Previous Owners**: The number of previous owners of the car.
- **Fuel_Type**: The type of fuel used by the car (Petrol, Diesel, CNG).
- **Seller_Type**: The type of seller (Individual or Dealer).
- **Transmission_Type**: The type of transmission (Manual or Automatic).

### Training

The model is trained using a dataset containing a large number of car instances, each with associated features and prices. During training, the model learns to minimize the difference between its predicted prices and the actual prices in the training data.

### Evaluation

The performance of the model is evaluated using various metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared (R2) score. These metrics provide insights into how well the model generalizes to unseen data.

## User Interface (UI)

### Overview

The UI provides a user-friendly interface for users to input car features and obtain predictions for car prices. It is designed to be intuitive and accessible, allowing users to interact with the model effortlessly.

### Features

The UI includes the following features:

- Input fields for users to enter car features (Year, Present_Price, Kms_Driven, Number of Previous Owners).
- Dropdown menus for selecting categorical features (Fuel_Type, Seller_Type, Transmission_Type).
- A button to trigger the prediction process.
- A display area to show the predicted car price.

### Usage

To use the UI, users can follow these steps:

1. Enter the values for the car features into the corresponding input fields.
2. Select the appropriate options from the dropdown menus for categorical features.
3. Click the "Predict" button to obtain the predicted car price.
4. The predicted price will be displayed in the designated area below the input fields.

## Conclusion

The car price prediction model and its accompanying UI provide a convenient tool for users to estimate the price of a car based on its features. By leveraging machine learning techniques and user-friendly design, the system offers valuable insights for car buyers and sellers alike.

