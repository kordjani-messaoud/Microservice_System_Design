#! /bin/bash

containers=`docker ps -aq`

for container in $containers
do
    docker rm $container
done