## 👋 opencv-controller
Python GUI OpenCV 영상 처리


## 💻 가상환경 Install

```bash
pip install -r requirements.txt
python -m venv 가상환경이름
```

## 1️⃣ 기능: '영상 불러오기'
```
영상 호출 확인 (기능없음)
Check video call (no function)
```

## 2️⃣ 기능: '이미지 호출'
```
첫번째 버튼 영상 파일 선택, 두번째 버튼 이미지 파일 선택. 두 개의 파일을 블렌딩합니다.
The first button selects a video file, the second button selects an image file. Blends two files.
```

## 3️⃣ 기능: '도면 마스크 영역 추출'
```
두번째 버튼 이미지 파일 선택, 저장 경로 필수 지정
Select second button image file, specify save path required
```

## 4️⃣ 기능: '영상 위에 이미지(+알파) 합성'
```
첫번째 버튼 영상 파일 선택, 두번째 버튼에서 처음은 원본 이미지, 다음은 알파 이미지 선택. 현재 경로에서 out 폴더 생성 후 날짜로 영상 저장.
The first button selects the video file, the second button selects the original image first and then the alpha image. Create an out folder in the current path and save the video by date.
```