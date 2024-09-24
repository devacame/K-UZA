# 프로젝트/Project Name : K-UZA
파이썬 자막 생성 프로그램/Python caption translating program - made before google supported auto translate captions on YouTube
## <기능>
유튜브 영상의 대화를 번역해서 볼 수 있음
1. STT - Google
	* 언어 목록/Language List
		1. 영어/English
		2. 프랑스어/French
		3. 스페인어/Spanish
		4. 독일어/German
		5. 중국어/Chinese
		6. 일본어/Japanese
		7. 러시아어/Russian
		8. 네덜란드어/Dutch
		9. 직접입력/Manual
2. 번역/Translate to
	* 언어 : 한국어/Korean

## 전체적인 흐름/Process
1. URL 통해 오디오 다운로드/Download audio by url
2. GCP Cloud Storage에 오디오 파일 업로드/Upload file to GCP
3. 영상 출력/Display Video
4. 오디오 처리/Process audio
    1. STT(Speech to Text) - Google
    2. Translate - Google

## <개발 환경/Development Environment>
### [언어/Language]

	* Python 3.9.2

### [VCS]

	* GIT
	설치 : https://git-scm.com/
	깃허브 Repo : https://github.com/coder38611/K-UZA

### [가상 환경/Virtual Envrionment]

-Python 내장 venv (가상 환경 설정)

```
$ python -m venv venv (Mac/Linux: python3)
$ source venv/Scripts/activate (Mac/Linux: venv/bin/activate)
$ pip install wheel (Mac/Linux: pip3)
```

### [외부 라이브러리/External Libraries]

* google-cloud-speech
* google-cloud-translate
* pytube
* PyQt5

```
$ pip install SpeechRecognition googletrans PyQt5 (Mac/Linux: pip3)
$ pip install git+https://github.com/pytube/pytube (Mac/Linux: pip3)
```

## 프로젝트 파일/Project Files
### K-UZA.py - main 파일

* 이 파일을 실행하여 프로그램 실행 / Run this file to execute

### GUI

* 메인 GUI 컴포넌트/Main GUI Component \_\_init\_\_.py

### src

* 영상 다운로드/Download Video - youtube_download.py
* 자막 추출/Extract Captions - caption_stt.py
* 자막 번역/Translate Captions - caption_text_translate.py

## <일정/Progress> (주당 2시간/2hr per week)

* 1주차 - 프로젝트 구상 및 아이디어 회의 Week 1 - Brainstorm ideas
* 2주차 - 구체적인 계획 결정 Week 2 - Finalize project plan
* 3주차 - 개발 환경 설정 Week 3 - Set dev environment
* 4주차 - 1차시 개발 (기능 개발-오디오 다운로드 및 자막 번역) Week 4 - Programming Session 1 (Feature: Download audio and translate captions)
* 5주차 - 2차시 개발 (기능 개발-STT 및 버그 수정) Week 5 - Programming Session 2 (Feature: Implement Speech-to-Text and bug fixes) 
* 6주차 - 3차시 개발 (GUI 개발) Week 6 - Progamming Session 3 (Feature: Develop GUI)
* 7주차 - 버그 수정 및 프로젝트 마무리 Week 7 - Bug fixes and finishing the project
