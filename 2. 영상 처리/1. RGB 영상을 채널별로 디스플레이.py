import cv2 as cv
import sys

img = cv.imread('/home/admin/Develop/openCV/사진 파일/cat.jpg')
if img is None:
    sys.exit('해당 파일이 존재하지 않습니다.')

cv.imshow('original_RGB', img)
# 사진 4분할
cv.imshow('Upper Left Half', img[:img.shape[0]//2, :img.shape[1]//2, :])
cv.imshow('Upper Right Half', img[:img.shape[0]//2, img.shape[1]//2:, :])
cv.imshow('Lower Left Half', img[img.shape[0]//2:, :img.shape[1]//2, :])
cv.imshow('Lower Right Half', img[img.shape[0]//2:, img.shape[1]//2:, :])
# 중앙 묘사
cv.imshow('Center Half', img[img.shape[0]//4:3*img.shape[0]//4, img.shape[1]//4:3*img.shape[1]//4,:])
# 각 채널 별 묘사
cv.imshow('R channel', img[:, :, 2])
cv.imshow('G channel', img[:, :, 1])
cv.imshow('B channel', img[:, :, 0])

cv.waitKey()
cv.destroyAllWindows()