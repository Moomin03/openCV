import cv2 as cv
import sys

img = cv.imread('/home/admin/Develop/openCV/사진 파일/cat.jpg')
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

def draw(event, x, y, flags, param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x,y), (x+200, y+200), (255, 0, 0), 2)
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img, (x, y), (x+100, y+100), (0, 0, 255), 2)
    # 이거 안쓰면 화면에 표시 안됨.
    cv.imshow('Drawing', img)
# 쓰지 않아도 되는 것 같은데 왜 쓰는거지?
cv.namedWindow('Drawing')
# 쓰지 않아도 상관 없지만 안쓰면 바로 안나타나서 써야한다.
cv.imshow('Drawing', img)
cv.setMouseCallback('Drawing', draw)

while True:
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break