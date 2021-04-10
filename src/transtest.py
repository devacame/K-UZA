from google.cloud import translate_v3beta1 as translate
from google.cloud import translate_v2 as translate
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/kimtaeyi/python_workspace/KUZA-DEV-a933fc24c14d.json'

def Translate(text, Source_lang, target_language):
    if Source_lang == None: 
        try:
            client = translate.Client()
            result = client.translate(text, target_language)
            print(result['translatedText'])
        except:
            return None

texts = 'Thanks for studying Today!\
The important thing is to take action, do something every day, and little by little, you will get there.'
Translate(texts, None, 'ko')
