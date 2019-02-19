import os
lists = []
import shutil
# for path, folder, files in os.walk(r'G:\Disk_File\Start_Here_Mac.app\Contents\Frameworks\mimi'):
#     for file in files:
#         if file.endswith('mp4'):
#             lists.append(file)
# print(len(lists))
path = os.listdir(r'G:\Disk_File\Start_Here_Mac.app\Contents\Frameworks\mimi')
print(path)
for mp4 in path:
    if mp4.endswith('.mp4') or mp4.endswith('.mkv'):
        print(mp4)
        lists.append(mp4)
        dir_name = os.path.splitext(mp4)[0]
        if os.path.exists(r'G:\Disk_File\Start_Here_Mac.app\Contents\Frameworks\mimi\{0}'.format(dir_name)):
            shutil.move(r'G:\Disk_File\Start_Here_Mac.app\Contents\Frameworks\mimi\{0}'.format(mp4),
                            r'G:\Disk_File\Start_Here_Mac.app\Contents\Frameworks\mimi\{0}\\'.format(dir_name))
        else:
            os.makedirs(r'G:\Disk_File\Start_Here_Mac.app\Contents\Frameworks\mimi\{0}'.format(dir_name))
            shutil.move(r'G:\Disk_File\Start_Here_Mac.app\Contents\Frameworks\mimi\{0}'.format(mp4),
                    r'G:\Disk_File\Start_Here_Mac.app\Contents\Frameworks\mimi\{0}\\'.format(dir_name))

print(len(lists))