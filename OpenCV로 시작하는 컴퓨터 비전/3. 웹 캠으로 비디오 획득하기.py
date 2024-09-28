import cv2 as cv
import sys

# 첫번째 인수로 웹 캠 번호를 지정하는데, 웹 캠이 하나인 경우에 0을 할당
cap = cv.VideoCapture(0)

if not cap.isOpened():
    sys.exit('카메라 연결 실패')
    
while True:
    # read함순느 호춣한 순간의 영상 한장, 즉 프레임을 획득하고 성공 여부와 프레임을 반환
    ret, frame = cap.read()
    
    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break
    
    cv.imshow('Video display', frame)
    
    key = cv.waitKey(1)
    if key==ord('q'):
        break
# 카메라와 연결 종료
cap.release()
cv.destroyAllWindows()