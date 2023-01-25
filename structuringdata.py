import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import cv2 as cv
from PIL import Image
import os,pickle

def getThePathAndLabel():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR,"Facedatabase")

    paths = []
    labels = []
    ids = []

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root,file) 
                paths.append(path)
                label = os.path.basename(os.path.dirname(path))
                idAndName = label.split("-")
                labels.append(idAndName[1])
                ids.append(idAndName[0])
    return labels,paths,ids
def get_img(path_to_image):
    try:
        pil_image = Image.open(path_to_image).convert("L")
        image_array = np.array(pil_image,"uint8")
        return image_array.flatten()
        # return image_array
    except:
        return None
def createDataFrameForTrain():
    labels,paths,ids = getThePathAndLabel()
    df = pd.DataFrame(data=labels,columns=['label'])
    df['id'] = ids
    df['path'] = paths
    df['structure_data'] = df['path'].apply(get_img)
    df1 = df['structure_data'].apply(pd.Series)
    df_final = pd.concat((df['id'],df['label'],df1),axis=1)
    pickle.dump(df_final,open('all_data_image.pickle','wb'))
    # return df_final

# plt.imshow(get_img("Facedatabase/0001-Vothy Vysal/Vothy Vysal0.jpg"))
# plt.show()