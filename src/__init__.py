import sys
sys.path.append('./.')
from youtube_download import get_youtube_audio
from setup_google_storage import create_bucket, upload_audio_file, delete_audio_file
from caption_stt import run_stt
from caption_text_translate import translate
from google.cloud import storage
from os import environ


def run_backend(url, stt_lang='en-US'):
    try:
        with open('./GCP-API-KEY.json', 'r') as keyfile:
            iskey = keyfile.read()
        environ['GOOGLE_APPLICATION_CREDENTIALS'] = './GCP-API-KEY.json'
        if not iskey.strip():
            raise RuntimeError
    except Exception:
        return 'GCP 키가 없습니다.'
    caption = ''

    try:
        audio_state = get_youtube_audio(url)
        if audio_state:
            raise Exception

        try:
            storage.Client().get_bucket('kuza_audio')
        except Exception:
            bucket_creation_state = create_bucket()
            if bucket_creation_state:
                raise Exception

        upload_state = upload_audio_file()
        if upload_state:
            raise Exception

        caption = run_stt(stt_lang)
        if caption.startswith('Fatal:'):
            raise Exception

        translated_text = translate(caption)
        if translated_text.startswith('Fatal:'):
            raise Exception

    except Exception:
        return f'Fatal:알 수 없는 에러가 발생하였습니다.\n{translated_text}'

    deletion_state = delete_audio_file()
    if deletion_state:
        return deletion_state

    return translated_text