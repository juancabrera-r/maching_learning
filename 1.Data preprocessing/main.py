# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:35:46 2022

@author: Juan Manuel
"""

'''
IMPORT LIBRARIES
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''
Importing the dataset
'''
dataset = pd.read_csv('Data.csv')
#feature o independ variable
x = dataset.iloc[:,:-1].values #crea una matriz con todas las filas y todas las columnas menos la última
y = dataset.iloc[:,-1].values
print(x)
print(y)

'''
Taking care of missing data
Remplaza el valor que falta por la media del resto de valores
Saikat learn (libreria)
'''
from sklearn.impute import SimpleImputer

#funcion SimpleImputer(missing_values = 'valores nan', strategy='media')
imputer = SimpleImputer(missing_values = np.nan, strategy='mean') 
#indicamos donde se calculas los valores "missing", en este caso las columnas Age y Salary
imputer.fit(x[:,1:3]) 
#indicamos en que columnas se deben guardar los nuevos datos
x[:, 1:3] = imputer.transform(x[:,1:3])

'''
Encoding categorical data
Se asigna a cada "string" (France, Spain, Germany) un numero, para evitar descorrelaciones
Al existir 3 variables, se crean 3 columnas de manera que cada pais se identifica por 1 vector
Francia 0 0 1
Spain 0 1 0
Germany 1 0 0 
se llama -> One hot encoding
'''
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# [0] indica la columna Country
#passthrough  indica que queremos mantener la columna Age y Salary
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])],
                       remainder='passthrough')

#
x = np.array(ct.fit_transform(x))

print(x)

'''
Encoding the Dependent Variable
'''
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y = le.fit_transform(y)
print(y)

'''
Splitting the dataset into the Training set and Test set
'''
from sklearn.model_selection import train_test_split

#observación realizadas, el 20% test, 80% train
# de 10 clientes, 8 se asignan a train y 2 a test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

'''
Feature skealing
Se puede hacer "estandarización" o "normalización"
Significa escalar una serie de valores por ejemplo entre 0 y 1 (normalización)
Entre -3 y +3 (estandarización), tb entre -2 y +2

Fit --> calcula la media (mean) y la desviación estandar (standar deviation - std) usada para el escalado
Transform --> aplica la fórmula de estandarización (Standardization) y escala
Fir-Transform --> primero aplica fit y luego transforma
'''
from sklearn.preprocessing import StandardScaler

#aplicamos estandarización
sc = StandardScaler()
#No debemos estandarizar la columna "country", unicamente en Age y Salary
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] = sc.transform(x_test[:, 3:])

print(x_train)
print(x_test)






