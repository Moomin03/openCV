import sys
import cv2 as cv
import math
'''
    왼쪽은 직사각형을 그리고, 오른쪽은 클릭했을 때가 중심이고
    오른쪽 버튼을 놓은 곳이 원주다.
'''

img = cv.imread('/home/admin/Develop/openCV/사진 파일/cat.jpg')
if img is None:
    sys.exit('존재하지 않는 파일입니다.')
cv.imshow('mainwindow', img)

def draw(event, x, y, flags, params):
    global x1, y1
    if event==cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img, (x, y), (x+100, y+100), (255, 0, 0), 2)
    elif event==cv.EVENT_LBUTTONDOWN:
        x1, y1 = x, y
    elif event==cv.EVENT_LBUTTONUP:
        cv.circle(img, (x1, y1), int(math.sqrt((x1-x)**2+(y1-y)**2)), (0, 255, 0), 2)
    cv.imshow('mainwindow', img)
cv.setMouseCallback('mainwindow', draw)

cv.waitKey()
cv.destroyAllWindows()