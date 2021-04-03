from google.cloud import translate_v2 as translate
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ''

def trans(text, target_lang):
    try:
        client = translate.Client()
        result = client.translate(text, target_lang)
    except:
        return None

    return result['translatedText']



