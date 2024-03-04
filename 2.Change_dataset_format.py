import os
import json
import shutil

DATA_PATH = 'data'

def copy_folder(source_folder, destination_folder):
    try:
        # Copy the entire folder and its contents to the destination
        shutil.copytree(source_folder, destination_folder)
        print(f"Folder '{source_folder}' successfully copied to '{destination_folder}'.")
    except Exception as e:
        print(f"Error copying folder: {e}")

def change_file_name(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File name changed successfully: {old_name} -> {new_name}")
    except FileNotFoundError:
        print(f"Error: File not found - {old_name}")
    except Exception as e:
        print(f"Error: {e}")

def change_class_name(DATA_FLODER):
    def change_folder_name(old_name, new_name):
        try:
            os.rename(old_name, new_name)
            print(f"Folder name changed from '{old_name}' to '{new_name}' successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    folders = [folder for folder in os.listdir(DATA_FLODER) if os.path.isdir(os.path.join(DATA_FLODER, folder))]
    folders

    class_dict = {}
    for i,f in enumerate(folders):
        change_folder_name(f'{DATA_FLODER}/{f}', f'{DATA_FLODER}/class{i}')
        class_dict[f'class{i}'] = f
        
    with open(f'{DATA_FLODER}/class_dict.json', 'w') as json_file:
        json.dump(class_dict, json_file, indent=4)

def ChangeDatasetFormat(ORIGINAL_DATE,DATA_FLODER):
    # ORIGINAL_DATE = 'data/test'
    # DATA_FLODER = "data/test"
    #copy original floder to data floder for train
    copy_folder(ORIGINAL_DATE, DATA_FLODER)

    #change class name and save class_dict.json
    if 'class_dict.json' not in os.listdir(DATA_FLODER):
        change_class_name(DATA_FLODER)
        print('Change class name sucuessful')
    else:
        print('Already change class name')
    with open(f'{DATA_FLODER}/class_dict.json', 'r') as json_file:
        data = json.load(json_file)
    print('clasd_dict = ',data)

    #change img file name
    for f in [x for x in os.listdir(DATA_FLODER) if not '.' in x]:
        for i,ff in enumerate(os.listdir(f'{DATA_FLODER}/{f}')):
            old_file = f'{DATA_FLODER}/{f}/{ff}'
            xx = old_file.split('.')[-1]
            change_file_name(old_file,f'{DATA_FLODER}/{f}/img{i}.{xx}')

#----------------------------
folders = [f for f in os.listdir(DATA_PATH) if os.path.isdir(os.path.join(DATA_PATH, f))]

for f in folders:
    ORIGINAL_DATE = f'data/{f}'
    DATA_FLODER = f"data/{f}"
    ChangeDatasetFormat(ORIGINAL_DATE,DATA_FLODER)

# ORIGINAL_DATE = 'data/test'
# DATA_FLODER = "data/test"
# ChangeDatasetFormat(ORIGINAL_DATE,DATA_FLODER)