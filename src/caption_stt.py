from google.cloud import speech_v1p1beta1 as speech


def run_stt(lang):
    try:
        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(uri=f'gs://kuza_audio/audio_file')
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.MP3,
            sample_rate_hertz=16000,
            language_code=lang,
        )
        operation = client.long_running_recognize(config=config, audio=audio)
    except Exception:
        return 'Fatal:STT 서비스 연결에 실패하였습니다.'

    try:
        response = operation.result(timeout=6000)
        text = ''
        for result in response.results:
            text += result.alternatives[0].transcript + ' '
    except Exception:
        return 'Fatal:자막 생성에 실패하였습니다.(시간 초과)'
    return text
