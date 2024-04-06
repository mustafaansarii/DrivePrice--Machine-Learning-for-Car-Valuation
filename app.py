from flask import Flask, render_template, request
import modelbit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', prediction_text="")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve form data
        year = int(request.form['Year'])
        present_price = float(request.form['Present_Price'])
        kms_driven = float(request.form['Kms_Driven'])
        num_owners = int(request.form['Owner'])
        fuel_type = request.form['Fuel_Type_Petrol']
        seller_type = request.form['Seller_Type_Individual']
        transmission_type = request.form['Transmission_Manual']

        # Mapping the fuel type, seller type, and transmission type to numerical values
        fuel_type_mapping = {"Petrol": 0, "Diesel": 1, "CNG": 2}
        seller_type_mapping = {"Dealer": 1, "Individual": 0}
        transmission_type_mapping = {"Manual": 0, "Automatic": 1}

        # Getting the numerical values
        fuel_type_numeric = fuel_type_mapping.get(fuel_type)
        seller_type_numeric = seller_type_mapping.get(seller_type)
        transmission_type_numeric = transmission_type_mapping.get(transmission_type)

        # Getting the inference
        inference_result = modelbit.get_inference(
            region="ap-south-1",
            workspace="mustafaansari",
            deployment="predict_car_price",
            data=[year, present_price, kms_driven, num_owners, fuel_type_numeric, seller_type_numeric, transmission_type_numeric]
        )

        # Extracting the output message from the dictionary and removing the quotes
        output_message = inference_result['data'].strip('"')

        return render_template('index.html', prediction_text=output_message)

if __name__ == '__main__':
    app.run(debug=True)
