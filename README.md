# Face-Recognition
### Face Recognition Using keras_FaceNet

## Download source code
```
git clone https://github.com/phawitb/atapy-face-recognition.git
```




## Install Package
#### Use anaconda
```python
create anaconda envirionment
conda create -n atapyfacerecognition python=3.9
conda activate atapyfacerecognition
```
#### Use anaconda from atapy-face-recognition.yml
```
conda env create -f atapy-face-recognition.yml
conda activate atapyfacerecognition
```
#### Use pip 
```
cd atapy-face-recognition
pip install -r requirements.txt
```

## Prepare Data
#### 1.Download Data 
```
cd atapy-face-recognition
python 0.Download_data_from_google_drive.py
```
#### 2.Extract data.zip file >> floder original_data
#### 3.Split data to train test
```
python 1.Split_train_test.py
```
#### 4.Change dataset format
```
python 2.Change_dataset_format.py
```
```
data
├── train
│    ├── class0
│		├── img0.jpg
│		├── img1.jpg
│		├── img2.jpg
│		...
│	├── class1
│		├── img0.jpg
│		├── img1.jpg
│		├── img2.jpg
│		...
│	├── class_dict.json
│		...
│	├── class
├── test
    ├── class0
		├── img0.jpg
		├── img1.jpg
		├── img2.jpg
		...
	├── class1
		├── img0.jpg
		├── img1.jpg
		├── img2.jpg
		...
	├── class
		...
	├── class_dict.json

```
#### 5.Crop faces in images
```
python 3.Crop_faces.py
```
#### 6.Delete incorrect face image in each floder

## Train
```
python 4.FaceRecognition_train.py
```
#### model output >> model_v1.pkl
## Test
#### test all images in data/test >> Result
```
python 5.FaceRecognition_test.py
```
#### test basic 1 image
```
python 6.PredictSimple.py
```

#### note
```
conda env export -n atapy-face-recognition -f atapy-face-recognition.yml
```

