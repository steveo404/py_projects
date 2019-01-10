#!/bin/bash

public_ip=`wget http://ipecho.net/plain -O - -q`

file1=`cat ipResults.txt`

if [ $public_ip != $file1 ]; then 
	echo $public_ip | mail -s "IP CHANGE" steveo404@gmail.com 
fi


