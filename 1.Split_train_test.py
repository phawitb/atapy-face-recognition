import os
from sklearn.model_selection import StratifiedShuffleSplit
from shutil import copyfile

TEST_SIZE = 0.2
data_folder = 'original_data'
output_folder = 'data'

train_folder = os.path.join(output_folder, 'train')
test_folder = os.path.join(output_folder, 'test')

os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

classes = [d for d in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder, d))]

sss = StratifiedShuffleSplit(n_splits=1, test_size=TEST_SIZE, random_state=42)

for class_name in classes:
    class_path = os.path.join(data_folder, class_name)
    
    files = [f for f in os.listdir(class_path) if os.path.isfile(os.path.join(class_path, f))]
    
    labels = [class_name] * len(files)
    
    for train_index, test_index in sss.split(files, labels):
        for i in train_index:
            src_path = os.path.join(class_path, files[i])
            dst_path = os.path.join(train_folder, class_name, files[i])
            os.makedirs(os.path.join(train_folder, class_name), exist_ok=True)
            copyfile(src_path, dst_path)
        
        for i in test_index:
            src_path = os.path.join(class_path, files[i])
            dst_path = os.path.join(test_folder, class_name, files[i])
            os.makedirs(os.path.join(test_folder, class_name), exist_ok=True)
            copyfile(src_path, dst_path)
