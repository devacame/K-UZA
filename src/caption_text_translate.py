from google.cloud import translate
from google.cloud import translate_v2 as translate


def translate(text, source_lang, target_language='ko'):
    if source_lang == None:
        try:
            client = translate.Client()
            result = client.translate(text, target_language)
            return (result['translatedText'])
        except:
            return None
    else:
        try:
            response = client.translate_text(
                request={
                    "parent": parent,
                    "contents": [text],
                    "mime_type": "text/plain",
                    "source_language_code": source_lang,
                    "target_language_code": target_language,
                }
            )
            word_translate = []
            for translation in response.translations:
                word_translate.append(translation.translated_text)
            return " ".join(word_translate)
        except:
            return None
