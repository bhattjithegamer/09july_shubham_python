import pytube
url = "https://youtu.be/RLhuPD2ASKE?si=pI19LcHDbpxsZ0m2"
yt = pytube.YouTube(url)

streams = yt.streams.get_highest_resolution()
streams.download()
print("Download completed...")