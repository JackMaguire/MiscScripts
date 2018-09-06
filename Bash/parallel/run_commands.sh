#!/bin/bash

file=$1
num_processors=$2

echo running $file with $num_processors processors

num_commands=`cat $file | wc -l`

for x in `eval echo {1..$num_commands}`; do
    echo $x;
done | xargs -n 1 -P $num_processors ./run_nth_line.sh $file
