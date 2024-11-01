#!/bin/bash



packages=`pip freeze | tr -s = | cut -d = -f 1`


for package in $packages
do
	pip show $package | grep -E 'Requires:|Name:'
done
