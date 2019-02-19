#!/usr/bin/python
# -*- coding: UTF-8 -*-
import psutil

disks = psutil.disk_partitions()
for i in disks:
    disk = psutil.disk_usage(i.mountpoint)
    print(r'磁盘 %s 占用空间百分比 %s'%(i.mountpoint ,disk.percent))
