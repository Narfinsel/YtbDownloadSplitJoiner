# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from user_classes.youtube_downloader import YoutubeDownloader
from user_classes import video_parser
import argparse, platform, os, re
from os.path import expanduser

URL = "https://www.youtube.com/watch?v=f9zyenX2PWk"
RESOLUTION = "720p"
VIDEO_CODEC = "libx264"
VIDEO_QUALITY = "24"
COMPRESSION = "slow"        # slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
DIRECTORY_DL = "C:\\Users\\User\\Desktop\\Download_Ytb"
DIRECTORY_DL_CLIP_JOIN = ""
FOLDER_CLIP = "ClippedJoined"
SAVE_EACH_CLIP = True
EXTEND_BY_MILLI_SECS = 500
# SEGMENTS = "0:30-00:45, 1:00-01:15, 2:30-2:45"
SEGMENTS = "0:28-00:73, 1:02-01:19, 2:20-2:35"

SEPARATOR = "\ or /"


def get_folder_separator():
    sys_platform = platform.system()
    separator = "ss"
    if sys_platform == 'Darwin' or sys_platform =='Linux':
        separator = "/"
    elif sys_platform == 'Windows':
        separator = "\\"
    return separator


def get_default_dl(separator):
    home = expanduser("~")
    my_dl_location = home + separator + "Desktop" + separator + "Download_Ytb"
    return  my_dl_location


def parse_segments(segments):
    # big_segments = re.split(',|, |\[|\]', segments)
    big_segments = re.split(',|, ', segments)
    new_array = []
    for big in big_segments:
        if big != '':
            big = big.strip()
            small_segments = re.split("(\s)*-(\s)*", big)
            new_array.append( [small for small in small_segments if small is not None])
    return new_array



def set_args():
    parser = argparse.ArgumentParser(
        description="Script that adds 3 numbers from CMD"
    )
    parser.add_argument("--dl_dir", type=str)
    parser.add_argument("--url", type=str, required=True)
    parser.add_argument("--res", type=str)
    parser.add_argument("--v_codec", type=str)
    parser.add_argument("--v_quality", type=str)
    parser.add_argument("--compression", type=str)
    parser.add_argument("--save_clips", type=bool)
    parser.add_argument("--extend_ms", type=int)
    parser.add_argument("--segments", type=str, required=True)


    global DIRECTORY_DL, DIRECTORY_DL_CLIP_JOIN, SEPARATOR
    global URL, RESOLUTION, SAVE_EACH_CLIP
    global VIDEO_CODEC, VIDEO_QUALITY, COMPRESSION, EXTEND_BY_MILLI_SECS, SEGMENTS

    args = parser.parse_args()
    DIRECTORY_DL = args.dl_dir
    URL = args.url
    RESOLUTION = args.res
    VIDEO_CODEC = args.v_codec
    VIDEO_QUALITY = args.v_quality
    COMPRESSION = args.compression
    SAVE_EACH_CLIP = args.save_clips
    EXTEND_BY_MILLI_SECS = abs(args.extend_ms)
    SEGMENTS = args.segments
    SEGMENTS = parse_segments(SEGMENTS)

    # print(f"  -  SEGMENTS = {SEGMENTS}")
    SEPARATOR = get_folder_separator()

    if DIRECTORY_DL is None:
        DIRECTORY_DL = get_default_dl(SEPARATOR)

    DIRECTORY_DL_CLIP_JOIN = DIRECTORY_DL + SEPARATOR + FOLDER_CLIP
    if not os.path.exists(DIRECTORY_DL_CLIP_JOIN):
        os.makedirs(DIRECTORY_DL_CLIP_JOIN)

    if RESOLUTION is None:
        RESOLUTION = "720p"
    if VIDEO_CODEC is None:
        VIDEO_CODEC = "libx264"
    if VIDEO_QUALITY is None:
        VIDEO_QUALITY = "24"
    if COMPRESSION is None:
        COMPRESSION = "slow"
    if SAVE_EACH_CLIP is None:
        SAVE_EACH_CLIP = False
    if EXTEND_BY_MILLI_SECS is None:
        EXTEND_BY_MILLI_SECS = 0


def run():
    youtube_dl = YoutubeDownloader(DIRECTORY_DL, URL, RESOLUTION)
    youtube_dl.download()
    v_name = youtube_dl.get_downloaded_title()

    video_prs = video_parser.VideoParser(DIRECTORY_DL, DIRECTORY_DL_CLIP_JOIN, SEPARATOR,
                                         VIDEO_CODEC, VIDEO_QUALITY, COMPRESSION)
    video_prs.parse_video(v_name, SEGMENTS, SAVE_EACH_CLIP, EXTEND_BY_MILLI_SECS)


def print_args():
    print(f"  -  VIDEO_DL_DIRECTORY   = {DIRECTORY_DL}")
    print(f"  -  VIDEO_CLIP_DIRECTORY = {DIRECTORY_DL_CLIP_JOIN}")
    print(f"  -  SEPARATOR   = {SEPARATOR}")
    print(f"  -  URL = {URL}")
    print(f"  -  RESOLUTION  = {RESOLUTION}")
    print(f"  -  VIDEO_CODEC = {VIDEO_CODEC}")
    print(f"  -  VIDEO_QUALITY = {VIDEO_QUALITY}")
    print(f"  -  COMPRESSION = {COMPRESSION}")
    print(f"  -  SAVE_EACH_CLIP = {SAVE_EACH_CLIP}")
    print(f"  -  EXTEND_BY_MILLI_SECS = {EXTEND_BY_MILLI_SECS}")
    print(f"  -  SEGMENTS = {SEGMENTS}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    set_args()
    run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/