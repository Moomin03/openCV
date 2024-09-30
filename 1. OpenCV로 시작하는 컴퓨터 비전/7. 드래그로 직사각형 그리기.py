import sys
import cv2 as cv

img = cv.imread('/home/admin/Develop/openCV/사진 파일/cat.jpg')
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

def draw(event, x, y, flags, param):
    global ix, iy
    if event==cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y
    elif event==cv.EVENT_LBUTTONUP:
        cv.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 2)
    cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)
cv.setMouseCallback('Drawing', draw)
while True:
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break