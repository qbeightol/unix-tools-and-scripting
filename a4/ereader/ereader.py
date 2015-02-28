#! /usr/bin/python
#  ereader.py

import os, sys

reader_rc_path = os.path.expanduser("~/.reader_rc")
# if the file doesn't already exist, open will create a new file
# think about adding a "r" to the mode for the file
progress = open(reader_rc_path, "w")

# check comand line arguments

if sys.argv[1] == "-n":
    lines_per_page = sys.argv[2] 
    text_path = sys.argv[3]
else:
    lines_per_page = 40
    text_path = sys.argv[1]


print text_path

while True:
    command = input(":")
    if   command == "n": 
        print "next"
    elif command == "p":
        print "previous"
    else:
        print "invalid command"
    end


# need to parse command line arguments
# safe to assume that "-n" comes first?

# once I have a file, I'll need to hash it, and look up its page # in the
# reader_rc file

# I'll need to update the reader_rc file (either by changing the bindings
# or by adding new entries)

# I'll also need to create a file object for the input file (and based off 
# reader_rc, I might need to skip ahead to a particular line)

# I'll need to read off a specified #of lines

# I'll need to be able to move backwards/forwards and respond to key strokes


# 
