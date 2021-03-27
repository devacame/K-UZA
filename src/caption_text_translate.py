from google.cloud import translate
import os
# 구글 번역 api 인증 키 파일 설정
# 다운로드한 json파일 위치를 넣어주면 된다.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ''

# 번역 함수 
def trans(text, target = 'ko'):
    # 클래스 생성 
    translate_client = translate.Client()
    # 번역 시작
    translation = translate_client.translate(
        text,
        target_language=target)

    # 번역한 문자열 리턴
    return translation['translatedText']


    #주석

