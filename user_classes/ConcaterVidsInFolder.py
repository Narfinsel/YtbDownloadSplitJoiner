
from moviepy.editor import *
import os, re


class ConcaterVidsInFolder:
    def __init__(self, directory_concat, extension, video_codec, video_quality, compression):
        self.directory_concat = directory_concat
        self.extension = extension
        self.video_codec = video_codec
        self.video_quality = video_quality
        self.compression = compression
        self.regex_ext = "(^.*\.(" + extension + ")$)"
        # self.regex_ext = "(^.*\.("+ '|'.join(extensions) +")$)"   " for array of extensions


    def __retrieve_vids_from_folder(self, flag_present_in_name=""):
        flag_present_in_name = flag_present_in_name.strip()
        pattern_ext = re.compile(self.regex_ext)
        video_list = []

        for filename in os.scandir(self.directory_concat):
            if filename.is_file():
                if pattern_ext.match(filename.name):
                    if flag_present_in_name != "":
                        if flag_present_in_name in filename.name:
                            full_name = os.path.join(self.directory_concat, filename.name)
                            video_list.append(full_name)
                    else:
                        full_name = os.path.join(self.directory_concat, filename.name)
                        video_list.append(full_name)
        return video_list


    def join_videos(self, final_vid_name, flag_present_in_name=""):
        name_list = self.__retrieve_vids_from_folder(flag_present_in_name)
        print(f" final_vid_name = {final_vid_name}        self.extension = {self.extension}")
        final_vid_name = final_vid_name + "." + self.extension
        final_vid_name = os.path.join(self.directory_concat, final_vid_name)

        # concatenate files
        clips_list = []
        for name in name_list:
            clips_list.append( VideoFileClip(name) )
        final_clip = concatenate_videoclips(clips_list)

        # save file
        final_clip.write_videofile(final_vid_name, threads=4, fps=24,
                                   codec=self.video_codec,
                                   preset=self.compression,
                                   ffmpeg_params=["-crf", self.video_quality])




