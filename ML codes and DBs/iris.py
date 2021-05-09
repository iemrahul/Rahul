from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import csv
import pandas as pd

dataset = pd.read_csv(r'iris.csv')

X = dataset.drop(['names'],axis=1)
y = dataset['names']
for i in range(len(y)) :
    if y[i] == 'Iris-setosa':
        y[i] = 1
    elif y[i] == 'Iris-versicolor':
        y[i] = 2
    else :
        y[i]=3
lr = LinearRegression()
lr.fit(X,y)
print(lr.coef_)
print(lr.intercept_)
p = lr.predict([[1,2,3,3]])
print(p)