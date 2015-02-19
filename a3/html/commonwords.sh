#! /bin/bash

cat superbowl.txt | tr '[A-Z] ' '[a-z]\n' > pass1.txt
grep '[^[:space:]]\+' pass1.txt > pass2.txt

cat pass2.txt | sort | uniq -c | sort -rn | head -100 > commonwords.txt

# clean up 
rm pass1.txt
rm pass2.txt


