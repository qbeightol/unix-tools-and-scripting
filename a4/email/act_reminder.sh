#! /bin/bash
day=date | cut -f 1 -d " " 

list=gawk ' BEGIN NR>1 {if ($1 == $day) $list=$3;} END' myweekly_act.txt

echo $list