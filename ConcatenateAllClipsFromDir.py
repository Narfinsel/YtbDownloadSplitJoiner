# This is a sample Python script.
import os.path
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from user_classes.ConcaterVidsInFolder import ConcaterVidsInFolder
from os.path import expanduser
import argparse

EXTENSIONS = ("mp4", "mov", "avi", "vlc", "wmv", "webm", "flv")
DIRECTORY_DL = "C:\\Users\\User\\Desktop\\Download_Ytb\\ClippedJoined"
RESOLUTION = "720p"
VIDEO_CODEC = "libx264"
VIDEO_QUALITY = "24"
COMPRESSION = "slow"        # slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
PREF_EXTENSION = ("mp4")
FINAL_VID_NAME = "GUGUCHI"


def get_default_dl():
    home = expanduser("~")
    my_dl_location = os.path.join(home, "Desktop", "Download_Ytb", "ClippedJoined")
    return my_dl_location


def set_args():
    parser = argparse.ArgumentParser(description="From PyVidConcater.sh")
    parser.add_argument("--dir", type=str)
    parser.add_argument("--name", type=str)
    parser.add_argument("--suff", type=str)
    parser.add_argument("--res", type=str)
    parser.add_argument("--codec", type=str)
    parser.add_argument("--qual", type=str)
    parser.add_argument("--comp", type=str)

    global DIRECTORY_DL, FINAL_VID_NAME, PREF_EXTENSION
    global RESOLUTION, VIDEO_CODEC, VIDEO_QUALITY, COMPRESSION

    args = parser.parse_args()
    DIRECTORY_DL = args.dir
    FINAL_VID_NAME = args.name
    PREF_EXTENSION = args.suff
    RESOLUTION = args.res
    VIDEO_CODEC = args.codec
    VIDEO_QUALITY = args.qual
    COMPRESSION = args.comp

    if FINAL_VID_NAME is None:
        FINAL_VID_NAME = "PyConcaterVid_" + str(random.randint(1, 1000))
    if PREF_EXTENSION is None:
        PREF_EXTENSION = "mp4"
    if RESOLUTION is None:
        RESOLUTION = "720p"
    if VIDEO_CODEC is None:
        VIDEO_CODEC = "libx264"
    if VIDEO_QUALITY is None:
        VIDEO_QUALITY = "24"
    if COMPRESSION is None:
        COMPRESSION = "slow"


def run():
    global DIRECTORY_DL
    if DIRECTORY_DL is None:
        DIRECTORY_DL = get_default_dl()
    if not os.path.exists(DIRECTORY_DL):
        os.makedirs(DIRECTORY_DL)

    concater = ConcaterVidsInFolder(DIRECTORY_DL, PREF_EXTENSION, VIDEO_CODEC, VIDEO_QUALITY, COMPRESSION)
    concater.join_videos(FINAL_VID_NAME)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Remove set_args if running from PyCharm or any other IDE
    run_inside_pycharm = os.getenv("RUNNING_IN_PYCHARM")
    if run_inside_pycharm is None:
        set_args()
    run()





# See PyCharm help at https://www.jetbrains.com/help/p