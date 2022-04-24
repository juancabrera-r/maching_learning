# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 05:25:55 2022

@author: Juan Manuel
"""

'''
TREE REGRESSION

Dadas 2 variables x1 y x2, permite determinar una tercera dimensión y


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
Training the Decision Tree Regression model on the whole dataset
'''
from sklearn.tree import DecisionTreeRegressor

regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(x, y)


'''
Predicting a new result

Al no existir feature scaling no es necesario hacer transformaciones
'''
print(regressor.predict([[6.5]]))


'''
Visualising the Decision Tree Regression

No es escomendable usar la visualización de datos pq no tienen el mismo resultado
'''
plt.scatter(x, y, color = 'red')
plt.plot(x, regressor.predict(x), color = 'blue')
plt.title('Decision Tree Regression')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

'''
Visualising the Decision Tree Regression results (higher resolution)
'''
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, regressor.predict(x_grid), color = 'blue')
plt.title('Decision Tree Regression')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()