# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 05:56:19 2022

@author: Juan Manuel
"""

'''

SIMPLE LINEAL REGRESSION
modelo matemático para aproximar la relación de dependencia entre una
variable dependiente Y(salario), n variables independientes X (años experiencia)
y = a*x + b

'''


'''
Import libraries
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''
Importing the dataset
'''
dataset = pd.read_csv('Salary_Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

print(x)
print(y)

'''
Splitting the dataset into the Training set and Test set
20% del muestreo son seleccionados para test y el 80% para training
'''

from sklearn.model_selection import train_test_split

#observación realizadas, el 20% test, 80% train
# de 10 clientes, 8 se asignan a train y 2 a test
#random_state = 0 -> coge los últimos valores para testeo.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)


'''
Training the Simple Linear Regression model on the Training Set
'''

from sklearn.linear_model import LinearRegression

regressor = LinearRegression() #llama a la clase LinearRegression
#Fit --> fit linear model
regressor.fit(x_train, y_train) #fit es una función de LinearRegression

'''
Predicting the Test set result
Predecir el salario para cada muestra de test (el 20%) 
'''

y_pred = regressor.predict(x_test)

'''
Visualising the Training set result
#Scatter --> plot y vs. x
'''
y_pred_train = regressor.predict(x_train) 

plt.scatter(x_train, y_train, color= 'red')
plt.plot(x_train, y_pred_train, color = 'blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

'''
Visualising the Test set result
'''

plt.scatter(x_test, y_test, color= 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

'''
Making a single prediction
Salario para un empleado con 12 años d eexperiencia.
Se usa dobre pareja de corchetes pq el método predict espera una matriz 2D
12 --> escalar
[12] --> 1D array
[[12]] --> 2D array
'''
print(regressor.predict([[12]]))

'''
Getting the final linear regression expression
Salary = a*x + b
a = 9313.57
b= 26780.099
'''
print(regressor.coef_)
print(regressor.intercept_)