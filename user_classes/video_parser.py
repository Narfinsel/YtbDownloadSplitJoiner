
from moviepy.editor import *
from datetime import datetime, timedelta
import re


class VideoParser:
    def __init__(self, directory_video, directory_clip_join, separator, video_codec, video_quality, compression):
        self.directory_video = directory_video
        self.directory_clip_join = directory_clip_join
        self.video_codec = video_codec
        self.video_quality = video_quality
        self.compression = compression
        self.separator = separator

        self.regex_all_cases = "((\d)?(\d)?\:)?((\d)?\d:\d\d)(\.)?(\d *)"
        self.regex_hmsf = "(?<!\:)((\d)?\d:\d\d:\d\d\.\d*)"   # pattern 00:00:00.0000 or 0:00:00.0000
        self.regex_msf = "(?<!\:)((\d)?\d:\d\d\.\d*)"         # pattern 00:00.0000 or 0:00.0000
        self.regex_ms = "((\d)?\d:\d\d)"                      # pattern 00:00 or 0:00
        self.pattern_hmsf = re.compile(self.regex_hmsf)
        self.pattern_msf = re.compile(self.regex_msf)
        self.pattern_ms = re.compile(self.regex_ms)


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


    def parse_video(self, video_name, segments, do_save_each_clip, delete_ytb_vid_after, extend_both_side_by_milli_secs):
        full_vid_name = self.directory_video + self.separator + video_name
        clipped = []

        video = VideoFileClip(full_vid_name)
        count = 0
        for segment in segments:
            count += 1
            start_time = self.__subtract_delta_and_return_string(segment[0], -1 * extend_both_side_by_milli_secs)
            end_time = self.__subtract_delta_and_return_string(segment[1], extend_both_side_by_milli_secs)
            clip = video.subclip(start_time, end_time)
            clipped.append(clip)

            if do_save_each_clip:
                name_clip = self.directory_clip_join + self.separator + self.__index_video_name(video_name, count)
                clip.write_videofile(name_clip,
                                     threads=4, fps=24,
                                     codec=self.video_codec,
                                     preset=self.compression,
                                     ffmpeg_params=["-crf", self.video_quality])
        self.__join_clips(clipped, video_name)
        video.close()

        if delete_ytb_vid_after:
            if os.path.exists(full_vid_name):
                os.remove(full_vid_name)


    def __index_video_name(self, vid_name, index):
        index_last_dot = vid_name.rfind('.')
        list_vid_name = list(vid_name)
        list_vid_name.insert(index_last_dot, "_" + str(index))
        new_vid_name = ''.join(list_vid_name)
        return new_vid_name


    def __subtract_delta_and_return_string(self, str_time, delta_time):
        if self.pattern_hmsf.match(str_time):
            format_for_time = '%H:%M:%S.%f'
        elif self.pattern_msf.match(str_time):
            format_for_time = '%M:%S.%f'
        elif self.pattern_ms.match(str_time):
            format_for_time = '%M:%S'

        time_object = datetime.strptime(str_time, format_for_time)
        time_object = time_object + timedelta(milliseconds=delta_time)

        if format_for_time == '%M:%S':
            format_for_time = '%M:%S.%f'
        back_to_string = datetime.strftime(time_object, format_for_time)
        return back_to_string

