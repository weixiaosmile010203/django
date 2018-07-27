import cv2
cap = cv2.VideoCapture(r'D:\迅雷下载\Westworld.S02E05.Akane.No.Mai.720p.AMZN.WEBRip.DDP5.1.x264-NTb[rarbg]\Westworld.S02E05.Akane.No.Mai.720p.AMZN.WEB-DL.DDP5.1.H.264-NTb.mkv')
#       判断视频是否打开
print(cap.isOpened())
#       获取视频的帧数
print( cap.get(cv2.CAP_PROP_FPS))
#       获取视频的宽度
print(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
#       获取视频的高度
print(int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#       获取视频的所有的帧数
print(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
