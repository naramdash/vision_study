import cv2
import numpy as np

def main():
    red = (0, 0, 255)
    green = (0, 255, 0)
    blue = (255, 0, 0)
    white = (255,255,255)

    # 1. Line and Rectangle

    # 300x300 크기
    # 3개의 채널을 가진 컬러 이미지
    # 각 채널은 uint8 타입 (0~255 범위의 정수값을 가짐)
    # zeros: 모든 픽셀 값을 0으로 초기화 (검은색 이미지)
    canvas = np.zeros((300, 300, 3), dtype="uint8")


    cv2.line(canvas, (0, 0), (300, 300), green)
    cv2.line(canvas, (300, 0), (0, 300), red)
    # 선 두께는 1픽셀로 설정
    cv2.rectangle(canvas, (10, 10), (60, 60), green, 1)
    # 선 두께는 2픽셀로 설정
    cv2.rectangle(canvas, (50, 200), (200, 225), red, 2)
    # 채워진 사각형을 그립니다. (선 두께를 -1로 설정)
    cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)

    cv2.imshow("Original", canvas)
    cv2.waitKey(0)

    # 2. Circle

    # 캔버스 초기화 (검은색 이미지)
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    # 원의 중심 좌표를 계산합니다.
    (centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

    # 0부터 175미만!!까지 25 간격으로 반지름을 증가시키며 원을 그립니다.
    for r in range(0, 175, 25):
        cv2.circle(canvas, (centerX, centerY), r, white, 1)

    cv2.imshow("Circles", canvas)
    cv2.waitKey(0)

    # 3. Filled Circles

    for _ in range(0, 25):
        # 무작위로 색상 값을 생성합니다.
        # numpy의 randint 함수를 사용하여 
        # 0부터 256미만의 무작위 정수
        # 숫자 3개의 튜플
        # 을 리스트로 반환
        color = np.random.randint(0, 256, size=(3,)).tolist()
        # 원의 중심 좌표를 무작위로 생성합니다.
        # 0부터 300미만의 무작위 정수 2개를 생성하여 (x, y) 좌표로 사용합니다.
        center = tuple(np.random.randint(0, 300, size=(2,)))
        # 원의 반지름을 무작위로 생성합니다.
        # 5부터 200미만의 무작위 정수를 생성하여 원의 반지름으로 사용합니다.
        radius = np.random.randint(5, 200)
        # 캔버스에 채워진 원을 그립니다.
        # OpenCV의 circle 함수에서 -1은 채움을 의미합니다.
        cv2.circle(canvas, center, radius, color, -1)
    
    cv2.imshow("Filled Circles", canvas)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()