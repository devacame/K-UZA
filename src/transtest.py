from google.cloud import translate
from google.cloud import translate_v2 as translate
import os

def Translate(text, Source_lang, target_language):
    if Source_lang == None: 
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
                "source_language_code": Source_lang,
                "target_language_code": target_language,
                }
            )
            Word_translate = []
            for translation in response.translations:
                Word_translate.append(translation.translated_text)
            return " ".join(Word_translate)
        except:
            return None

