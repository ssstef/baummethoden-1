import pandas as pd
import pickle

# load trained model
file_to_open = open("models/baummethoden.pickle",'rb')
trained_model = pickle.load(file_to_open)
file_to_open = open("models/baummethoden.pickle",'rb')
file_to_open.close()

# load data that we want predictions for
test_attribute_names = ['variance_wavelet_transformed_image', 'skewness_wavelet_transformed_image', 'curtosis_wavelet_transformed_image', 'entropy_image']
prediction_data = pd.read_csv('data/data_banknote_authentication.csv', names=test_attribute_names)

print(trained_model.predict(prediction_data))