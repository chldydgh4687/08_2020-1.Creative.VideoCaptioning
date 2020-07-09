#!/bin/sh

#made by : yonghoChoi
#-----------------------------------------------------------#
# This shell script convert MSVD into low-quality MSVD.
#-----------------------------------------------------------#

echo "Convert MSVD into Low-quality MSVD...................."

msvd_dir= 'your msvd path folder'
move_dir= 'new output folder'

for entry in $msvd_dir/*
do
	echo "$entry converting..................."
	filepathname="$entry"
	filename=`basename $entry.avi`
	
	ffmpeg -i $filepathname -c:v libx264 -preset slow -crf:v 40 $move_dir/$filename
	
	echo "$move_dir/$filename finish............."
done



