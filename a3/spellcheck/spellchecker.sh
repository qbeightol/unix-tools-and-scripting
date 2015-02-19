#! /bin/bash

cat $1 | tr -d '[:punct:]' | sed 's/[[:space:]]\+/\n/g' > pass1.txt
cat pass1.txt | tr '[A-Z]' '[a-z]' > pass2.txt

cat english.txt | tr '[A-Z]' '[a-z]' > decap_english.txt

grep -F -v -x -f decap_english.txt pass2.txt > spellchecker.txt

# clean up
rm pass1.txt
rm pass2.txt
rm decap_english.txt
