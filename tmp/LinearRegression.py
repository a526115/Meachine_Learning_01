from numpy import genfromtxt
import numpy as np
from sklearn import datasets, linear_model
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dataPath = r"D:\Project-KOL\Data\214_train_data.csv"

image_path = r"D:\Project-KOL\Data\\"
train_dataPath = r"D:\Project-KOL\Data\214_train_data.csv"
all_dataPath = r"D:\Project-KOL\Data\feed.csv"

name = ['industry','pubmed','WanFang','Score']
pd_train_data = pd.read_csv(train_dataPath,usecols=(2,3,4,19),names=name,header=0)
#print(pd_train_data)
print(pd_train_data[['industry','pubmed','WanFang']])
print(pd_train_data[['Score']])




x = pd_train_data[['industry','pubmed','WanFang']]
y = pd_train_data[['Score']]

print ("x: ")
print (x)
print ("y: ")
print (y)

regr = linear_model.LinearRegression()
regr.fit(x, y)

#打印出regr的参数
print ("cofficients")
print (regr.coef_)
print ("intercept: ")
print (regr.intercept_)

# #预测一个例子
# xPred实际值是995
xPred = [[1,0,254]]
yPred = regr.predict(xPred)
print ("real number for y is 2 and predicted y:")
print (yPred)


