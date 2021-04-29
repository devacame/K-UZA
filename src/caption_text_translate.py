from google.cloud import translate_v2


def translate(text):
    try:
        client = translate_v2.Client()
        result = client.translate(text, 'ko')
        return (result['translatedText'])
    except Exception:
        return 'Fatal: 자막 번역에 실패하였습니다.'
