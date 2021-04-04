from setup_google_storage import create_bucket, upload_audio_file, delete_audio_file
from youtube_download import get_youtube_audio
from caption_stt import run_stt
from google.cloud import storage
from os import environ
environ['GOOGLE_APPLICATION_CREDENTIALS'] = './GCP-API-KEY.json'


def run_backend(url, lang='en-US'):
    caption = ''
    try:
        audio_state = get_youtube_audio(url)
        if audio_state:
            return audio_state
        bucket_name = 'kuza_audio'
        try:
            storage.Client().get_bucket(bucket_name)
        except Exception:
            bucket_creation_state = create_bucket(bucket_name)
            if bucket_creation_state:
                return bucket_creation_state
        upload_state = upload_audio_file(bucket_name)
        if upload_state:
            return upload_state
        caption = run_stt(lang, bucket_name)
        if caption.startswith('Fatal'):
            return caption
    except Exception:
        return 'Fatal:알 수 없는 에러가 발생하였습니다.'
    finally:
        deletion_state = delete_audio_file(bucket_name)
        if deletion_state:
            return deletion_state
    return caption
