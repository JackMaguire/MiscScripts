#!/bin/bash
#SQ is alias on longleaf
while [[ `SQ | grep jackmag | wc -l` -gt 0 ]]; do
    sleep 7200
    GB=$(expr `du -s . | awk '{print $1}'` / 1000000)
    if [[ $GB -gt 50 ]]; then
        remind `pwd`_using_${GB}_GB
    fi
done