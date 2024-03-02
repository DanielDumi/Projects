## import the libraries
# numpy for working with arrays
import numpy as np
# for plotting charts
import matplotlib.pyplot as plt
# import data sets and pre process
import pandas as pd

## import data sets
dataset = pd.read_csv('Data.csv')
# take the indexes
# get all the values of the columns except the last one
x = dataset.iloc[:, :-1].values
# get all the values but only for the last column
y = dataset.iloc[:, -1].values

## taking care of missing data(there are gaps in the csv file)
# import the best library for machine learning
from sklearn.impute import SimpleImputer
# new variable
# replace all the missing values with the mean
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
# method to look at the missing data from salary and age columns(only for numerical)
imputer.fit(x[:, 1:3])
# do the replacement
x[:, 1:3] = imputer.transform(x[:, 1:3])
# check the new x
# print(x)


## encoding the independent variables
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))
# print(x)


## encoding the dependent variable
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)


##splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)

## feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
# fit will get the mean and standard deviation and transform will apply the formula
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] = sc.transform(x_test[:, 3:])
print(x_train)
print(x_test)

