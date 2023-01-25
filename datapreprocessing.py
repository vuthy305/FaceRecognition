import pickle
import numpy as np
import matplotlib.pyplot as plt 

def dataPreProcessing():
    label_ids = {}
    ids = {}
    current_id = 0
    current_i = 0
    y_norm  = []
    df = pickle.load(open('all_data_image.pickle','rb'))

    # independent features
    X = df.iloc[:,2:].values
    # dependent features
    y = df.iloc[:,1].values
    # id features
    id = df.iloc[:,0].values

    Xnorm = X / X.max()

    for label in y:
        if not label in label_ids:
            label_ids[label] = current_id
            current_id += 1
        id_ = label_ids[label]
        y_norm.append(id_)
    for i in id:
        if not i in ids:
            ids[i] = current_i
            current_i += 1

    pickle.dump(label_ids,open('label.pickle','wb'))
    pickle.dump(ids,open('ids.pickle','wb'))
    np.savez('data_norm.npz',Xnorm,y_norm)
    # return df.iloc[1,2:].value