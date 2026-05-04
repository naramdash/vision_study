# 비전스터디 1회

- 2026-05-12 (화)
- 김주호

## 발표 내용

- 1장 Introduction
- 2장 Python and Required Packages
- 3장 Loading, Displaying, and Saving
- 4장 Image Basics
- 5장 Drawing

## 1장 Introduction

배우는 이유

1. **매우 많은** 이미지
    - 제조 검사 이미지
    - 의료 CT/MRI
    - CCTV
    - 위성 사진
    - 자율주행 카메라
    - 물류 바코드 이미지
2. **분석**하고
    - 불량 위치 탐지
    - 이상 부위 확인
    - 사람/차량 감지
    - 차선 인식
    - 균열 탐지
    - 상품 진열 상태 확인
3. **분류**하고
    - 정상/불량 분류
    - 질병 유무 분류
    - 상품 종류 분류
    - 작물 상태 분류
    - 재활용품 종류 분류
    - 문서 유형 분류
4. **정량화**해야한다
    - 결함 개수 측정
    - 종양 크기 측정
    - 교통량 계산
    - 사람 수 계산
    - 작물 생장 정도 측정
    - 균열 길이 측정

감시(surveillance, 추적), 의료, 인체 인식 등 여러 분야에서 사용.

## 2장 Python and Required Packages

책에서 제공하는 환경 구성이 있으나, outdate된 내용이 많아 제가 *현시점에 맞게 적절히 변경*하였습니다.

2026-05-04 기준

- 최신 uv 버전: [0.11.8 (2026-04-27)](https://github.com/astral-sh/uv/releases/tag/0.11.8)
- 최신 OpenCV 버전: [4.13.0 (2025-12-31)](https://github.com/opencv/opencv/releases/tag/4.13.0)
- 최신 Python 버전: [3.14.4 (2026-04-07)](https://github.com/python/cpython/releases/tag/v3.14.4)
- 최신 NumPy 버전: [2.4.4 (2026-03-29)](https://github.com/numpy/numpy/releases/tag/v2.4.4)
- 최신 SciPy 버전: [1.17.1 (2026-02-23)](https://github.com/scipy/scipy/releases/tag/v1.17.1)
- 최신 matplotlib 버전: [3.10.9 (2026-04-24)](https://github.com/matplotlib/matplotlib/releases/tag/v3.10.9)
- 최신 Mahotas 버전: [1.4.18 (2024-07-18)](https://pypi.org/project/mahotas/#history)
- 최신 scikit-learn 버전: [1.8.0 (2025-12-10)](https://github.com/scikit-learn/scikit-learn/releases/tag/1.8.0)


### uv 기반 프로젝트

| 구분            | 일반 파이썬 프로젝트                   | uv 기반 프로젝트                        |
| --------------- | -------------------------------------- | --------------------------------------- |
| 언어            | Python으로 작성됨                      | Rust로 작성됨 (압도적 속도)             |
| 설치 도구       | pip                                    | uv pip                                  |
| 환경 관리       | venv, virtualenv 등 별도 사용          | uv venv (통합 관리)                     |
| 속도            | 패키지 설치 시 수십 초~수 분 소요      | 0.1~1초 내외 (캐싱 최적화)              |
| **의존성 해결** | **가끔 충돌 발생, 해결 속도 느림**     | **매우 빠르고 정확한 의존성 계산**      |
| **버전 관리**   | **별도로 Python 설치 필요 (pyenv 등)** | **uv가 Python 버전까지 직접 설치/관리** |

#### uv 설치

```powershell
# Windows에서 uv 설치
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```bash
# Linux/Mac에서 uv 설치
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### uv로 프로젝트 생성

```bash
# vision_study_1이라는 이름의 프로젝트 생성
# Python 3.13 버전 사용 (3.14는 아직 호환성 문제로 권장되지 않음)
uv init --python ">=3.13, <3.14" vision_study_1

# 프로젝트 디렉토리로 이동
cd vision_study_1

# 생성된 pyproject.toml 파일 확인
cat pyproject.toml 

# 프로젝트에서 사용할 Python 버전 가져오기
uv sync
```

#### uv로 패키지 설치

```bash
# uv 표준 방식으로 패키지 설치
uv add "opencv-python>=4,<5" "numpy>=2,<3" "scipy>=1,<2" "matplotlib>=3,<4" "mahotas>=1,<2" "scikit-learn>=1,<2"

# 설치된 패키지 확인
cat pyproject.toml 
```

## 3장 Loading, Displaying, and Saving

`ch3_load_display_save.py` 파일을 아래와 같이 작성합니다.

```python
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
```

argument와 함께 ch3_load_display_save.py 파일을 실행합니다.

```bash
# ch3_load_display_save.py 파일을 실행하면서 -i 옵션으로 이미지 경로를 전달합니다.
uv run ch3_load_display_save.py -i ~/Pictures/example.png

# 새창에 아무키나 눌러 이미지를 닫습니다.
# [Enter]

# newimage.jpg 파일이 생성되었는지 확인합니다.
ls
```

> **Q1. 왜 `cv`가 아니라 `cv2`인가요?**
> 
> 구 버전(`cv`): 초기 OpenCV는 C 언어 기반이었습니다. 이때 파이썬에서 불러오던 이름이 import cv였습니다.
>
> 신 버전(`cv2`): 이후 OpenCV는 C++ 기반으로 완전히 재설계되었습니다. 이 새로운 C++ 인터페이스를 사용하는 파이썬 바인딩(연결 도구)을 기존의 cv와 구분하기 위해 cv2라는 이름을 붙였습니다.
>
> 지금 우리가 쓰는 OpenCV는 버전 4.13이지만, 파이썬 모듈 이름은 여전히 cv2를 사용합니다. 이는 하위 호환성을 유지하고, cv2라는 이름 자체가 파이썬 오픈씨브이의 대명사가 되었기 때문입니다.

> **Q2. im은 무슨 뜻인가요?**
>
> `im`은 단순하게 Image(이미지)의 약자입니다. 오픈소스 커뮤니티와 영상 처리 분야에서 관행적으로 사용하는 축약어라고 보시면 됩니다.
> 
> 코드에서 자주 보이는 단어들의 의미는 다음과 같습니다.
> - `imread`: Image Read (이미지를 읽어온다)
> - `imshow  `: Image Show (이미지를 화면에 보여준다)
> - `imwrite`: Image Write (이미지를 파일로 저장한다)
> - `img` 또는 `im`: 이미지 데이터를 담고 있는 변수명으로 가장 많이 쓰입니다.

## 4장 Image Basics

### 픽셀이란 무엇인가

- 이미지의 기본적인(primitive) 구성 요소
- 픽셀보다 더 세밀한 단위는 없음
- 일반적으로 픽셀은 이미지의 특정 위치에 있는 "색" 혹은 "강도"를 나타냄
- 500x300 크기의 이미지는 150,000개의 픽셀로 구성됨
- 픽셀은 대부분
  - 단일 채널(흑백 이미지, grayscale)
      -  각 픽셀은 0부터 255 사이의 값
      -  0은 검은색, 255는 흰색
  - 다중 채널(컬러 이미지, color)
      - 각 픽셀은 여러 채널의 값을 가짐 (예: RGB)
      - 각 채널의 값은 0부터 255 사이
      - 0은 해당 채널의 색이 없음, 255는 최대 색 강도
      - 일반적으로 8비트 부호없는 정수(unsigned int8)로 표현
      - 흰색은 `(255, 255, 255)`, 검은색은 `(0, 0, 0)`, 빨간색은 `(255, 0, 0)` 등으로 표현

### 좌표계 개요

- OpenCV에서 이미지의 좌표계는 왼쪽 상단이 원점(0, 0)입니다.
- x축은 오른쪽으로 증가, y축은 아래로 증가합니다.

| y\x | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | ⬛   | ⬛   | ⬛   | ⬛   | ⬛   | ⬛   | ⬛   | ⬛   |
| 1   | ⬜   | ⬜   | ⬜   | ⬛   | ⬜   | ⬜   | ⬜   | ⬜   |
| 2   | ⬜   | ⬜   | ⬜   | ⬛   | ⬜   | ⬜   | ⬜   | ⬜   |
| 3   | ⬜   | ⬜   | ⬜   | ⬛   | ⬜   | ⬜   | ⬜   | ⬜   |
| 4   | ⬜   | ⬜   | ⬜   | ⬛   | ⬜   | ⬜   | ⬜   | ⬜   |
| 5   | ⬜   | ⬜   | ⬜   | ⬛   | ⬜   | ⬜   | ⬜   | ⬜   |
| 6   | ⬜   | ⬜   | ⬜   | ⬛   | ⬜   | ⬜   | ⬜   | ⬜   |
| 7   | ⬛   | ⬛   | ⬛   | ⬛   | ⬛   | ⬛   | ⬛   | ⬛   |

### 픽셀 접근과 조작

ch4_getting_and_setting.py  파일을 아래와 같이 작성합니다.

```python
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
```

argument와 함께 ch4_getting_and_setting.py 파일을 실행합니다.

```bash
# ch4_getting_and_setting.py 파일을 실행하면서 -i 옵션으로 이미지 경로를 전달합니다.
uv run ch4_getting_and_setting.py -i ~/Pictures/example.png

# Corner와 Updated 두 개의 창이 열립니다. 
# Corner 창에는 원래 이미지의 왼쪽 위 100x100 픽셀 영역이 표시되고
# Updated 창에는 100x100이 초록색으로 변경된 이미지가 표시됩니다.

# 새창에 아무키나 눌러 이미지를 닫습니다.
# [Enter]
```

## 5장 Drawing

OpenCV는 이미지 위에 도형을 그릴 수 있는 쉽고 편리한 메소드들을 제공합니다.

- `cv2.line`
- `cv2.rectangle`
- `cv2.circle`

`ch5_drawing.py` 파일을 아래와 같이 작성합니다.

```python
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
```

> [**Q3. 컴퓨터 비전과 이미지 처리에 관한 책에서 왜 굳이 사각형, 원, 선을 그리는 방법을 배워야 하는 걸까요?**](https://customers.pyimagesearch.com/lessons/ppao-chapter-5-drawing/)
>
> 컴퓨터 비전 알고리즘이 이미지 내에서 무언가를 '이해'하고 나면, **그 결과를 사람에게 '시각화'해 보여줘야 하기 때문**
>
> - 관심 영역(ROI, Region of Interest) 표시: 검출된 물체 주위에 사각형 그리기.
> - 움직임 추적: 비디오 스트림에서 움직이는 물체에 경계 상자(Bounding Box) 그리기.
> - 얼굴 검출: 사람이나 고양이 얼굴을 찾아 표시하기.
> - 물체 경로 표시: 물체가 이동한 경로를 선이나 원으로 그리기.
>
> OpenCV의 드로잉 함수는 이미지에서 객체를 찾거나 감지하거나 인식하는 데 직접적인 도움을 주지는 않았지만, **결과를 시각화할 수 있게 해주었으며, 이는 여전히 이미지 처리/컴퓨터 비전 파이프라인의 일부**