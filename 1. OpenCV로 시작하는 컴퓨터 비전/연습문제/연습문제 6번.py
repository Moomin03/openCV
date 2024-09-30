import sys
import cv2 as cv
'''
    직사각형 왼쪽 위에 laugh라 써넣었다. laugh를 직사각형에서 조금 떨어뜨려 표시하고
    laugh 문자열이 화살표로 직사각형을 가리키도록 수정하시오.
'''

img = cv.imread('/home/admin/Develop/openCV/사진 파일/cat.jpg')
if img is None:
    sys.exit('파일이 존재하지 않습니다.')

cv.rectangle(img, (255, 379), (568, 568), (255, 0, 0), -1)
cv.putText(img, 'laugh', (255, 124), 5, 2, (0, 0, 255), 2)
cv.arrowedLine(img, (400, 124), (400, 379), (0, 255, 0), 2)
cv.imshow('mainwindow', img)
cv.waitKey()
cv.destroyAllWindows()