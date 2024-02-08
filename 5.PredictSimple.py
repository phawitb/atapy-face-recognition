from face_recognition import FaceRecognition
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import classification_report, roc_curve, precision_recall_curve, roc_auc_score, accuracy_score
# import matplotlib.pyplot as plt
# import os
# import glob
# import pandas as pd
# import random
# import numpy as np
import cv2
# import base64
# from tqdm import tqdm
# import requests
# from pprint import pprint
# import shutil
import json
# from PIL import ImageFont, ImageDraw, Image

def prediction(fr,img):
    result = fr.predict(img, threshold=0.3)
    R = []
    for r in result['predictions']:
        r['person_name'] = class_dict[r['person']]
        R.append(r)

    return R


CLASS_DICT_PATH = 'data/train/class_dict.json' 
TEST_IMAGE_FILE = "data/train/class2/img1.jpg" #"./Datasets/Test2/"
MODEL_PATH = "model_v1.pkl"
CONFIDENCE = 0.7

with open(CLASS_DICT_PATH, 'r') as file:
    class_dict = json.load(file)

fr = FaceRecognition()
fr.load(MODEL_PATH)

#----loop-----
img =  cv2.imread(TEST_IMAGE_FILE)
results = prediction(fr,img)

print('TEST_IMAGE_FILE : ',TEST_IMAGE_FILE)
print('RESULT : ',results)



