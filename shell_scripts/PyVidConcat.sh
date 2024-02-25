#!/bin/sh
#!/bin/s

#EXAMPLES OF HOW TO RUN IN CMD
:'
PyVidsConcat.sh --dir "C:\Users\User\Desktop\Download_Ytb\ClippedJoined" --name "Chupacabra" --suff mp4 --res 720p --codec libx264 --qual 24 --comp slow

PyVidConcat.sh --dir "C:\Users\User\Desktop\Download_Ytb\ClippedJoined" --name "Chupacabra" --suff mp4

PyVidConcat.sh --name "Chupacabra" --suff mp4

PyVidConcat.sh --name "Chupacabra"

PyVidConcat.sh
---> IGNORE WHAT IS ABOVE THIS <---

'

#Python Script
PY_SCRIPT_CONCAT="D:\___Storage\__Programing\Python\YtbDownloadSplitJoiner\ConcatenateAllClipsFromDir.py"
SLEEP_AFTER_DONE=10


#Set start values so that reading can be done even if argument is absent
dir_concat=""
vid_name=""
suffix=""
resolution=""
codec=""
quality=""
compression=""


#Read the argument values
while [ $# -gt 0 ]
	do
		case "$1" in
			--dir) dir_concat="$2"; shift;;
			--name) vid_name="$2"; shift;;
			--suff) suffix="$2"; shift;;
			--res) resolution="$2"; shift;;
			--codec) codec="$2"; shift;;
			--qual) quality="$2"; shift;;
			--comp) compression="$2"; shift;;
			--) shift;;
		esac
    shift;
done


#Default values for arguments
__dir_concat="C:\Users\User\Desktop\Download_Ytb\ClippedJoined"
__vid_name="PyVidConcat_new"
__suffix="mp4"
__resolution="720p"
__codec="libx264"
__quality=24
__compression="slow"


#Set arguments to default if absent
if [$dir_concat == ""];then
	dir_concat=$__dir_concat
fi
if [$vid_name == ""]; then
	vid_name=$__vid_name
fi
if [$suffix == ""]; then
	suffix=$__suffix
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



#Print arguments
echo ""
echo " Concat Dir    : $dir_concat";
echo " Video Name    : $vid_name";
echo " Suffix        : $suffix";
echo " Resolution    : $resolution";
echo " Video Codec   : $codec";
echo " Video Quality : $quality";
echo " Compression   : $compression";
echo ""


#Run Python Script
python $PY_SCRIPT_CONCAT --dir $dir_concat --name $vid_name  --suff $suffix --res $resolution --codec $codec --qual $quality --comp $compression


#Finish
echo "DONE"
sleep $SLEEP_AFTER_DONE