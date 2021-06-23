from flask import Flask, Response, jsonify, request
import pandas as pd
import os
from io import StringIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

training_data = pd.read_csv(os.path.join('data', 'auto-mpg.csv'))

trained_model = pd.read_pickle(os.path.join('models', 'baummethoden.pickle'))

prediction_data = pd.read_csv(os.path.join('data', 'prediction_input_mpg.csv'))

@app.route('/')
def main():
    return {
        "hello": "world",
    }

@app.route('/training_data')
def do():
    return Response(training_data.to_json(), mimetype='application/json')

@app.route('/prediction_data')
def cool():
    return Response(prediction_data.to_json(), mimetype='application/json')

@app.route('/predict')
def stuff():
    zylinder = request.args.get('zylinder')
    ps = request.args.get('ps')
    gewicht = request.args.get('gewicht')
    beschleunigung = request.args.get('beschleunigung')
    baujahr = request.args.get('baujahr')


    if(zylinder and ps and gewicht and beschleunigung and baujahr):
        prediction_data = pd.DataFrame.from_dict({
            zylinder: zylinder,
            ps: ps,
            gewicht: gewicht,
            beschleunigung: beschleunigung,
            baujahr: baujahr
        }, orient = 'index')

        
        csv_string = ",".join([zylinder, ps, gewicht, beschleunigung, baujahr])

        csv_data = StringIO(csv_string)

        test_attribute_names = ['zylinder', 'ps', 'gewicht', 'beschleunigung','baujahr']
        prediction_data = pd.read_csv(csv_data, names=test_attribute_names)

        prediction = trained_model.predict(prediction_data)

        return {
            'result': prediction.item(0)
        }
    
    return Response('Please provide all neccessary parameters to get a prediction: zylinder, ps, gewicht, beschleunigung, baujahr', mimetype='application/json')