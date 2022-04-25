'''
K-NN
    1. Choose the number K of neighbors
    2. Take the K nearest neighbors of the new data point, according to the Euclidean distance (distance bw 2 points)
    3. Among these k neighbors, count the number of data points in each category
    4. Assign the new data point to th ecategory where you counted the most neighbors
'''

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

'''
Splitting the dataset into the Training set and Test set
'''
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)


'''
Feature Scaling

Es necesario escalar las variables Age y Salary. Purchased no es necesario 
pq ya está escalada
Escalar permite "normalizar" varias variables para que unas no tengan más peso que la otra
'''
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
x_train = sc.fit_transform(X_train)
x_test = sc.transform(X_test)

'''
Training the K-NN model on the Training set
'''
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors=5, metric = 'minkowski', p=2)
classifier.fit(x_train, y_train)

'''
Predicting a new result
predict_proba --> probabilidad estimada
predict --> predicción 
sc.transform --> transforma(30,78000) a la escala
'''
predict = classifier.predict(sc.transform([[30,87000]]))
print(predict)


'''
Predicting the Test set results

'''
y_pred = classifier.predict(x_test)
print(y_pred)
#concatena 2 predicciones para comparar los errores
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))


'''
Making the Confusion Matrix
Define el nº de predicciones correctas e incorrectas
True Negative, False Positive, False Negative, True Positivo
'''
from sklearn.metrics import confusion_matrix, accuracy_score

cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))

'''
Visualising the Training set results

meshgrid function is used to create a rectangular grid out of two given 
one-dimensional arrays representing the Cartesian indexing or Matrix indexing.
'''
from matplotlib.colors import ListedColormap

X_set, y_set = sc.inverse_transform(x_train), y_train

X1, X2 = np.meshgrid(np.arange(start = X_set[:,0].min() -10, stop = X_set[:,0].max() + 10, step = 0.25),
                     np.arange(start = X_set[:,1].min() -1000, stop = X_set[:,1].max() + 1000, step = 0.25))

plt.contourf(X1, X2, classifier.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red','green')))

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], c = ListedColormap(('red','green'))(i), label = j)

plt.show()

'''
Visualising the Test set results
'''

# X_set, y_set = sc.inverse_transform(x_test), y_test
#
# X1, X2 = np.meshgrid(np.arange(start = X_set[:,0].min() -10, stop = X_set[:,0].max() + 10, step = 0.25),
#                      np.arange(start = X_set[:,1].min() -1000, stop = X_set[:,1].max() + 1000, step = 0.25))
#
# plt.contourf(X1, X2, classifier.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
#              alpha = 0.75, cmap = ListedColormap(('red','green')))
#
# plt.xlim(X1.min(), X1.max())
# plt.ylim(X2.min(), X2.max())
#
# for i, j in enumerate(np.unique(y_set)):
#     plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], c = ListedColormap(('red','green'))(i), label = j)
#
# plt.show()