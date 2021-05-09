import pandas as pd
import csv
import math
import random

def loadCSV(filename):
    lines = csv.reader(open(r'pima-indians-diabetes.csv'))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i]=[float(x) for x in dataset[i]]
    return dataset

def splitDataset(dataset,splitratio):
    trainSize = int(len(dataset)*splitratio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange((len(copy)))
        trainSet.append(copy.pop(index))
    return  [trainSet,copy]


def separateByClass(dataset):
    separated={}
    for i in range(len(dataset)):
        vector=dataset[i]
        if vector[-1] not in separated:
            separated[vector[-1]]=[]
        separated[vector[-1]].append(vector)
    return separated

def mean(numbers):
    return sum(numbers)/float(len(numbers))


def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg,2) for x in numbers])/(float(len(numbers)-1))
    return math.sqrt(variance)

def summarize(dataset):
    summaries = [(mean(attributes),stdev(attributes)) for attributes in zip(*dataset)]
    del summaries[-1]
    return summaries

def summarizeByClass(dataset):
    separated  = separateByClass(dataset)
    summaries={}
    for classValue,instances in separated.items():
        summaries[classValue] = summaries(instances)
    return summaries