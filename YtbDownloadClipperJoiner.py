# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from youtube_downloader import YoutubeDownloader
import video_parser
import argparse

URL = "https://www.youtube.com/watch?v=f9zyenX2PWk"
RESOLUTION = "720p"
VIDEO_CODEC = "libx264"
VIDEO_QUALITY = "24"
COMPRESSION = "slow"        # slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
VIDEO_SAVE_DIRECTORY = "C:\\Users\\User\\Desktop\\Download_Ytb"
VIDEO_CLIP_DIRECTORY = "C:\\Users\\User\\Desktop\\Download_Ytb\\ClippedJoined"
SAVE_EACH_CLIP = True
EXTEND_BY_MILLI_SECS = 500
SEGMENTS = [["0:30", "00:45"],
            ["1:00", "01:15"],
            ["2:30", "2:45"]]



def get_args():
    parser = argparse.ArgumentParser(
        description="Script that adds 3 numbers from CMD"
    )
    parser.add_argument("--num1", required=True, type=int)
    parser.add_argument("--num2", required=True, type=int)
    parser.add_argument("--num3", required=True, type=int)
    args = parser.parse_args()

    num1 = args.num1
    num2 = args.num2
    num3 = args.num3
    print(f" {num1} + {num2} + {num3} = {num1 + num2 + num3} ")


def run():
    youtube_dl = YoutubeDownloader(VIDEO_SAVE_DIRECTORY, URL, RESOLUTION)
    youtube_dl.download()
    v_name = youtube_dl.get_downloaded_title()

    video_prs = video_parser.VideoParser(VIDEO_SAVE_DIRECTORY, VIDEO_CLIP_DIRECTORY,
                                         VIDEO_CODEC, VIDEO_QUALITY, COMPRESSION)
    video_prs.parse_video(v_name, SEGMENTS, SAVE_EACH_CLIP, EXTEND_BY_MILLI_SECS)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_args()
    # run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/