#-*- coding=utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

import sklearn.preprocessing as sp


image_path = r"D:\Project-KOL\Data\\"
train_dataPath = r"D:\Project-KOL\Data\214_train_data.csv"
all_dataPath = r"D:\Project-KOL\Data\feed.csv"

#Read 300+ train Data
name = ['city level','industry','pubmed','WanFang','Trial','Class','BedCount','Pysician#','DailyPatient#','5Yrs','IMS GLP1','IMS Trulicity','HDF Patients','HDF Article','HDF Total']
pd_train_data = pd.read_csv(train_dataPath,usecols=(1,2,3,4,5,8,9,10,11,12,13,14,15,16,17),names=name,header=0)
pd_all_data = pd.read_csv(all_dataPath,usecols=(4,6,7,8,11,12,13,14,15,16,17,18,19,20,21),names=name,header=0,encoding="gb2312")


print(pd_train_data[['industry','pubmed','WanFang']].describe())
print(pd_all_data[['industry','pubmed','WanFang']].describe())

print(pd_train_data[['Score']])

#数据归一化
min_max_scaler = sp.MinMaxScaler()
X_train_minmax = min_max_scaler.fit_transform(pd_train_data)
print(type(pd_train_data))
print(type(X_train_minmax))
print(X_train_minmax.take([1,2,3],axis=1))

#绘制直方图矩阵
pd_train_data.hist( figsize=(10,10),layout=(3,5))
plt.savefig(image_path+'train_bar_chart.png')
plt.show()



plt.close()
pd_all_data.hist(figsize=(10,10),layout=(3,5))
plt.savefig(image_path+'all_bar_chart.png')

plt.show()
plt.close()



# find common features as below
# choose 'industry','pubmed','WanFang' as variable