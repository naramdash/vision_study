import argparse
import cv2

def main():
    """
    입력받은 이미지를 읽고, 기본 정보를 출력한 뒤 화면에 표시하고 저장하는 메인 함수입니다.
    """

    # 명령줄에서 이미지 경로를 입력받을 수 있도록 인자 파서를 설정합니다.
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image", required=True, help="Path to the input image")

    # 사용자가 전달한 명령줄 인자를 파싱합니다.
    args = vars(parser.parse_args())
    image_path = args["image"]

    # 지정한 경로에서 이미지를 읽어옵니다.
    image = cv2.imread(image_path)
    if image is None:
        parser.error(f"Cannot read image file: {image_path}")

    # 이미지의 가로, 세로, 채널 수 정보를 출력합니다.
    print(f"width: {image.shape[1]} pixels")
    print(f"height: {image.shape[0]} pixels")
    print(f"channels: {image.shape[2]}")

    ### Chapter 4: Getting and Setting Pixel Values

    # 가장 왼쪽 위 픽셀의 색상 값을 읽어옵니다.
    # image의 픽셀은 2차원 배열처럼 접근할 수 있다. (matrix 형태)
    # numpy와의 연관이 있는 부분
    #
    # OpenCV는 BGR 순서로 색상 값을 저장하므로, (b,g,r) 순서로 값을 읽어옵니다.
    # 까먹으면 안되는 부분
    (b,g,r) = image[0,0]
    print(f"Getting Pixel at (0,0) - Red: {r}, Green: {g}, Blue: {b}")

    # 가장 왼쪽 위 픽셀의 색상 값을 빨간색으로 변경합니다.
    image[0,0] = (0,0,255)

    # 변경된 픽셀의 색상 값을 다시 읽어옵니다.
    (b,g,r) = image[0,0]
    print(f"Re-Getting Pixel at (0,0) - Red: {r}, Green: {g}, Blue: {b}")


    # 이미지의 왼쪽 위 100x100 픽셀 영역을 가져와서 화면에 표시합니다.
    # numpy의 2차원 배열 슬라이싱을 활용하여 영역을 선택할 수 있습니다.
    corner = image[0:100, 0:100]
    cv2.imshow("Corner", corner)

    # 왼쪽 위 100x100 픽셀 영역의 색상 값을 초록색으로 변경합니다.
    image[0:100, 0:100] = (0, 255, 0)
    cv2.imshow("Updated", image)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()