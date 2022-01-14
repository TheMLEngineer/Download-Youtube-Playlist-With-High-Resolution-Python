
from pytube import Playlist , YouTube
# p is playlist URL that you want to download
p = 'https://www.youtube.com/playlist?list=PLR_Fdtpy7e-zxVFrZ1kMdxOtnoxvDfDov'

playlist = Playlist(p)
urls = []
print('Number of videos in playlist: %s' % len(playlist.video_urls))
for video_url in playlist.video_urls:
    print(video_url)
    urls.append(video_url)
    for url in urls:
        my_video = YouTube(url)

        print("*****************DOWNLOAD VID*************")
        print(my_video.title)

        my_video = my_video.streams.get_highest_resolution()
        # As my local is Linux I used Linux file path , If you are using Windows OS PATH structure may differ , Copy the absolute path where you need to download videos here
        path = '/home/karthik/Downloads/MHB'
        my_video.download(path)
        print("VIDEO DOWNLOAD DONE")
