# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 12:08:55 2022

@author: srini
"""

from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
import sklearn
import pickle
import pandas as pd
from sklearn.utils.validation import check_array
import numpy as np
from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()


app = Flask(__name__)
CORS(app, support_credentials=True)
model1 = pickle.load(open("log_model1.pkl", "rb"))
@app.route('/',methods=['POST','GET'])


@app.route("/")
@cross_origin(supports_credentials=True)
def home():
    return render_template("index.html")


@app.route("/predict", methods = ['POST'])
@cross_origin()
def predict():
    if request.method == "POST":
        Time_to_play = 0
        Can_you_walk_to_a_park = 0
        Can_you_walk_to_a_play_area = 0
        Time_to_play=request.form['Time_to_play']
        
        if(Time_to_play=='No, I need a lot more'):
            Time_to_play = 0
            
        else:
           
            Time_to_play = 1
            Time_to_play = 2
            Time_to_play = 3
            
        Can_you_walk_to_a_park = request.form['Can_you_walk_to_a_park']
        if(Can_you_walk_to_a_park == 'Yes'):
            Can_you_walk_to_a_park = 1
            
        else:
            Can_you_walk_to_a_park = 0
        Can_you_walk_to_a_play_area = request.form['Can_you_walk_to_a_play_area']
        if(Can_you_walk_to_a_play_area=='Yes'):
            Can_you_walk_to_a_play_area = 1
        else:
            Can_you_walk_to_a_play_area = 0
            
        data = ['Can_you_walk_to_a_play_area','Can_you_walk_to_a_park','Time_to_play']
        data = lb.fit_transform(data)
        prediction = model1.predict([data])
        if prediction == 0:
            return render_template('index.html',prediction_text = "Borderline_Difficulties")
        elif (prediction == 1):
            return render_template('index.html', prediction_text = "Clinically_Singificant_Difficulties")
        else:
         return render_template('index.html', prediction_text = "Expected")
     
    else:
         return render_template('index.html')
        

        
if __name__ == "__main__":
    app.run(debug=False)