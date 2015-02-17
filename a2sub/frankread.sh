#! bin/bash

# finds the 10 most common words in letter 3 of Frankenstein (ignores 
# punctuation, and capitilization) 
cat frankenstein.txt | head -298 | tail -44 | tr '[A-Z] ' '[a-z]\n' | sed 's/ \+\n/g' | sort | uniq -c | sort -rn | head -10 > frankenread.txt
