#! /usr/bin/bash


while true
do
url="https://web.archive.org/web/20140301052344/http://www.movies.com/rss-feeds/top-ten-box-office-rss"
title_html='<title><\!\[CDATA\[[0-9]\{1,2\}.*</title>'
description_html='<description>.*</description>'
curl $url 2> /dev/null | grep -o $title_html | sed "s/<title><!\[CDATA\[//g" | sed "s/\]\]><\/title>//g"
synopsis=$(curl $url 2> /dev/null | grep -o $description_html | sed "s/<br.*>//g" | sed "s/<description><!\[CDATA\[//g" | sed "s/\]\]><\/description>//g")
IFS=$'\n'
array=($synopsis)
read -p "Choose a movie (1-10) > " mov_num
printf "Movie $mov_num\nSynopsis\n\n"
echo ${array[$mov_num]}
read -p "Please enter to return"
done