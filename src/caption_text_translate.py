# from google.cloud import translate
from google.cloud import translate_v2


def translate(text):
    # if source_lang == None:
    try:
        client = translate_v2.Client()
        result = client.translate(text, 'ko')
        return (result['translatedText'])
    except Exception:
        return 'Fatal: 자막 번역에 실패하였습니다.'
    # else:
    #     try:
    #         response = client.translate_text(
    #             request={
    #                 "parent": parent,
    #                 "contents": [text],
    #                 "mime_type": "text/plain",
    #                 "source_language_code": source_lang,
    #                 "'ko'_code": 'ko',
    #             }
    #         )
    #         word_translate = []
    #         for translation in response.translations:
    #             word_translate.append(translation.translated_text)
    #             print(translation.translated_text)
    #         return " ".join(word_translate)
    #     except Exception:
    #         return 'Fatal: 자막 번역에 실패하였습니다.'
