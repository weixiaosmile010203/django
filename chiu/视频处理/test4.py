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


def get_frame(fileOpen):
    vc = cv2.VideoCapture(fileOpen)
    fram = 0.01
    counts = 1
    if vc.isOpened():
        ret, frame = vc.read()
    else:
        ret = False
    while ret:
        vc.set(cv2.CAP_PROP_POS_FRAMES, int(counts))
        ret, frame = vc.read()
        if fram < 1:
            name = os.path.splitext(fileOpen)[1] + str(counts) + '.jpg'
            os.chdir(os.path.dirname(fileOpen))
            cv2.imwrite(name, frame)
            counts = (vc.get(cv2.CAP_PROP_FRAME_COUNT)) * fram
            fram += 0.02
            print(int(counts))
        else:
            cv2.waitKey(1)
            break
    vc.release

local_path = r"G:\Disk_File\Start_Here_Mac.app\Contents\Frameworks\mimi"

for fileOpen in feach_path(local_path):
    get_frame(fileOpen)
