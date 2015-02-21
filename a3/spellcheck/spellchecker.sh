#! /bin/bash

cat $1 | tr -d '[:punct:]' | sed 's/[[:space:]]\+/\n/g' > pass1.txt

grep -F -v -x -i -f english.txt pass1.txt > spellchecker.txt

# clean up
rm pass1.txt

