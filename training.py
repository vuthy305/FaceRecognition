import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

def generateSVM(X,y):
    model_tune = SVC()
    param_grid = {
        'C':[1,10,20,30,50,100],
        'kernel':['rbf','poly','linear'],
        'gamma': [0.1,0.05,0.01,0.001,0.002,0.005],
        'coef0':[0,1]
    }
    model_grid = GridSearchCV(model_tune, param_grid= param_grid,scoring="accuracy",cv=5,verbose=1)

    model_grid.fit(X,y)
    return model_grid.best_params_['C'],str(model_grid.best_params_['kernel']),model_grid.best_params_['gamma'],model_grid.best_params_['coef0']
    # print(model_grid.best_score_)

def training():
    data = np.load("data_pca_mean.pickle.npz")

    X = data['arr_0']
    y = data['arr_1']
    mean = data['arr_2']
    

    x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.3,stratify=y)
    # x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
    # print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)

    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)

    c,k,g,co= generateSVM(X,y)
    print(c,k)
    # model = SVC(C=1,kernel='rbf',gamma=0.002,probability=True)
    model = SVC(C=c,kernel=k,gamma=g,probability=True,coef0=co)
    # model = SVC(C=1,kernel='linear',gamma=0.07,probability=True)
    # model = SVC(C=1,kernel='poly',gamma=0.03,probability=True)
    # model = GaussianNB()
    model.fit(x_train, y_train)

    

    guassianModel = GaussianNB(var_smoothing=0.2848035868435802)
    guassianModel.fit(x_train, y_train)
    # model.fit(x_train,y_train)
    # print("Model trained sucessfully")
    # print(guassianModel.score(x_test, y_test))

    # print("Using SVM")
    # print(model.score(x_train, y_train))
    # print(model.score(x_test, y_test))

    # y_pred = model.predict(x_test)
    # y_prob = model.predict_proba(x_test)

    # cm = metrics.confusion_matrix(y_test,y_pred)
    # cm = np.concatenate((cm,cm.sum(axis=0).reshape(1,-1)),axis=0)
    # cm = np.concatenate((cm,cm.sum(axis=1).reshape(-1,1)),axis=1)
    # plt.imshow(cm)
    # for i in range(9):
    #     for j in range(9):
    #         plt.text(j,i,'%d'%cm[i,j])
            
    # plt.xticks([0,1])
    # plt.yticks([0,1])
    # plt.xlabel('Predicted Values')
    # plt.ylabel('True Values')
    # plt.show()

    # print(cm)

    # cr = metrics.classification_report(y_test,y_pred,output_dict=True)
    # print(metrics.cohen_kappa_score(y_test,y_pred))

    # print(pd.DataFrame(cr).T)

    pickle.dump(model, open('model_svm_pickle.pickle','wb'))
    pickle.dump(guassianModel, open('model_gussianNaviBayes_pickle.pickle','wb'))
    pickle.dump(mean, open('mean_preprocess.pickle','wb'))
# training()