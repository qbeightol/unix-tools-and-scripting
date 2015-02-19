#! /bin/bash

cat frankenstein.txt | tr '[A-Z]\n' '[a-z] ' | tr -d '[:punct:]' > pass1.txt
sed 's/ \+/\n/g' pass1.txt > pass2.txt 
grep -F -v -f prepositions.txt pass2.txt > nopreps.txt
sort nopreps.txt | uniq -c | sort -rn | head -100 > frankenprepos.txt

# clean up 
rm pass1.txt
rm pass2.txt
rm nopreps.txt

