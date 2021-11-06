from pytube import YouTube
from os import rename


def get_youtube_audio(url):
    try:
        video = YouTube(url).streams.filter(only_audio=True).first()
        file_name = video.download()
    except Exception as e:
        print(e)
        return 'Fatal:오디오 처리에 실패하였습니다.'
    rename(file_name, 'audio.mp3')
    return None

