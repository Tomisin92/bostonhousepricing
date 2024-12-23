import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np

app = Flask(__name__)  # starting point of where the application will run

# Load the model
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/regpredict_api', methods=['POST'])
def regpredict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1, -1))
    
    # Transform input data
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    
    # Predict
    output = regmodel.predict(new_data)[0]
    formatted_output = round(output, 2)  # Format to 2 decimal places
    
    # Check for negative prediction
    if formatted_output < 0:
        message = "The prediction is negative. This may indicate an issue with the model or input data."
        print(message)
        return jsonify({"message": message, "prediction": formatted_output})
    
    print(formatted_output)
    return jsonify({"prediction": formatted_output})

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scalar.transform(np.array(data).reshape(1, -1))
    print(final_input)
    
    # Predict
    output = regmodel.predict(final_input)[0]
    formatted_output = round(output, 2)  # Format to 2 decimal places
    
    # Check for negative prediction
    if formatted_output < 0:
        message = "The prediction is negative. This may indicate an issue with the input data."
        return render_template("home.html", prediction_text=message)
    
    return render_template("home.html", prediction_text="The house price prediction is ${}k".format(formatted_output))

if __name__ == "__main__":
    app.run(debug=True)

