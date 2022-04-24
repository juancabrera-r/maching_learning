# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:00:48 2022

@author: Juan Manuel
"""

'''
MULTIPLE LINEAR REGRESSION

Ejercicio:
    Determinar cuales son las CIA más interesante en invertir.
    R&D Spend | Administration | Marketing Spend | State | Profit
    Para ellos hay que ver cuanto gastan en R&D, administration y marketing y
    cuanto profit hacen

multiple linear regression 
    y = b0 + b1*x1 + b2*x2 + ... * b3*x3
    y --> variable dependiente (Profit)
    x -> variables independientes (Rest variable)
    State -> categorical variable, para cada categoría se crea una columna y 
        se completa con 1 y 0. 
        A estas nuevas variables se denominan Dummy Variables (D1)
        Por ejemplo: si son dos variables NY y California. D1 será 1 para NY
        y 0 para California.
        IMPORTANTE --> SIEMPRE HAY QUE OMITIR 1 DUMMY VARIABLE, si hay 3 DV se omite 1
    
    y = b0 + b1*x1 + b2*x2 + b3*x3 + b4*D1

Suposiciones en multiple linear regression:
    Hay que comprobar que se cumplen cada una de las suposiciones
    1. Linearity
    2. Homoscedasticity
    3. Multivariate normality
    4. Independence of erros
    5. Lack of multicollinearity

Statistical significance (significación estadística):
        es la probabilidad de que una relación entre dos o más variables en un
        análisis no sea pura coincidencia, sino que en realidad sea causada por
        otro factor. En otras palabras, la significancia estadística es una
        forma de demostrar matemáticamente que puedes confiar en una
        estadística determinada.
        https://mixpanel.com/es/topics/statistical-significance/
'''

'''
BUILD A MODEL
    
5 methos of building models:
    1. All-in
    2. Backward Elimination (SE USA ESTE EN EL EJERCICIO)
    3. Forward Selection
    4. Biderectional Elimination
    5. Score Comparison

    Stepwise regression --> refers 2, 3 y 4
    
All-in - cases: usa todas las variables
    - Prior knowledge
    - You have to
    - Preparing for Backward Elimination
    
Backward Elimination:
    1. Select a significance level to stay in the model. (Ej. SL = 0.05 (5%))
    2. Fit the full model with all possible predictos
    3. Consider the predictor with the highest P-value
        If P > SL, go to STEP 4, otherwise go to FIN
    4. Remove the predictor
    5. Fit the model without this variable -> go to STEP 3
    FIN: your model is ready

Forward Selection:
    1. Select a significance level to enter the model (Ej. SL=0.05)
    2. Fit all regression models y - xn Select the one with the lowest P-value
    3. Keep this variable and fit all possible models with one extra predictor
        added to the one(s) you already have
    4.Consider the predictor with the lowest P-value.
        If P < SL, go to STEP 3, otherwise go to FIN
        FIN: keep the previous model

Bidirectional Elimination
    1. Select a significance level to enter an d to stay in the model
        Ej. SLENTER = 0.05, SLSTAY = 0.05
    2. Perform the next step of Forward Selection
        New variables must have: P < SLENTER to enter
    3. Perform ALL steps of Backward Elimination
        old variables must have P < SLSTAY to stay
    4. No new variables can enter and no old variables can exit
    FIN: your model is ready
        
All Possible Models
    1. Select a criterion of goodness (Ej. Akaike criterion)
    2. Construct All Possible Regression Models: 2^N-1 total combinations
    3. Select the one with the best criterion
    FIN: Your model is ready

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
dataset = pd.read_csv('50_Startups.csv')
x = dataset.iloc[ : , :-1].values
y = dataset.iloc[ : , -1].values

'''
Missing datas
'''



'''
Encoding the independent variable
'''
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])],
                       remainder='passthrough')
x = np.array(ct.fit_transform(x))


'''
Splitting the dataset into the Training set & Test set
'''
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2,
                                                    random_state = 0)

'''
Training the Multiple Linear Regression model on the Training set
'''
from sklearn.linear_model import LinearRegression

regressor = LinearRegression() #built the model
regressor.fit(x_train,y_train) #training the model

'''
Predicting the Test set result
There are 4 feature (4 variables) so it can't be plot
'''

y_pred = regressor.predict(x_test)
np.set_printoptions(precision=2) #ajustamos a 2 decimales
#.reshape(len()) --> permite mostrar los datos de forma vertical
#axis = 1 --> concatenate vertically
#axis = 0 --> concatenate horizontally
print(np.concatenate((y_pred.reshape(len(y_pred),1),
                      y_test.reshape(len(y_test),1)), 1)) 

'''
Making a single prediction (for example the profit of a startup with 
                            R&D Spend = 160000, Administration Spend = 130000,
                            Marketing Spend = 300000 and State = 'California')
'''

print(regressor.predict([[1, 0, 0, 160000, 130000, 300000]]))

'''
Getting the final linear regression equation with the values of the coefficients
herefore, the equation of our multiple linear regression model is:

Profit=86.6×Dummy State 1−873×Dummy State 2+786×Dummy State 3+
0.773×R&D Spend+0.0329×Administration+0.0366×Marketing Spend+42467.53
'''
print(regressor.coef_)
print(regressor.intercept_)