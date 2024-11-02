#! /bin/bash

containers=`docker ps -a | grep -v minikube | grep Exited | tr -s ' ' | cut -d ' ' -f1`

docker rm $containers