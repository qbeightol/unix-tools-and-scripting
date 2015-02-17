#!/bin/bash

# see if you can figure out what went wrong when I tried to delete punctuation
# using tr -d [:punct:]

# finds the 10 most common words within the tweets folder
cat tweets/* | tr ' ' '\n' | sort | uniq -c | sort -rn | head -10 > most_common.txt
