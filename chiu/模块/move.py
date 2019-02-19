# -*- coding: UTF-8 -*-
import psutil
import os

#       机器分区池
disks = ['/mnt/sdb', '/mnt/sdc']

#       获取当前监控磁盘空间的百分比并且返回


def disk_usage_percent(current):
    percent = psutil.disk_usage(current).percent
    return percent


for disk in disks:
    if disk_usage_percent(disk) > 90:
        pass
    else:
        os.system('mv /root/data/* %s/data/' % disk)
        break
