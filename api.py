from flask import Flask, Response, jsonify, request
import pandas as pd
import os
from io import StringIO

app = Flask(__name__)

training_data = pd.read_csv(os.path.join('data', 'data_banknote_authentication.csv'))

trained_model = pd.read_pickle(os.path.join('models', 'baummethoden.pickle'))

prediction_data = pd.read_csv(os.path.join('data', 'prediction_input.csv'))

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
    variance_wavelet_transformed_image = request.args.get('variance_wavelet_transformed_image')
    skewness_wavelet_transformed_image = request.args.get('skewness_wavelet_transformed_image')
    curtosis_wavelet_transformed_image = request.args.get('curtosis_wavelet_transformed_image')
    entropy_image = request.args.get('entropy_image')

    print('variance_wavelet_transformed_image: ', variance_wavelet_transformed_image)


    if(variance_wavelet_transformed_image and skewness_wavelet_transformed_image and curtosis_wavelet_transformed_image and entropy_image):
        prediction_data = pd.DataFrame.from_dict({
            variance_wavelet_transformed_image: variance_wavelet_transformed_image,
            skewness_wavelet_transformed_image: skewness_wavelet_transformed_image,
            curtosis_wavelet_transformed_image: curtosis_wavelet_transformed_image,
            entropy_image: entropy_image
        }, orient = 'index')
        test_attribute_names = ['variance_wavelet_transformed_image', 'skewness_wavelet_transformed_image', 'curtosis_wavelet_transformed_image', 'entropy_image']

        csv_string = variance_wavelet_transformed_image + ',' + skewness_wavelet_transformed_image + ',' + curtosis_wavelet_transformed_image + ',' + entropy_image
        
        csv_data = StringIO(csv_string)

        prediction_data = pd.read_csv(csv_data, names=test_attribute_names)

        prediction = trained_model.predict(prediction_data)
        print(prediction)
        return {
            'result': prediction.item(0)
        }
    
    return Response('Please provide all neccessary parameters to get a prediction: variance_wavelet_transformed_image, skewness_wavelet_transformed_image, curtosis_wavelet_transformed_image, entropy_image', mimetype='application/json')