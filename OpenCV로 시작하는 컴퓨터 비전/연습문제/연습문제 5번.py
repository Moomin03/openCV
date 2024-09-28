import sys
import cv2 as cv
'''
    사용자가 g를 클릭하면 명앙 영상을 디스플레이하고,
    사용자가 c를 입력하면 다시 칼라 영상을 디스플레이하도록 하시오.
'''

img = cv.imread('/home/admin/Develop/openCV/사진 파일/cat.jpg')
if img is None:
    sys.exit('해당 파일이 존재하지 않습니다.')

change_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.namedWindow('MAINBOARD')
cv.imshow('MAINBOARD', img)
while True:
    if cv.waitKey(1)==ord('g'):
        cv.imshow('MAINBOARD', change_img)
    elif cv.waitKey(1)==ord('c'):
        cv.imshow('MAINBOARD', img)
    elif cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break