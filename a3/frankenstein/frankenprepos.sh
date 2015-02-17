#! /bin/bash

# finds the 10 most common words in letter 3 of Frankenstein (ignores 
# punctuation, and capitilization) 
cat frankenstein.txt | tr '[A-Z]\n' '[a-z] ' | tr -d '[:punct:]' | sed 's/ \+/\n/g' | sort > words.txt

uniq -c  prepositions.txt > counted_preps.txt

sed -r 's/[[:space:]]+([[:digit:]]+) /\1\t/' counted_preps.txt > counted_preps2.txt


join -1 2 -2 1 -a 1 words.txt prepositions.txt > table.txt
