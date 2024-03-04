import gdown

#download file from google drive https://drive.google.com/file/d/10sWDaxARKFadt4qw4fReQ2vX2YzZmdXY/view?usp=drive_link
file_id = '10sWDaxARKFadt4qw4fReQ2vX2YzZmdXY'
output_file = 'data.zip'
url = f'https://drive.google.com/uc?id={file_id}'
gdown.download(url, output_file, quiet=False)
