import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import pickle 
from PIL import Image
from glob import glob
from sklearn.decomposition import PCA

def eigenImage():
    data = np.load("data_norm.npz")

    X = data['arr_0'] # independent features
    y = data['arr_1'] # target value

    # print(X.shape)
    # print(y.shape)

    X1 = X - X.mean(axis = 0)
    # X1 = np.cov(X)

    # print(X1.shape)

    # pca = PCA(n_components=None,whiten=True,svd_solver='auto')

    # x_pca = pca.fit_transform(X1)

    # print(x_pca.shape)

    # eigen_ratio = pca.explained_variance_ratio_
    # eigen_ratio_cum = np.cumsum(eigen_ratio)

    # # print(eigen_ratio_cum)

    # plt.figure(figsize=(10,4))
    # plt.subplot(1,2,1)
    # plt.plot(eigen_ratio[:200],'r>--')
    # plt.xlabel('no. of components')
    # plt.ylabel('Explained Variance ratio')
    # plt.subplot(1,2,2)
    # plt.xlabel('no. of components')
    # plt.ylabel('Cumulative Explained Variance ratio')
    # plt.plot(eigen_ratio_cum[:200],'r>--')
    # plt.show()

    pca_50 =  PCA(n_components=50,whiten=True,svd_solver='auto')
    x_pca_50 = pca_50.fit_transform(X1)

    # print(x_pca_50.shape)

    # pickle.dump(p, file)

    pickle.dump(pca_50,open("pca.pickle","wb"))

    x_pca_inv = pca_50.inverse_transform(x_pca_50)

    # print(x_pca_inv.shape)

    # eig_img = x_pca_inv[1,:]
    # eig_img_re = eig_img.reshape((100,100))
    # plt.imshow(eig_img_re,cmap="gray")
    # plt.show()
    # pics = np.random.randint(0,240,40)
    # plt.figure(figsize=(15,8))
    # for i,pic in enumerate(pics):
    #     plt.subplot(4,10,i+1)
    #     img = X[pic,:].reshape(100,100)
    #     plt.imshow(img,cmap='gray')
    #     plt.title('{}'.format(y[pic]))
    #     plt.xticks([])
    #     plt.yticks([])
    # print("="*20+'Eigen Images'+"="*20)
    # plt.figure(figsize=(15,8))
    # for i,pic in enumerate(pics):
    #     plt.subplot(4,10,i+1)
    #     img = x_pca_inv[pic,:].reshape(100,100)
    #     plt.imshow(img,cmap='gray')
    #     plt.title('{}'.format(y[pic]))
    #     plt.xticks([])
    #     plt.yticks([])
    # plt.show()

    np.savez("data_pca_mean.pickle.npz",x_pca_50,y,X.mean(axis=0))
# eigenImage()