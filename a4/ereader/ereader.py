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
        back_line(file)

# moves forward [n] lines in [file]
def fwd_lines(file, n): 
    for i in range(0, n, 1): 
        file.readline()

# prints the next [n] lines in [file]
def print_lines(file, n):
    for i in range(0, n, 1):
        print file.readline(),
    # print "\n",

# prints ======= ... for 80 chars
def print_sep():
    for i in range(0, 80, 1):
        sys.stdout.write("=")
    

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

# lookup our progress in the text file #####################################

text = open(text_path, "r") 
hash =  hashlib.md5(text.read()).hexdigest();

if not hash in progress_dict:
    progress_dict[hash] = 0
    write_dict(progress_dict, rc_loc)

loc = int(progress_dict[hash]) 

text.read()
max_loc = text.tell()
text.seek(0, 0)
fwd_lines(text, loc)



# display loop #############################################################

while True:
    loc_before_printing = text.tell()
    os.system("clear")
    print_lines(text, lines_per_page)
    print_sep()
    command = raw_input(":")
    if   command == "n":
        if text.tell() == max_loc:
            back_lines(text, lines_per_page)
        elif loc_before_printing != text.tell():
            progress_dict[hash] = int(progress_dict[hash]) + lines_per_page
            write_dict(progress_dict, rc_loc)
    elif command == "p":
        back_lines(text, 2 * lines_per_page)
        if loc_before_printing != text.tell():
            progress_dict[hash] = int(progress_dict[hash]) - lines_per_page
            write_dict(progress_dict, rc_loc)
    elif command == "q":
        sys.exit()
    else:
        print "invalid command"

