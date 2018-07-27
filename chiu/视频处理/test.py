import cv2 as cv

cap = cv.VideoCapture(r"D:\迅雷下载\Ready.Player.One.2018.1080p.WEB.h264-WEBTiFUL[rarbg]\ready.player.one.2018.1080p.web.h264-webtiful.mkv")
cap.set(cv.CAP_PROP_POS_FRAMES,131411)
a,b=cap.read()
cv.imshow('b',b)
print(int(cap.get(cv.CAP_PROP_FRAME_COUNT)))
cv.waitKey(10000)

