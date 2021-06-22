from flask import Flask, Response
import pandas as pd
import os
app = Flask(__name__)

trained_model = pd.read_pickle(os.path.join('models', 'baummethoden.pickle'))
prediction_data = pd.read_csv(os.path.join('data', 'prediction_input.csv'))

@app.route('/')
def main():
    return Response(prediction_data.to_json(), mimetype='application/json')
