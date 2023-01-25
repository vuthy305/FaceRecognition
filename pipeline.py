import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import pickle
import cv2
import pickle
import matplotlib.image as mat_image
from PIL import Image



# # test data
# test_data_path = 'sal.jpg'
# color = 'bgr'
# # step-1: read image
# img = cv2.imread(test_data_path)


def pipeline_model(img,color='rgb'):
    labels = {}
    ids = {}
    font = cv2.FONT_HERSHEY_SIMPLEX
    with open("label.pickle","rb") as f:
        og_labels = pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}
    with open('ids.pickle','rb') as f:
        og_labels = pickle.load(f)
        ids = {v:k for k,v in og_labels.items()}

    # load all the models
    haar = cv2.CascadeClassifier("Haarcascade/haarcascade_frontalface_default.xml")
    # pickle files
    mean  = pickle.load(open('mean_preprocess.pickle','rb'))
    model_svm  = pickle.load(open('model_svm_pickle.pickle','rb'))
    model_pca  = pickle.load(open('pca.pickle','rb'))
    model_nav  = pickle.load(open('model_gussianNaviBayes_pickle.pickle','rb'))


    # print('Model loaded sucessfully')
    # step-2: convert into gray scale
    if color == 'bgr':
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    # step-3: crop the face (using haar cascase classifier)
    # faces = haar.detectMultiScale(gray,1.5,3)
    faces = haar.detectMultiScale(gray,1.3,5)
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) # drawing rectangle
        roi = gray[y:y+h,x:x+w] # crop image
        # step - 4: normalization (0-1)
        roi = roi / 255.0
        # step-5: resize images (100,100)
        if roi.shape[1] > 100:
            roi_resize = cv2.resize(roi,(100,100),cv2.INTER_AREA)
        else:
            roi_resize = cv2.resize(roi,(100,100),cv2.INTER_CUBIC)
        # step-6: Flattening (1x10000)
        roi_reshape = roi_resize.reshape(1,100*100) # 1,-1
        # step-7: subptract with mean
        roi_mean = roi_reshape - mean
        # print(roi_mean.shape)
        # step -8: get eigen image
        eigen_image = model_pca.transform(roi_mean)
        # step -9: pass to ml model (svm)
        # results = model_svm.predict_proba(eigen_image)[0]
        results = model_nav.predict_proba(eigen_image)[0]
        # step -10:
        predict = results.argmax() # 0 or 1 
        score = results[predict]
        # step -11:
        text = "%s : %0.2f"%(labels[predict],score)
        id = ids[predict]
        cv2.putText(img,text+"_"+id,(x,y),font,1,(0,255,0),2)
        print(text)
    return img

# color = 'bgr'
# # step-1: read image
# img = Image.open(test_data_path) # rgb
# # step2: convert into array
# img = np.array(img)
# # step3: pass to pipeline model
# img = pipeline_model(img)
# plt.imshow(img)
# plt.show()
# # print(mean)

# pipeline_model(img)