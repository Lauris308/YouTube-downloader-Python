from pytube import Playlist

choice = input("Download audio(a) or video(v)?").lower()

p = Playlist(input("Enter playlist: " ))
opath = input("Enter file location: ")

if choice == "a":
    print(f'Downloading: {p.title}')
    for video in p.videos:
        video.streams.get_audio_only().download(opath)

elif choice == "v":
    print(f'Downloading: {p.title}')
    for video in p.videos:
        video.streams.get_highest_resolution().download(opath)
else:
    exit()
