import sys
import cv2 as cv
'''
    문제 : 서로다른 영상 2개를 img1과 img2에 저장하고
    서로 다른 윈도우에 디스플레이하시오!
'''

img1 = cv.imread('/home/admin/Develop/openCV/사진 파일/cat.jpg')
img2 = cv.imread('/home/admin/Develop/openCV/사진 파일/cat_gray.jpg')
if img1 is None or img2 is None:
    sys.exit('해당 파일이 존재하지 않습니다.')
cv.imshow('img1', img1)
cv.imshow('img2.', img2)
cv.waitKey()
cv.destroyAllWindows()