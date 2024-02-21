#!/bin/sh

#Python Script
PY_SCRIPT="D:\___Storage\__Programing\Python\YtbDownloadSplitJoiner\YtbDownloadClipperJoiner.py"

#Read the argument values
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



while [ $# -gt 0 ]
	do
		case "$1" in
			--dl) dir_download="$2"; shift;;
			--clip) dir_clip_clips="$2"; shift;;
			--url) url="$2"; shift;;
			--res) resolution="$2"; shift;;
			--cod) codec="$2"; shift;;
			--qual) quality="$2"; shift;;
			--comp) compression="$2"; shift;;
			--ext) time_ext="$2"; shift;;
			--save) save_each_clip="$2"; shift;;
			--seg) clip_segments="$2"; shift;;
			--) shift;;
		esac
    shift;
done


__resolution="720p"
__codec="libx264"
__quality=24
__compression="slow"
__time_ext=400
__save_each_clip="True"
__clip_segments='0:30-00:45, 1:00-01:15, 2:30-2:45'
__dir_download="C:\Users\User\Desktop\Download_Ytb"
__dir_clip_clips="C:\Users\User\Desktop\Download_Ytb\ClippedJoined"


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


echo ""
echo " Download Dir  : $dir_download";
echo " Clip Dir      : $dir_clip_clips";
echo " URL           : $url";
echo " Resolution    : $resolution";
echo " Video Codec   : $codec";
echo " Video Quality : $quality";
echo " Compression   : $compression";
echo " Extend Time   : $time_ext";
echo " Save Clips?   : $save_each_clip";
echo " Segments      : $clip_segments";
echo ""

sleep 10



:'
python $PY_SCRIPT --dl_dir $dir_download --dest_dir $dir_clip_clips  --url $url --res $resolution --v_codec $codec --v_quality $quality --compression $comp --extend_ms $time_ext --save_clips $save_each_clip --segments $clip_segments

python $PY_SCRIPT --url $url --extend_ms $time_ext --save_clips $save_each_clip --segments $clip_segments

sleep 5
'



:'

PyClipJoiner.sh --dl "C:\Users\User\Desktop\Download_Ytb" --clip "C:\Users\User\Desktop\Download_Ytb\ClippedJoined4" --url https://www.youtube.com/watch?v=f9zyenX2PWk --res 720p --cod libx264 --qual 24 --comp slow --save True --ext 500 --seg "0:30-00:45, 1:00-01:15, 2:30-2:45"

PyClipJoiner.sh --url https://www.youtube.com/watch?v=f9zyenX2PWk --save True --ext 500 --seg "0:30-00:45, 1:00-01:15, 2:30-2:45"

'
