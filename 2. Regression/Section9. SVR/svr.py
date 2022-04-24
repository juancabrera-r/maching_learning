# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:05:00 2022

@author: Juan Manuel
"""

'''
SVR (Support Vector Regression)

https://aprendeia.com/maquina-de-vectores-de-soporte-regresion-teoria/


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
#print(x)
#print(y)
''' 1. Hay que transformar la variable que es de 1 dimensión a otra de 2 dimensión'''
y = y.reshape(len(y),1) #shape(nº row, nºcolum)
#print(y)


'''
Feature Scaling
En lineal regresion, multiple linea regression y polinomia regression no es necesario
aplicar feature scaling.

En necesario escalar los datos level y salary porque sus valores son muy distintos
Deben estar en el mismo rango.
'''
from sklearn.preprocessing import StandardScaler

#aplicamos estandarización
sc_x = StandardScaler() #creamos un objeto Scaler
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y)

#☺y[:, 1] = sc.fit_transform(y)
#x[:, 3:] = sc.transform(x_test[:, 3:])

print(x)
print(y)

'''
Training the SVR model on the whole dataset
'''
from sklearn.svm import SVR

regressor = SVR(kernel = 'rbf') #creamos un objeto 'regressor' que haga una petición a la clase
#rbf --> radial basic funtion. Función de aprendizaje para encontrar una clasificación
#o regresión no lineal.
regressor.fit(x, y.ravel()) #ravel() se coloca para eliminar un error

'''
Predicting a new reesult
'''
#Cuando se hace una predicción, la observación (6.5) debe estar en la misma
#escala en el modelo de entrenamiento
#regressor.predict(sc_x.transform([[6.5]]))
#el resultado está escalado. Hay que invertirlo
print(sc_y.inverse_transform(regressor.predict(sc_x.transform([[6.5]]))))

'''
Visualing the SVR results
'''
plt.scatter(sc_x.inverse_transform(x), sc_y.inverse_transform(y), color = 'red')
plt.plot(sc_x.inverse_transform(x), sc_y.inverse_transform(regressor.predict(x)), color = 'blue')
plt.title('Truth or Bluff (SVR')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

'''
Visualising the SVR result (smoother)
'''

x_grid = np.arange(min(sc_x.inverse_transform(x)), max(sc_x.inverse_transform(x)), 0.1)
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(sc_x.inverse_transform(x), sc_y.inverse_transform(y), color = 'red')
plt.plot(x_grid, sc_y.inverse_transform(regressor.predict(sc_x.transform(x_grid))), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression smoother')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


