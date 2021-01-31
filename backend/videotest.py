from pytube import YouTube
import os
import ffmpy


def downloadVideo(url):
    yt = YouTube(url)
    yt = yt.streams.filter(only_audio=True).first()
    if not os.path.exists("./tmp"):
        os.makedirs("./tmp")
    yt.download("./tmp", filename="video")
    os.system("ffmpeg -i ./tmp/video.mp4 -acodec pcm_s16le -ar 16000 ./tmp/video.wav")


videourl = "https://www.youtube.com/watch?v=v4ISo3oB9Lw&ab_channel=MrSuicideSheep"
downloadVideo(
    videourl,
)
