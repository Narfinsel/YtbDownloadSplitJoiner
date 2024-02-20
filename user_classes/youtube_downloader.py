
from pytube import YouTube


class YoutubeDownloader:
    def __init__(self, download_dir, url, resolution):
        self.download_dir = download_dir
        self.url = url
        self.resolution = resolution
        self.downloaded_filename = "none"


    def download(self):
        self.__download(self.download_dir, self.url)


    def __download(self, dl_directory, video_url):
        video_dl = YouTube(video_url)
        video = video_dl.streams.get_by_resolution(self.resolution)
        if video is None:
            video = video_dl.streams.get_highest_resolution()
        dl_resolution1 = video.__getattribute__("resolution")

        try:
            video.download(dl_directory)
            self.downloaded_filename = video.default_filename
            print("video was downloaded successfully")
        except:
            print("Failed to download video")


    def get_downloaded_title(self):
        return self.downloaded_filename