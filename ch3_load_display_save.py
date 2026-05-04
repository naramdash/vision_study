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

    # 이미지를 창에 표시합니다.
    cv2.imshow("Image", image)
    # 키 입력을 기다렸다가 창을 닫습니다.
    # 참고: cv2.waitKey(0)은 키를 누를 때까지 무기한 대기합니다.
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 이미지를 새 파일로 저장합니다.
    cv2.imwrite("newimage.jpg", image)

if __name__ == "__main__":
    main()
