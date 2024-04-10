# Car Price Prediction
[LIve on Render](https://car-price-predictor-k9en.onrender.com/)
## Introduction

The Car Price Prediction Web Application is a Flask-based web application that predicts the price of cars based on various features such as car model, company, manufacturing year, kilometers driven, and fuel type. The prediction model is built using scikit-learn (sklearn), a popular machine learning library in Python. The dataset used for training the model is sourced from Kaggle, a platform for data science competitions and datasets.

## Features

- Predict the price of a car based on input parameters.
- User-friendly interface with dropdown menus for selecting car details.
- Input validation to ensure correct data entry.
- Cross-origin resource sharing (CORS) enabled to allow communication between the client-side and server-side scripts.

## Technologies Used

- **Flask**: Flask is a micro web framework for Python used to develop web applications. It provides tools, libraries, and technologies for building web applications.
- **Flask-CORS**: Flask-CORS is an extension for Flask that adds support for Cross-Origin Resource Sharing (CORS), allowing AJAX requests from a different domain than the one serving the web application.
- **scikit-learn (sklearn)**: Scikit-learn is a machine learning library in Python that provides simple and efficient tools for data mining and data analysis. It features various algorithms for classification, regression, clustering, dimensionality reduction, and more.
- **Pandas**: Pandas is a data manipulation and analysis library for Python. It is used for reading and processing CSV files containing car data sourced from Kaggle.
- **NumPy**: NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions.

## Dataset

The dataset used for training the car price prediction model is sourced from Kaggle. The dataset contains information about various cars, including their make, model, year of manufacture, kilometers driven, fuel type, and price. The dataset is preprocessed and cleaned to handle missing values, categorical variables, and other data inconsistencies.

## Model Building

The car price prediction model is built using scikit-learn (sklearn). The dataset is split into training and testing sets for model evaluation. Several regression algorithms provided by sklearn, such as Linear Regression, Random Forest Regression, and Gradient Boosting Regression, are considered and evaluated for their performance in predicting car prices.

After evaluating different algorithms, the Random Forest Regression algorithm is selected as the final model due to its superior performance in terms of accuracy and robustness.

## Deployment

The Car Price Prediction Web Application is deployed on a cloud platform such as Heroku or AWS using Flask. The deployment process involves configuring the environment, setting up dependencies, and deploying the Flask application. The deployed application is accessible over the internet, allowing users to input car details and obtain predicted prices.

## Conclusion

The Car Price Prediction Web Application provides an intuitive interface for users to predict the price of cars based on various parameters. Leveraging the power of scikit-learn and Flask, the application offers accurate predictions and a seamless user experience. With its simple design and reliable performance, it serves as a valuable tool for car buyers and sellers alike.
