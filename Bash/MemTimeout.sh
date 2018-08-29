#!/bin/bash

#This script monitors all processes where the command contains the first agument (token)
#We kill the process if the memory usage (measured by percent) of that process exceeds
#the second argument (mem_percent_limit). This script is an infinite loop.

#There is an optional third argument, death_file. This infinite loop will stop looping
#if that file exists. Intended use will be in conjunction with the following command pattern:
#$ ./potentially_dangerous_command ; touch kill_loop
#$ ./MemTimeout.sh poten 25 kill_loop

token=$1
mem_percent_limit=$2
if [[ "$#" -gt "2" ]]; then
    death_file=$3
fi

while true; do
    for x in `ps -all | grep $1 | awk '{print $4}'`; do
	mem_percent=`ps -ef -o pid,%mem $x | tail -n1 | awk '{print $2}'`
	need_to_kill=`echo "$mem_percent > $mem_percent_limit" | bc`
	if [[ "$need_to_kill" -eq "1" ]]; then
	    echo "Killing PID $x for using $mem_percent percent of the available memory"
	    kill $x
	fi
    done
    sleep 10
    if [ -f $death_file ]; then
	exit 0
    fi
done
