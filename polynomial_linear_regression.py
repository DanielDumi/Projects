# importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing dataset
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# splitting categorical data
# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=0)


# training the linear regressio model on the whole dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

# training the polynomial regression model on the whole dataset
from sklearn.preprocessing import PolynomialFeatures
# getting better predictions
poly_reg = PolynomialFeatures(degree=6)
x_poly = poly_reg.fit_transform(x)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

# visualising the linear regression results
plt.scatter(x, y, color='red')
plt.plot(x, lin_reg.predict(x), color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position label')
plt.ylabel('Salary')
plt.show()

# visualising the polynomial linear regression results
plt.scatter(x, y, color='red')
plt.plot(x, lin_reg_2.predict(poly_reg.transform(x)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position label')
plt.ylabel('Salary')
plt.show()

# visualising the polynomial regression result(for higher resolutin and smoother curve)
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color='red')
plt.plot(x_grid, lin_reg_2.predict(poly_reg.fit_transform(x_grid)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position label')
plt.ylabel('Salary')
plt.show()

# predicting a new result with linear regression
lin_reg.predict([(6.5)])

# predicting a new result with polynomial regression
lin_reg_2.predict(poly_reg.fit_transform([(6.5)]))
