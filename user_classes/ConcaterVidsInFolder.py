
from moviepy.editor import *
import os


class ConcaterVidsInFolder:
    def __init__(self, directory_concat, extensions, video_codec, video_quality, compression):
        self.directory_concat = directory_concat
        self.extensions = extensions
        self.video_codec = video_codec
        self.video_quality = video_quality
        self.compression = compression

    def retrieve_vids_from_folder(self):
        for filename in os.scandir(self.directory_concat):
            if filename.is_file():
                if filename.endswith():
                    print(filename.path)

    def join_videos(self, final_vid_name, flag_in_clip_name=""):
        clips_list = []

        final_clip = concatenate_videoclips(clips_list)
        # save file
        final_vid_name = self.directory_concat + self.separator + "Concat_" + "daa"
        final_clip.write_videofile(final_vid_name, threads=4, fps=24,
                                   codec=self.video_codec,
                                   preset=self.compression,
                                   ffmpeg_params=["-crf", self.video_quality])




