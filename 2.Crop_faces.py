import os
from ultralytics import YOLO
import cv2
import numpy as np

def detection_img(img,border_percen):
    # border_percen = 0.1 #for add border 10%
    results = model.predict(source=img)
    bboxs = []
    for r in results:
        boxes = r.boxes
        for i,box in enumerate(boxes):
            B = box.xyxy.tolist()[0]
            left, top, right, bottom = [int(x) for x in B]
            bboxs.append((int(left*(1-border_percen)), int(top*(1-border_percen)), int((1+border_percen)*right), int((1+border_percen)*bottom)))

    return bboxs

def crop_img(img,bboxs):
    cropped_imgs = []
    for i,b in enumerate(bboxs):
        left, top, right, bottom = b
        cropped_img = img[top:bottom, left:right]
        
        cropped_imgs.append(cropped_img)
    return cropped_imgs

def draw_bbox(img,bboxs):
    bbox_imgs = []
    for i,b in enumerate(bboxs):
        (left, top, right, bottom) = b
        
        text = 'sdvsdvds'
        
        # Draw bounding box
        img_bboxed = cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

        # Add text above the bounding box
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        font_thickness = 1
        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]

        text_x = (left + right - text_size[0]) // 2
        text_y = top - 5  # Adjust this value based on your preference

        img_bboxed = cv2.putText(img_bboxed, text, (text_x, text_y), font, font_scale, (0, 255, 0), font_thickness)
        
        bbox_imgs.append(img_bboxed)
        
    return bbox_imgs
    
model = YOLO('yolov8n-face.pt')
source_path = 'data/train'
output_path = 'data/train' #'output_data2'
border_percen = 0.2 #for add border face_croped 0.1 for 10%

folders = [folder for folder in os.listdir(source_path) if os.path.isdir(os.path.join(source_path, folder))]

for folder in folders:
    directory_path = f'{source_path}/{folder}'
    files = [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]
    files = [x for x in files if x.split('.')[-1] in ['jpg','jpeg', 'bmp', 'png', 'gif']]

    print('\n',directory_path,">>>",len(files))
    if not os.path.exists(directory_path.replace(source_path,output_path)):
        os.makedirs(directory_path.replace(source_path,output_path))

    for file in files:
        img_path = f'{directory_path}/{file}'
        img_src = cv2.imread(img_path)
        
        bboxs = detection_img(img_src,border_percen)

        out_imgs = crop_img(img_src,bboxs)
        # out_imgs = draw_bbox(img_src,bboxs)
    
        for out_img in out_imgs:
            output_file_path = img_path.replace(source_path,output_path)
    
            print('output_file_path',output_file_path)
            cv2.imwrite(output_file_path, out_img)


