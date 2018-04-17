#!/bin/bash

message=""

if [ "$#" == "0" ]; then
    message="NOTIFICATION"
else
    message=$1
fi

osascript /Users/jack/Dropbox/add_reminder.scpt $message