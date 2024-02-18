
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


class VideoParserImprecise:
    def __init__(self, directory_video, directory_clip_join):
        self.directory_video = directory_video
        self.directory_clip_join = directory_clip_join

    def __join_clips(self, clips_list, video_name):
        if len(clips_list) == 0:
            return
        final = VideoFileClip(clips_list[0])
        for i in range(1, len(clips_list)):
            clip = VideoFileClip(clips_list[i])
            final = concatenate_videoclips([final, clip])
            del clip
        final.write_videofile(self.directory_clip_join + '/' + video_name)

    def parse_video(self, video_name, segments):
        count = 0
        clipped = []
        for segment in segments:

            clip = self.__clip_segment(video_name, segment, count)
            clipped.append(clip)
            count+=1

        self.__join_clips(clipped, video_name)

    def __clip_segment(self, video_name, segment, index):
        origin = self.directory_video + "/" + video_name
        new_vid_name = self.__index_video_name(video_name, index)
        destination = self.directory_clip_join + "/" + new_vid_name
        ffmpeg_extract_subclip(
            origin,
            self.__convert_string_to_seconds(segment[0]),
            self.__convert_string_to_seconds(segment[1]),
            destination)
        if os.path.isfile(destination):
            return destination
        else:
            return "N/A"

    def __convert_string_to_seconds(self, string_timeframe):
        # format is 00:00:00 or 00:00
        list_durations = str(string_timeframe).split(":")
        hour, minute, second = 0, 0, 0

        if len(list_durations) == 3:
            hour = int(list_durations[0])
            minute = int(list_durations[1])
            second = int(list_durations[2])
        elif len(list_durations) == 2:
            minute = int(list_durations[0])
            second = int(list_durations[1])
        return hour*3600 + minute*60 + second

    def __index_video_name(self, vid_name, index):
        index_last_dot = vid_name.rfind('.')
        list_vid_name = list(vid_name)
        list_vid_name.insert(index_last_dot, "_" + str(index))
        new_vid_name = ''.join(list_vid_name)
        return new_vid_name