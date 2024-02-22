# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from moviepy.editor import *

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
SEGMENTS = "0:30-00:45, 1:00-01:15, 2:30-2:45"
SEPARATOR = "\ or /"


def __join_clips(self, clips_list, video_name):
    if len(clips_list) == 0:
        return
    final_clip = concatenate_videoclips(clips_list)
    # save file
    final_vid_name = self.directory_video + self.separator + "Concat_" + video_name
    final_clip.write_videofile(final_vid_name, threads=4, fps=24,
                               codec=self.video_codec,
                               preset=self.compression,
                               ffmpeg_params=["-crf", self.video_quality])




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Remove set_args if running from PyCharm or any other IDE
    # set_args()
    __join_clips()


# See PyCharm help at https://www.jetbrains.com/help/p