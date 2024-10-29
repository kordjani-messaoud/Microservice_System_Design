#! /bin/bash




images=`docker image ls | grep mnkordjani99 | tr -s ' ' | cut -f 3 -d ' '`


for image in $images
do
docker image rm $image
done
