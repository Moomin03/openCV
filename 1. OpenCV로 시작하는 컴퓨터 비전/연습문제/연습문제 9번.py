import sys
import cv2 as cv
'''
    붓으로 그림을 그리는데 붓의 사이즈가 +를 누르면 1만큼 커지고
    -를 누르면 1만큼 작아지는 프로그램을 만들어라
'''

img = cv.imread('/home/admin/Develop/openCV/사진 파일/cat.jpg')
if img is None:
    sys.exit('해당 파일은 존재하지 않습니다.')
cv.imshow('mainwindow', img)
brush_size = 5
def draw(event, x, y, flags, params):
    if event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), brush_size, (255, 0, 0), 2)
    cv.imshow('mainwindow', img)
cv.setMouseCallback('mainwindow', draw)
while True:
    if cv.waitKey(1)==ord('+'):
        brush_size+=1
    elif cv.waitKey(1)==ord('-'):
        brush_size-=1
    elif cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break