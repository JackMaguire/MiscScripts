#!/bin/bash

file=$1
line=$2

cmd=`cat $file | head -n $line | tail -n 1`
eval $cmd
