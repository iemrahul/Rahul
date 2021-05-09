from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

data = pd.read_csv(r'iris.csv')
#print(data.head())
X = data.drop(['names'],axis=1)
y = data['names']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=5)
print(X_train)