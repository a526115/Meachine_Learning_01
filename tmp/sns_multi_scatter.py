import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

image_path = r"D:\Project-KOL\Data\\"
train_dataPath = r"D:\Project-KOL\Data\214_train_data.csv"
all_dataPath = r"D:\Project-KOL\Data\feed.csv"

name = ['city level','industry','pubmed','WanFang','Trial','Class','BedCount','Pysician#','DailyPatient#','5Yrs','IMS GLP1','IMS Trulicity','HDF Patients','HDF Article','HDF Total']
pd_all_data = pd.read_csv(all_dataPath,usecols=(4,6,7,8,11,12,13,14,15,16,17,18,19,20,21),names=name,header=0,encoding="gb2312")


sns.pairplot(pd_all_data,vars=['city level','industry','pubmed','WanFang','Trial','Class','BedCount','Pysician#','DailyPatient#','5Yrs','IMS GLP1','IMS Trulicity','HDF Patients','HDF Article','HDF Total'])
plt.savefig(image_path+'sns_Mult_scatter_graph.png')
plt.show()
