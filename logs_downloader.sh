#!/bin/bash

URL="$1"
BUILD_NUMBER=`echo $URL | cut -d/ -f14`
DEVICE=`echo $URL | cut -d/ -f9`
mkdir -p ~/log_files
cd ~/log_files
# echo $URL
# echo $BUILD_NUMBER
for i in `seq 1 $BUILD_NUMBER`;
do
    wget -nv ""
    mv opera_output.out "$i"
    # echo $i
done

echo "\nFINISHED\n"
