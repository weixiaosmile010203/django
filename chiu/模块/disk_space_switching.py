import psutil
import shutil, os
#       机器分区池
disks = ['/mnt/sda/', '/mnt/sdc', '/mnt/sdd']

#       当前监控的磁盘
current = disks[0]


#       获取当前监控磁盘空间的百分比并且返回


def disk_usage_percent(current):
    percent = psutil.disk_usage(current).percent
    return percent


n = 0
for disk in disks:
    if disk_usage_percent(disk) > 60:
        n += 1
        print('磁盘空间将满，请切换磁盘')
        disk = disks[n]
        print('当前磁盘为', disk)
        print(disk + '空间为', disk_usage_percent(disk))
        os.system('ls %s' % disk)
    os.listdir('/mnt/sdb/data')
    shutil.move('/mnt/sdb/data',)

