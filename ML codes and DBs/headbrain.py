# this is Linear regression example
# R-square method is used to check is the model is good fit or not

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

plt.rcParams['figure.figsize']= (20.0,10.0)
# names = ['Gender','Age Range','Head Size(cm^3)','Brain Weight(grams)']
data = pd.read_csv('./headbrain.csv')

X =  data['Head Size(cm^3)'].values
Y =  data['Brain Weight(grams)'].values
m = len(X)
X = X.reshape((m,1))
reg = LinearRegression()
reg = reg.fit(X,Y)
Y_pred =  reg.predict(X)
r2_score = reg.score(X,Y)
print(r2_score)