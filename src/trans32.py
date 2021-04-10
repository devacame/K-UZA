from google.cloud import translate_v3beta1 as translate
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/kimtaeyi/python_workspace/KUZA-DEV-a933fc24c14d.json'

def Translate(text, source, target):

    client = translate.TranslationServiceClient()
    response = client.translate_text(
        parent = parent,
        contents = text,
        mime_type = 'text/plain',  
        source_language_code = source,
        target_language_code = target)

    for translation in response.translations:
        return format(translation)


print(Translate("Hello World", "en", "ko"))