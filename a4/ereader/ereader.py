#! /usr/bin/python
#  ereader.py

import csv, hashlib, os, sys

# helper functions #########################################################

# reads a character from a file without affecting the file's offset/position
def read_char_wo_move(file):
    char = file.read(1)
    file.seek(-1, 1)
    return char
                
# moves the file's position one character back; if the file's position is 
# already at the front, the position is unchanged
def move_back_char(file):
    if file.tell() != 0: 
        file.seek(-1, 1)

# moves back a line in the text file
def back_line(file): 
    # assume the previous character was a newline
    move_back_char(file)
    move_back_char(file)
    char = read_char_wo_move(file)

    while char != "\n" and file.tell() > 0:
        move_back_char(file)
        char = read_char_wo_move(file)
                                                    
    if char == "\n":
        file.seek(1, 1)

# moves back [n] lines in the text file
def back_lines(file, n):
    for i in range(0, n, 1):
        print i
        print file.tell()
        back_line(file)

# moves forward [n] lines in [file]
def fwd_lines(file, n): 
    for i in range(0, n, 1): 
        file.readline()

# prints the next [n] lines in [file]
def print_lines(file, n):
    for i in range(0, n, 1):
        print i,
        print file.readline(),
    print "\n",

# writes [dict] as csv file stored at [loc]
def write_dict(dict, loc):
    loc_file = open(loc, "w")
    csv.writer(loc_file).writerows(dict.items()) 
    loc_file.close()
    
# start of script ##########################################################

# check comand line arguments ##############################################

if len(sys.argv) > 3 and sys.argv[1] == "-n":
    lines_per_page = int(sys.argv[2]) 
    text_path = sys.argv[3]
elif len(sys.argv) > 1:
    lines_per_page = 40
    text_path = sys.argv[1]
else:
    sys.exit("ereader.py expects at least one argument") 

# build a dictionary out of reader_rc ######################################

rc_loc = os.path.expanduser("~/.reader_rc") 

# if the rc file doesn't already exist, the following command will create a
# new file without overwriting it (note: the rc_file.seek(0, 0) is a little
# clumsy, but it seems like the least painful option given how we want the
# file to work, and the modes available for files)

rc_file = open(rc_loc, "a+")
rc_file.seek(0,0)
rc_reader = csv.reader(rc_file)
progress_dict= {}

for kv in iter(rc_reader):
    progress_dict[kv[0]] = kv[1]

rc_file.close()

print progress_dict

# lookup our progress in the text file #####################################

text = open(text_path, "r") 
hash =  hashlib.md5(text.read()).hexdigest();

if not hash in progress_dict:
    progress_dict[hash] = 0
    write_dict(progress_dict, rc_loc)

print progress_dict
loc = int(progress_dict[hash]) 
print loc
print text.tell()
text.seek(0, 0)
print text.tell()
fwd_lines(text, loc)
print text.tell()

# display loop #############################################################



while True:
    command = raw_input(":")
    if   command == "n":
        print lines_per_page
        print text.tell()
        print_lines(text, lines_per_page)
        progress_dict[hash] = int(progress_dict[hash]) + 40
        print "writing dictionary"
        write_dict(progress_dict, rc_loc)
        print "finished writing"
    elif command == "p":
        print int(progress_dict[hash]) - 40
        print 2 * lines_per_page
        back_lines(text, 2 * lines_per_page)
        print_lines(text, lines_per_page)
        progress_dict[hash] = int(progress_dict[hash]) - 40
        print "writing dictionary"
        write_dict(progress_dict, rc_loc)
        print "finished writing"
    elif command == "q":
        sys.exit()
    else:
        print "invalid command"


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
