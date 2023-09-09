import pytube
from pytube import YouTube

url = input("enter video url pls :")

path = ""

yt = YouTube(
        url
    )

yt.streams.get_highest_resolution().download(path)
