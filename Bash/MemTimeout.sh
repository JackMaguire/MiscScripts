#!/bin/bash

token=$1
mem_percent_limit=$2

for x in `ps -all | grep $1 | awk '{print $4}'`; do
    mem_percent=`ps -ef -o pid,%mem $x | tail -n1 | awk '{print $2}'`
    need_to_kill=`echo "$mem_percent > $mem_percent_limit" | bc`
    if [[ "$need_to_kill" -eq "1" ]]; then
	kill $x
    fi
done
