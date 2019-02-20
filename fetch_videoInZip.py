
import os
import zipfile
import sys


def unzip(zip_path,unzip_path):
    try:
        f = zipfile.ZipFile(zip_path,'r')
        for file in f.namelist():
            file_suffix = os.path.splitext(file)[-1]
            if file_suffix == '.mp4' or file_suffix == '.mkv' or file_suffix == '.avi':
                f.extract(file,unzip_path)
        f.close
    except:
        print('Error file not is ziptype')



def zip_list(files_path):
    file_list = []
    for root, folder, files in os.walk('./'):
        for file in files:
            file_list.append(os.path.join(root,file))
    return file_list

zipfiles = zip_list('./')
for zip_path in zipfiles:
    print(zip_path)
    unzip(zip_path, './')



