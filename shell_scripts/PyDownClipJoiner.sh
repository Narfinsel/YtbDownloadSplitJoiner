#!/bin/sh


#EXAMPLES OF HOW TO RUN IN CMD
:'
PyDownClipJoiner.sh --dl "C:\Users\User\Desktop\Download_Ytb" --dest "C:\Users\User\Desktop\Download_Ytb\ClippedJoined" --url https://www.youtube.com/watch?v=f9zyenX2PWk --res 720p --codec libx264 --qual 24 --comp slow --save True --ext 500 --seg "0:30-00:45,2:30-2:45"

PyDownClipJoiner.sh --dl "C:\Users\User\Desktop\Download_Ytb" --dest "C:\Users\User\Desktop\Download_Ytb\ClippedJoined" --url https://www.youtube.com/watch?v=f9zyenX2PWk --res 720p --codec libx264 --qual 24 --comp slow --save True --ext 500 --seg "0:30-00:45,1:00-01:15,2:30-2:45"

PyDownClipJoiner.sh --url https://www.youtube.com/watch?v=f9zyenX2PWk --save True --ext 500 --seg "0:30-00:45,1:00-01:15,2:30-2:45"

PyDownClipJoiner.sh --url https://www.youtube.com/watch?v=f9zyenX2PWk --ext 500 --seg "0:30-00:45,1:00-01:15,2:30-2:45"
---> IGNORE WHAT IS ABOVE THIS <---

'

#SCRIPT

#Python Script
PY_SCRIPT_SPLIT_JOIN="D:\___Storage\__Programing\Python\YtbDownloadSplitJoiner\YtbDownloadClipperJoiner.py"
SLEEP_AFTER_DONE=50


#Set start values so that reading can be done even if argument is absent
dir_download=""
dir_clip_clips=""
url=""
resolution=""
codec=""
quality=""
compression=""
time_ext=""
save_each_clip=""
clip_segments=""


#Read the argument values
while [ $# -gt 0 ]
	do
		case "$1" in
			--dl) dir_download="$2"; shift;;
			--dest) dir_clip_clips="$2"; shift;;
			--url) url="$2"; shift;;
			--res) resolution="$2"; shift;;
			--codec) codec="$2"; shift;;
			--qual) quality="$2"; shift;;
			--comp) compression="$2"; shift;;
			--save) save_each_clip="$2"; shift;;
			--ext) time_ext="$2"; shift;;
			--seg) clip_segments="$2"; shift;;
			--) shift;;
		esac
    shift;
done


#Default values for arguments
__dir_download="C:\Users\User\Desktop\Download_Ytb"
__dir_clip_clips="C:\Users\User\Desktop\Download_Ytb\ClippedJoined"
__resolution="720p"
__codec="libx264"
__quality=24
__compression="slow"
__time_ext=0
__save_each_clip=False



#Set arguments to default if absent
if [$dir_download == ""];then
	dir_download=$__dir_download
fi
if [$dir_clip_clips == ""]; then
	dir_clip_clips=$__dir_clip_clips
fi
if [$resolution == ""]; then
	resolution=$__resolution
fi
if [$codec == ""]; then
	codec=$__codec
fi
if [$quality == ""]; then
	quality=$__quality
fi
if [$compression == ""]; then
	compression=$__compression
fi
if [$time_ext == '']; then
	time_ext=$__time_ext
fi
if [$save_each_clip == ""]; then
	save_each_clip=$__save_each_clip
fi
if [$clip_segments == ""]; then
	clip_segments=$__clip_segments
fi


#Print arguments
echo ""
echo " Download Dir  : $dir_download";
echo " Clip Dir      : $dir_clip_clips";
echo " URL           : $url";
echo " Resolution    : $resolution";
echo " Video Codec   : $codec";
echo " Video Quality : $quality";
echo " Compression   : $compression";
echo " Extend Time   : $time_ext";
echo " Save Clips    : $save_each_clip";
echo " Segments      : $clip_segments";
echo ""


#Run Python Script
python $PY_SCRIPT_SPLIT_JOIN --dl $dir_download --dest $dir_clip_clips  --url $url --res $resolution --codec $codec --qual $quality --comp $compression --save $save_each_clip --ext $time_ext --seg $clip_segments


#Finish
echo "DONE"
sleep $SLEEP_AFTER_DONE


