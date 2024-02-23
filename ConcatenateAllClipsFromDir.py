# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from user_classes.ConcaterVidsInFolder import ConcaterVidsInFolder


RESOLUTION = "720p"
VIDEO_CODEC = "libx264"
VIDEO_QUALITY = "24"
COMPRESSION = "slow"        # slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
DIRECTORY_DL = "C:\\Users\\User\\Desktop\\Download_Ytb\\ClippedJoined"
EXTENSIONS = ("mp4", ".mov", ".avi", ".vlc", ".wmv", ".webm", ".flv")
SEPARATOR = "\ or /"




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Remove set_args if running from PyCharm or any other IDE
    # set_args()
    concater = ConcaterVidsInFolder(DIRECTORY_DL, EXTENSIONS, VIDEO_CODEC, VIDEO_QUALITY, COMPRESSION)
    concater.retrieve_vids_from_folder()




# See PyCharm help at https://www.jetbrains.com/help/p