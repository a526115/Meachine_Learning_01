#-*- coding=utf-8 -*-
import pandas as pd
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
import sklearn.preprocessing as sp


image_path = r"D:\Project-KOL\Data\\"
train_dataPath = r"D:\Project-KOL\Data\214_train_data.csv"
all_dataPath = r"D:\Project-KOL\Data\feed.csv"

name = ['industry','pubmed','WanFang','Score']
pd_train_data = pd.read_csv(train_dataPath,usecols=(2,3,4,19),names=name,header=0)
#print(pd_train_data)
print(pd_train_data[['industry','pubmed','WanFang']])
print(pd_train_data[['Score']])

#数据归一化
# min_max_scaler = sp.MinMaxScaler()
# X_train_minmax = min_max_scaler.fit_transform(pd_train_data[['industry','pubmed','WanFang']])
y= [i for item in pd_train_data[['Score']].values for i in item]
# print(y)


# print(type(pd_train_data))

# # print(X_train_minmax.take([1,2,3],axis=1))
#x_test = [[6,0,123]]
x_test = [[0,6,7]]
# X_test_minmax = min_max_scaler.fit_transform(x_test)
# print("X_test_minmax is")
# print(X_test_minmax)
#
model = KNeighborsClassifier(n_neighbors=8)
model.fit(pd_train_data[['industry','pubmed','WanFang']], y)
#
print("Predicted Result is:")

predicted= model.predict(x_test)
print(predicted)