#! /bin/bash

wget http://www.cs.cornell.edu/courses/cs2043/2015sp/assignments/superbowl.html

# remove html tags: 
sed 's/<[^>]*>//g' superbowl.html > superbowl.txt 
