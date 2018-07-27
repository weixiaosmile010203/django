import os
import shutil

for path, folder, files in os.walk(r"G:\Disk_File\Start_Here_Mac.app\Contents\Frameworks\mimi"):
    for file in files:
        if file.endswith('.jpg'):
            os.unlink(os.path.join(path,file))