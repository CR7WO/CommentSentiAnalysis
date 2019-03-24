#!/usr/bin/env python
# -*- coding: utf-8  -*-
# PCA

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

if __name__ == '__main__':

# 获取数据 [1995 rows x 400 columns]
    df = pd.read_csv('data/wordVecs.csv')
    y = df.iloc[:,1]
    x = df.iloc[:,2:]


# PCA降维
##计算全部贡献率
    n_components = 50
    pca = PCA(n_components=n_components)
    pca.fit(x)
#print pca.explained_variance_ratio_

##PCA作图
    plt.figure(1, figsize=(4, 3))
    plt.clf()
    plt.axes([.2, .2, .7, .7])
    plt.plot(pca.explained_variance_, linewidth=2)
    plt.axis('tight')
    plt.xlabel('n_components')
    plt.ylabel('explained_variance_')
    plt.show()



##根据图形取10维
    x_pca = PCA(n_components = 10).fit_transform(x)





