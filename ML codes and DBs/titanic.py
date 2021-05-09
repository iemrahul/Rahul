## Importing All the Usefull Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score



## Get Data
titanic_data = pd.read_csv('titanic.csv')

## Data Analysis
#sns.countplot(x="SibSp",data=titanic_data)
#titanic_data["Age"].plot.hist()

#sns.boxplot(x="Pclass", y= "Age",data=titanic_data)
#plt.show()
titanic_data.drop("Cabin",axis=1, inplace=True)
titanic_data.dropna(inplace=True)
#sns.heatmap(titanic_data.isnull(),yticklabels=False)

##Data Wrangling
sex = pd.get_dummies(titanic_data["Sex"],drop_first=True)
embark = pd.get_dummies(titanic_data["Embarked"],drop_first=True)
pcl = pd.get_dummies(titanic_data["Pclass"],drop_first=True)
# print(sex.head(5))
# print(embark.head(5))
# print(pcl.head(5))
titanic_data = pd.concat([titanic_data,sex,pcl,embark],axis=1)
titanic_data.drop(['Sex','Pclass','Embarked','Name','Ticket','PassengerId'],axis=1,inplace=True)
#print(titanic_data.head(5 ))
### Train data

X = titanic_data.drop("Survived",axis=1)
Y = titanic_data["Survived"]
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.33,random_state=20)
logmodel = LogisticRegression(max_iter=2000000)
logmodel.fit(X_train,Y_train)
prediction = logmodel.predict(X_test)
classification_report(Y_test,prediction)
print(confusion_matrix(Y_test,prediction))


## Data Accuracy


print(accuracy_score(Y_test,prediction))
plt.show()
