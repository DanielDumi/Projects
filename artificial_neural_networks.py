# artificial neural network
# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# data preprocessing
# importing dataset
dataset = pd.read_csv("Churn_Modelling.csv")
x = dataset.iloc[:, 3:-1].values
y = dataset.iloc[:, -1].values

# encoding categorical data
# label encoding the 'gender' column
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
x[:, 2] = le.fit_transform(x[:, 2])

# one hot encoding the 'geography' column (dummy variables)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

# splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=0)

# feature scaling (compulsory for deep learning)
# whenever building artificial neural network, apply feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# building the ANN
# initialising the ANN(ann as a sequential class)
ann = tf.keras.models.Sequential()

# adding the input layer and the first hidden layer
# adding 6 neurons (can experiment with other values)
# adding activation function (relu)
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

# adding the second hidden layer (relu = rectifier linear unit)
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

# adding the output layer
# need one neuron since we have a binary outcome
# using the sigmoid activation function
ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# training the ANN
# compiling the ANN
ann.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# training the ANN on the training set
ann.fit(x_train, y_train, batch_size=32, epochs=100)

# making the predictions and evaluating the model
# predicting the result of a single observation
# can add before the final parentheses > 0.5 in order to have a message regarding the prediction
print(ann.predict(sc.transform([[1, 0, 0, 600, 1, 40, 3, 60000, 2, 1, 1, 50000]])))

# predicting the test set results
y_pred = ann.predict(x_test)
y_pred = (y_pred > 0.5)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

# making the confusion matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))