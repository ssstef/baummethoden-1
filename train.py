import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix  

import pickle

#List with attribute names (it is optional to do this but it gives a better understanding of the data for a human reader)
attribute_names = ['variance_wavelet_transformed_image', 'skewness_wavelet_transformed_image', 'curtosis_wavelet_transformed_image', 'entropy_image', 'class']

#Read csv-file
data = pd.read_csv('data/data_banknote_authentication.csv', names=attribute_names)

#Shuffle data
data = data.sample(frac=1)

#Get the absolute number of how many instances in our data belong to class zero
count_real = len(data.loc[data['class']==0])

#Get the absolute number of how many instances in our data belong to class one
count_fake = len(data.loc[data['class']==1])

#Get the relative number of how many instances in our data belong to class zero
percentage_real = count_real/(count_fake+count_real)

#Get the relative number of how many instances in our data belong to class one
percentage_fake = count_fake/(count_real+count_fake)

#'class'-column
y_variable = data['class']

#all columns that are not the 'class'-column -> all columns that contain the attributes
x_variables = data.loc[:, data.columns != 'class']

x_train, x_test, y_train, y_test = train_test_split(x_variables, y_variable, test_size=0.2)

classifier = DecisionTreeClassifier() 

classifier = classifier.fit(x_train, y_train) 

y_pred = classifier.predict(x_test) 

conf_mat = confusion_matrix(y_test, y_pred)

accuracy = (conf_mat[0,0] + conf_mat[1,1]) /(conf_mat[0,0]+conf_mat[0,1]+ conf_mat[1,0]+conf_mat[1,1])


file_to_write = open("models/baummethoden.pickle", "wb")
pickle.dump(classifier, file_to_write)


