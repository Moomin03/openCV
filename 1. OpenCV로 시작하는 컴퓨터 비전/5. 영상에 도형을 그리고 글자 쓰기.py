import cv2 as cv
import sys

img = cv.imread('/home/admin/Develop/openCV/사진 파일/cat.jpg')
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.rectangle(img, (123, 0), (616, 521), (0, 0, 255), 2)
cv.rectangle(img, (267, 304), (378, 356), (255, 0, 0), 2)
cv.rectangle(img, (448, 248), (528, 306), (255, 0, 0), 2)
cv.imshow('Cat image', img)
cv.waitKey()
cv.destroyAllWindows()