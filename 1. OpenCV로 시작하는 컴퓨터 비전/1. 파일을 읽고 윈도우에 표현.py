import cv2 as cv
import sys

# 이미지 불러오기
img = cv.imread('/home/admin/Develop/openCV/사진 파일/cat.jpg')

# 파일이 존재하지 않을 시에 오류 반환
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

# 사진을 표현하는 홤녀 구성, 앞에 나오는 파라미터는 창 이름
cv.imshow('Image Display', img)

# img 타입
print(type(img))
print(img.shape)

# 0, 0과 1, 1의 화솟값
print(img[0, 0, 0], img[0, 0, 1], img[0, 0, 2])
print(img[0, 1, 0], img[0, 1, 1], img[0, 1, 2])

# waitKey 함수는 키도의 키가 눌릴 때까지 기다리다가, 키가 눌리면 해당 키의 유니코드 값을 반환
cv.waitKey()
cv.destroyAllWindows()