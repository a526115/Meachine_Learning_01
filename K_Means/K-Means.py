# -*- coding: utf-8 -*-
# 'Python 3.6 with Anaconda'
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from K_Means.Find_Best_K import elbow_plot
import logging
import logging.config
import os
from K_Means.Config.logging_config import LOGGING
import configparser

'''
****************************
Get Custom Log Configuration
****************************
'''
logging.config.dictConfig(LOGGING)  # 导入上面定义的logging配置
logger = logging.getLogger(__name__)  # 生成一个log实例

'''
****************************
     Read config.ini
****************************
'''
cf = configparser.ConfigParser()
logger.info(os.path.abspath('.')+"/Config/config.ini")
cf.read(os.path.abspath('.')+"/Config/config.ini")


# def get_path_value(self, name):
#     value = self.cf.get("path", name)
#     return value
try:

    '''
    ******************************************************************************************
    __name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。
    这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行
    ******************************************************************************************
    '''
    if __name__ == '__main__':
        image_path = cf.get("path",'image_path')
        inputfile = cf.get("path",'input_file')+"214_train_data.xls"
        all_dataPath = cf.get("path",'input_file')+"feed.csv"
        output_file = cf.get("path",'input_file')+"KMeansOutput.xls"

        k = 3
        iteration = 500
        name = ['city level', 'industry', 'pubmed', 'WanFang', 'Trial', 'Class', 'BedCount', 'Pysician#',
                'DailyPatient#',
                '5Yrs', 'IMS GLP1', 'IMS Trulicity', 'HDF Patients', 'HDF Article', 'HDF Total']
        data = pd.read_excel(inputfile, index_col='ID', names=name)
        '''
        ****************************************************************
        用0-score方法做数据标准化-归一化处理数据，该方法比较适合计算距离
        ****************************************************************
        '''
        data_zs = 1.0 * (data - data.mean()) / data.std()
        # logger.info(data_zs)


        logger.info('#PCA算法降维 and 主成分分析 mle -->自动确认最佳分类\n')
        logger.info('全部贡献率如下：\n')
        pca = PCA(n_components=15)
        pca.fit(data_zs)
        PCA(copy=True, n_components=15, whiten=False)
        logger.info('#变量方差贡献率 用于剔除贡献率低的维度')
        logger.info(pca.explained_variance_ratio_)  # 变量方差贡献率 用于剔除贡献率低的维度

        logger.info('自适应贡献率如下:')
        pca = PCA(n_components='mle')
        pca.fit(data_zs)
        PCA(copy=True, n_components='mle', whiten=False)
        logger.info('#mle 自动选择维度结果')
        logger.info(pca.explained_variance_ratio_)

        logger.info('#KMeans模型确定确定最佳k值')
        target_data = data_zs[['city level', 'industry', 'pubmed', 'WanFang', 'Trial', 'Class', 'BedCount', 'Pysician#',
                            'DailyPatient#',
                            '5Yrs', 'IMS GLP1', 'IMS Trulicity']].copy()
        '''
        ***********************
        画折线图显示k值变化趋势
        ***********************
        '''
        elbow_plot(target_data)

        model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration)
        model.fit(data_zs)

        r1 = pd.Series(model.labels_).value_counts()  # 统计各个类别的数目
        r2 = pd.DataFrame(model.cluster_centers_)  # 显示矩阵中心

        '''
        *************************************
        # K Means --> 整理输出数据格式 
        *************************************
        '''
        r = pd.concat([r2, r1], axis=1)
        logger.info(r1)
        # logger.info(r2)
        # logger.info(r)
        r3 = pd.concat([data, pd.Series(model.labels_)], axis=1)
        # logger.info(r3)
        test = pd.DataFrame(r3)
        # logger.info(test)
        '''
        **************
        结果输出重定向
        **************
        '''
        # 输出重定向
        test.to_excel(output_file)

except Exception as e:
    logger.info(e)
