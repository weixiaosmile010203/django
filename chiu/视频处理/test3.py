import os
import cv2

def feach_path(local_path):
    file_list = []
    for path, folder, files in os.walk(local_path):
        for file in files:
            if file.endswith('.mp4') or file.endswith('.mkv'):
                file_path = os.path.join(path,file)
                file_list.append(file_path)

    return file_list


def get_frame(fileOpen, timeF):
    vc = cv2.VideoCapture(fileOpen)
    c = 1000

    if vc.isOpened():
        ret, frame = vc.read()
    else:
        ret = False
    while ret:
        ret, frame = vc.read()
        if c % timeF == 0:
            name = os.path.splitext(fileOpen)[1] + str(c) + '.jpg'
            os.chdir(os.path.dirname(fileOpen))
            cv2.imwrite(name, frame)
        c += 1
        cv2.waitKey(1)
    vc.release

local_path = r"G:\Disk_File\Start_Here_Mac.app\Contents\Frameworks\mimi"

for fileOpen in feach_path(local_path):
    get_frame(fileOpen, 5000)
