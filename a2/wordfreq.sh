#!/bin/bash

# think about ways to make the scripts more robust (e.g. using an explicit 
# number of spaces seems like a bad idea. Likewise assuming the number of 
# tweets is 2000 isn't super flexible)

# counts the number of words in each tweet and stores the smallest count
wc -w tweets/* | sort -n | head -1 | sed 's/ *\([[:digit:]]\+\) [^[:space:]]\+/\1/' > min_words.txt

# same as the code above but saves the largest count in max_words.txt
wc -w tweets/* | sort -rn | head -2 | tail -1 | sed 's/ *\([[:digit:]]\+\) [^[:space:]]\+/\1/' > max_words.txt

# finds the average word count of the 2000 tweets
average=`wc -w tweets/* | sort -rn | head -1 | sed 's/ *\([[:digit:]]\+\) total/\1\/2000/'`
echo $average | bc > avg_words.txt
