# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from classes.parser.youtube_downloader import YoutubeDownloader
from classes.parser import video_parser
import argparse, platform, os, re
from os.path import expanduser

URL = "https://www.youtube.com/watch?v=mIV5rCuDb74"
RESOLUTION = "720p"
VIDEO_CODEC = "libx264"
VIDEO_QUALITY = "24"
COMPRESSION = "slow"        # slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
DIRECTORY_DL = "C:\\Users\\User\\Desktop\\Download_Ytb"
DIRECTORY_DL_CLIP_JOIN = ""
FOLDER_CLIP = "ClippedJoined"
SAVE_EACH_CLIP = True
DELETE_AFTER = False
EXTEND_BY_MILLI_SECS = 500
SEGMENTS = ""
SEGMENTS = "0:30-00:45, 1:00-01:15, 2:30-2:45"



def get_default_dl():
    home = expanduser("~")
    my_dl_location = os.path.join(home, "Desktop", "Download_Ytb")
    return my_dl_location


def print_args():
    print("\n")
    print(f"  -  VIDEO_DL_DIRECTORY   = {DIRECTORY_DL}")
    print(f"  -  VIDEO_CLIP_DIRECTORY = {DIRECTORY_DL_CLIP_JOIN}")
    print(f"  -  SEPARATOR   = {SEPARATOR}")
    print(f"  -  URL = {URL}")
    print(f"  -  RESOLUTION  = {RESOLUTION}")
    print(f"  -  VIDEO_CODEC = {VIDEO_CODEC}")
    print(f"  -  VIDEO_QUALITY = {VIDEO_QUALITY}")
    print(f"  -  COMPRESSION = {COMPRESSION}")
    print(f"  -  SAVE_EACH_CLIP = {SAVE_EACH_CLIP}")
    print(f"  -  DELETE_AFTER = {DELETE_AFTER}")
    print(f"  -  EXTEND_BY_MILLI_SECS = {EXTEND_BY_MILLI_SECS}")
    print(f"  -  SEGMENTS = {SEGMENTS}")
    print("\n")


def set_args():
    parser = argparse.ArgumentParser(description="From PyClipJoiner.sh")
    parser.add_argument("--dl", type=str)
    parser.add_argument("--dest", type=str)
    parser.add_argument("--url", type=str, required=True)
    parser.add_argument("--res", type=str)
    parser.add_argument("--codec", type=str)
    parser.add_argument("--qual", type=str)
    parser.add_argument("--comp", type=str)
    parser.add_argument("--save", type=str)
    parser.add_argument("--deldl", type=str)
    parser.add_argument("--ext", type=int)
    parser.add_argument("--seg", type=str)

    global DIRECTORY_DL, DIRECTORY_DL_CLIP_JOIN
    global URL, RESOLUTION, SAVE_EACH_CLIP, DELETE_AFTER
    global VIDEO_CODEC, VIDEO_QUALITY, COMPRESSION, EXTEND_BY_MILLI_SECS, SEGMENTS

    args = parser.parse_args()
    DIRECTORY_DL = args.dl
    DIRECTORY_DL_CLIP_JOIN = args.dest
    URL = args.url
    RESOLUTION = args.res
    VIDEO_CODEC = args.codec
    VIDEO_QUALITY = args.qual
    COMPRESSION = args.comp
    SAVE_EACH_CLIP = args.save
    DELETE_AFTER = args.deldl
    EXTEND_BY_MILLI_SECS = args.ext
    SEGMENTS = args.seg

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
    if DELETE_AFTER is None:
        DELETE_AFTER = True
    if EXTEND_BY_MILLI_SECS is None:
        EXTEND_BY_MILLI_SECS = 0
    if SEGMENTS is None:
        SEGMENTS = ""


def run():
    global SEGMENTS, DIRECTORY_DL, DIRECTORY_DL_CLIP_JOIN, EXTEND_BY_MILLI_SECS

    if DIRECTORY_DL is None:
        DIRECTORY_DL = get_default_dl()
    if not os.path.exists(DIRECTORY_DL):
        os.makedirs(DIRECTORY_DL)

    if DIRECTORY_DL_CLIP_JOIN is None or DIRECTORY_DL_CLIP_JOIN == '':
        DIRECTORY_DL_CLIP_JOIN = os.path.join(DIRECTORY_DL, FOLDER_CLIP)
    if not os.path.exists(DIRECTORY_DL_CLIP_JOIN):
        os.makedirs(DIRECTORY_DL_CLIP_JOIN)

    EXTEND_BY_MILLI_SECS = abs(int(EXTEND_BY_MILLI_SECS))

    youtube_dl = YoutubeDownloader(DIRECTORY_DL, URL, RESOLUTION)
    youtube_dl.download()
    v_name = youtube_dl.get_downloaded_title()

    video_prs = video_parser.VideoParser(DIRECTORY_DL, DIRECTORY_DL_CLIP_JOIN,
                                         VIDEO_CODEC, VIDEO_QUALITY, COMPRESSION)
    if SEGMENTS != "":
        video_prs.parse_video(v_name, SEGMENTS, SAVE_EACH_CLIP, DELETE_AFTER, EXTEND_BY_MILLI_SECS)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Remove set_args if running from PyCharm or any other IDE
    run_inside_pycharm = os.getenv("RUNNING_IN_PYCHARM")
    if run_inside_pycharm is None:
        set_args()
    run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/