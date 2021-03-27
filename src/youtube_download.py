from youtube_dl import YoutubeDL


def get_youtube_audio(url):
    try:
        audio_dl = YoutubeDL({'format': 'bestaudio'})
        audio_dl.extract_info(url)
    except Exception:
        return "오디오 처리에 실패하였습니다."
    return None
