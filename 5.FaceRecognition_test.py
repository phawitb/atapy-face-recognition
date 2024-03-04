from face_recognition import FaceRecognition
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_curve, precision_recall_curve, roc_auc_score, accuracy_score
import matplotlib.pyplot as plt
import os
import glob
import pandas as pd
import random
import numpy as np
import cv2
import base64
from tqdm import tqdm
import requests
from pprint import pprint
import shutil
import json
from PIL import ImageFont, ImageDraw, Image

def list_allfiles(startpath):
    F = []
    for root, dirs, files in os.walk(startpath):
        for file in files:
            f = os.path.join(root, file)
            if f.split('.')[-1] in ['jpg','jpeg', 'bmp', 'png', 'gif']:
                F.append(f)
    return F

#Settings
CLASS_DICT_PATH = 'data/train/class_dict.json' 
TEST_IMAGE_PATH = "data/test" #"./Datasets/Test2/"
MODEL_PATH = "model_v1.pkl"
SAVE_PATH = "Result"
CONFIDENCE = 0.6

fontpath = 'angsana.ttc'
font = ImageFont.truetype(fontpath, 32)

with open(CLASS_DICT_PATH, 'r') as file:
    class_dict = json.load(file)
if not os.path.exists(SAVE_PATH):
    os.mkdir(SAVE_PATH)
else:    
    shutil.rmtree(SAVE_PATH)
    os.mkdir(SAVE_PATH)
SAVE_PATH = os.path.join(os.getcwd(), SAVE_PATH)

# Testing
fr = FaceRecognition()
fr.load(MODEL_PATH)

# file_names = [fn for fn in os.listdir(TEST_IMAGE_PATH) if any(fn.endswith(ext) for ext in ['jpg','jpeg', 'bmp', 'png', 'gif'])]
file_names = list_allfiles(TEST_IMAGE_PATH)
for file in file_names:
    # img_path = os.path.join(TEST_IMAGE_PATH,file)
    img_path = file
    img =  cv2.imread(img_path)

    result = fr.predict(img, threshold=0.3)

    print(img_path,result['predictions'])

    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    # draw.text((text_x, text_y),  class_dict[p['person']], font = font, fill = (0,255,0))

    fact_person = [x for x in img_path.split('/') if 'class' in x][0]
    draw.text((0, 0),  class_dict[fact_person], font = font, fill = (0,255,0))
    img = np.array(img_pil)

    for p in result['predictions']:
        if p['confidence'] > CONFIDENCE:
            #drow box
            left,top,right,bottom = p['box']
            img = cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

            #Add Thai text above the bounding box
            # fontpath = thai_font 
            # font = ImageFont.truetype(fontpath, 32)
            text_x = left + 5 #(left + right) // 2
            text_y = top - 5 #top - 5  # Adjust this value based on your preference

            predict_person = p['person']
            if fact_person == predict_person:
                color = (0,255,0)
            else:
                color = (255,0,0)

            img_pil = Image.fromarray(img)
            draw = ImageDraw.Draw(img_pil)
            draw.text((text_x, text_y),  class_dict[p['person']], font = font, fill = color)
            draw.text((0, 0),  class_dict[p['person']], font = font, fill = color)
            img = np.array(img_pil)

            # Add text above the bounding box
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # font_scale = 0.9
            # font_thickness = 2
            # text_size = cv2.getTextSize(p['person'], font, font_scale, font_thickness)[0]
            # text_x = (left + right - text_size[0]) // 2
            # text_y = top - 5  # Adjust this value based on your preference
            # img = cv2.putText(img, class_dict[p['person']], (text_x, text_y), font, font_scale, (0, 255, 0), font_thickness)
        
    cv2.imwrite(os.path.join(SAVE_PATH,'Output_'+file.replace('/','_')), img)

