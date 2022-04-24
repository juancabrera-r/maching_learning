# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 06:22:21 2022

@author: Juan Manuel
"""

'''
RANDOM FOREST REGRESSION

Random forest es una versión de ensemble learing

    1. Pick at random K data proints from the Training set.
    2. Build the Decision Tree associated to these K data points
    3. Choose the number Ntree of trees you want to build and repeat 1 y 2.
    4. For a new data point, make each one of your Ntree trees predict the
    value of Y to for the data point in question, and assign the new data
    point the average across all of the predicted Y values
    
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
Training the Random Forest Regression model on the whole dataset
'''
from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(x, y)


'''
Predicting a new result

'''
print(regressor.predict([[6.5]]))


'''
Visualising the Decision Tree Regression results (higher resolution)
'''
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, regressor.predict(x_grid), color = 'blue')
plt.title('Random Forest Regression')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()