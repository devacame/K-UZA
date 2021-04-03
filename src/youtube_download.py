from pytube import YouTube
from os import rename


def get_youtube_audio(url):
    yt = YouTube(url)
    try:
        video = yt.streams.filter(only_audio=True).first().download()
    except Exception:
        return 'Fatal:오디오 처리에 실패하였습니다.'
    rename(video, 'audio.mp3')
    return None
