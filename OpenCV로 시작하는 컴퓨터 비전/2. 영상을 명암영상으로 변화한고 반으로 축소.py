import cv2 as cv
import sys

# 이미지 불러오기
img = cv.imread('/home/admin/Develop/openCV/사진 파일/cat.jpg')
# 이미지 존재하지 않으면 오류 반환
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
# cvtColor 함수를 사용해서 img를 cv.COLOR_BGR2GRAY로 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# desize가 0인 경우 fx와 fy를 따른다.
gray_small = cv.resize(gray, dsize=(0, 0), fx=0.5, fy=0.5)
# 이미지 저장
cv.imwrite('/home/admin/Develop/openCV/사진 파일/cat_gray.jpg', gray)
cv.imwrite('/home/admin/Develop/openCV/사진 파일/cat_gray_small.jpg', gray_small)
# 이미지 표현
cv.imshow('Color image', img)
cv.imshow('Gray image', gray)
cv.imshow('Gray image small', gray_small)
# 기본 구조
cv.waitKey()
cv.destroyAllWindows()