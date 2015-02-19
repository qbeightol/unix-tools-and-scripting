#! /bin/bash

cat superbowl.txt | tr '[A-Z] ' '[a-z]\n' > pass1.txt
grep '[^[:space:]]\+' pass1.txt > pass2.txt
sed 's/[[:punct:]]|[[:space:]]//g' pass2.txt > pass3.txt

grep -B $1 -A $2 "seahawks\|patriots" pass3.txt > teamwords.txt
# clean up 
rm pass1.txt
rm pass2.txt
rm pass3.txt 
