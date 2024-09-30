import sys
import cv2 as cv
import numpy as np
'''
    문제 : 0.1 ~1.0으로 축소한 영상 10개를 서로 다른 윈도우에
    디스플레이 하시오
'''

img = cv.imread('/home/admin/Develop/openCV/사진 파일/cat.jpg')
rate = np.arange(0.1, 1.1, 0.1)
for i in rate:
    resized_img = cv.resize(img, dsize=(0, 0), fx=i, fy=i)
    cv.imshow(f'{i} rate file!', resized_img)
cv.waitKey()
cv.destroyAllWindows()