# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 15:32:11 2022

@author: Juan Manuel
"""

'''
Polynomial Linear Regression

y = b0 + b1*x1 + b2*x1^2 + ... bn*x1^2
Se mantiene la misma variable x1

'''

'''
Import libraries
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


'''
Import dataset
'''
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[ : , 1:-1 ].values
y = dataset.iloc[ : , -1].values


'''
Training the Linear Regression model on the whole dataset
'''
#from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state = 0)
lin_reg = LinearRegression()
lin_reg.fit(x, y) #no realizamos el split para coger el máximo de datos

'''
Training the Polynomial Regression model on the whote dataset

Se realiza a partir de Multiple Linear Regression

    1. Se crea una matriz con (x1, x1^2, x1^3,...) (PolynomialFeatures class)
    2. Se crea una linearRegression
    
    degree = 2 --> y = b0 + b1*x1 + b2*x1^2
    degree = 4 --> y = b0 + b1*x1 + b2*x1^2 + b3*x1^3 + b4*x1^4
'''
from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(x)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

'''
Visualising the Linear Regression results
'''
plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg.predict(x), color = 'blue')
plt.title('Truth or Bluff (Linear Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

'''
Visualising the Polynomial Regression results
'''
plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg_2.predict(x_poly), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


'''
Visualising  the Polynomial Regression results (for higher resolution and smoother curve)
'''
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, lin_reg_2.predict(poly_reg.fit_transform(x_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression smoother')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

'''
Prediction a new result with Linear regression

[[6.5]] matrix 2
'''
print(lin_reg.predict([[6.5]]))

'''
Predicting a new result with Polynomial Regression

'''
print(lin_reg_2.predict(poly_reg.fit_transform([[6.5]])))