import os
import json

DATA_FLODER = "data/train"

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

