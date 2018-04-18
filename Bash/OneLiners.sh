#!/bin/bash
exit( 1 ) #just making sure we never run this

#get min and max of csv column
awk -F, -v min=100 -v max=0 '{if($10<min){min=$10}}{if($10>max){max=$10}}END{print min " " max} ' filename