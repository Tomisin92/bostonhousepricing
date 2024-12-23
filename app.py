import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

app=Flask(__name__)  # starting point of where my application will run
## Load the model
regmodel=pickle.load(open('regmodel.pkl', 'rb'))
scalar=pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/regpredict_api', methods=['POST'])

def regpredict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

if __name__=="__main__":
    app.run(debug=True)
    
    
    
