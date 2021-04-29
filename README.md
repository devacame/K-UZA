# 프로젝트 : K-UZA
파이썬 자막 생성 프로그램
## <기능>
유튜브 영상의 대화를 번역해서 볼 수 있음
1. STT - Google
	* 언어 목록
		1. 영어
		2. 프랑스어
		3. 스페인어
		4. 독일어
		5. 중국어
		6. 일본어
		7. 러시아어
		8. 네덜란드어
		9. 직접입력
2. 번역
	* 언어 : 한국어

## 전체적인 흐름
1. URL 통해 오디오 다운로드
2. GCP Cloud Storage에 오디오 파일 업로드
3. 영상 출력
4. 오디오 처리
    1. STT(Speech to Text) - Google
    2. Translate - Google

## <개발 환경>
### [언어]

	* Python 3.9.2

### [VCS]

	* GIT
	설치 : https://git-scm.com/
	깃허브 Repo : https://github.com/coder38611/K-UZA

### [가상 환경]

-Python 내장 venv (가상 환경 설정)

```
$ python -m venv venv (Mac/Linux: python3)
$ source venv/Scripts/activate (Mac/Linux: venv/bin/activate)
$ pip install wheel (Mac/Linux: pip3)
```

### [외부 라이브러리]

* google-cloud-speech
* google-cloud-translate
* pytube
* PyQt5

```
$ pip install SpeechRecognition googletrans PyQt5 (Mac/Linux: pip3)
$ pip install git+https://github.com/pytube/pytube (Mac/Linux: pip3)
```

## 프로젝트 파일
### K-UZA.py - main 파일

* 이 파일을 실행하여 프로그램 실행

### GUI

* 메인 GUI 컴포넌트 \_\_init\_\_.py

### src

* 영상 다운로드 - youtube_download.py
* 자막 추출 - caption_stt.py
* 자막 번역 - caption_text_translate.py

## <일정>

* 1주차 - 프로젝트 구상 및 아이디어 회의
* 2주차 - 구체적인 계획 결정
* 3주차 - 개발 환경 설정
* 4주차 - 1차시 개발 (기능 개발-오디오 다운로드 및 자막 번역)
* 5주차 - 2차시 개발 (기능 개발-STT 및 버그 수정)
* 6주차 - 3차시 개발 (GUI 개발)
* 7주차 - 버그 수정 및 프로젝트 마무리