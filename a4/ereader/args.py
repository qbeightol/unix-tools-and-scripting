#! /usr/bin/python

import sys

print sys.argv

for arg in sys.argv:
    print arg,

lines_per_page = 40

# check if the user included the "-n" flag: 
if sys.argv[1] == "-n":
    lines_per_page = sys.argv[2]

print ""
print lines_per_page
