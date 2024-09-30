import sys
import cv2 as cv
'''
    왼쪽 마우스를 누르면 직사각형을, 오른쪽 마우스를 누르면
    원을 그리는 프로그램을 만드시오.
'''

img = cv.imread('/home/admin/Develop/openCV/사진 파일/cat.jpg')
if img is None:
    sys.exit('해당 파일이 존재하지 않습니다.')

cv.imshow('mainwindow', img)
def draw(event, x, y, flags, params):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x, y), (x+100, y+100), (255, 0, 0), 2)
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x, y), 50, (0, 255, 0), 2)
    cv.imshow('mainwindow', img)
# 중요하다 외우자!
cv.setMouseCallback('mainwindow', draw)
cv.waitKey()
cv.destroyAllWindows()