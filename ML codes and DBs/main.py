import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import csv
from random import *
import math
import operator


def euclidianDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


def loaddata(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])


def getNeighbor(trainingSet, testInstance, k):
    distance = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclidianDistance(testInstance, trainingSet[x], length)
        distance.append((trainingSet[x], dist))
    distance.sort(key=operator.itemgetter(1))
    neighbor = []
    for x in range(k):
        neighbor.append(distance[x][0])
    return neighbor


def getResponce(neighbor):
    classVotes = {}
    for x in range(len(neighbor)):
        responce = neighbor[x][-1]
        if responce in classVotes:
            classVotes[responce] += 1
        else:
            classVotes[responce] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


def getAccuracy(testSet, prediction):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == prediction[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0


trainingSet = []
testSet = []
split = 0.67
loaddata(r'iris.csv', split, trainingSet, testSet)
print('train  ', repr(len(trainingSet)))
print('test ', repr(len(testSet)))
prediction = []
k = 3
for x in range(len(testSet)):
    neighbor = getNeighbor(trainingSet, testSet[x], k)
    result = getResponce(neighbor)
    prediction.append(result)
    print('> predicted=', repr(result), ',actual = ', repr(testSet[x][-1]))
accuracy = getAccuracy(testSet, prediction)
print("Accuracy of iris data is ", repr(accuracy), "%")
