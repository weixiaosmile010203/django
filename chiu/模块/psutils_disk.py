import psutil



#       磁盘使用情况
disk_used = psutil.disk_usage('c://')
print('磁盘空间所有信息\n', disk_used)
print('总磁盘空间',disk_used.total)
print('使用的磁盘空间', disk_used.used)
print('剩余的磁盘空间', disk_used.free)
print('磁盘使用百分比', disk_used.percent)

if disk_used.percent > 60:
    print('磁盘空间达到%s' % disk_used.percent)
    print('将要切换磁盘')