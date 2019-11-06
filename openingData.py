import numpy as np
import matplotlib.pyplot as plt
import pandas

temp = open("iris.data", "r")
dataSet = temp.read()
print(dataSet)

### USING PANDAS
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

print(dataset)

