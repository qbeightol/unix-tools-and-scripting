#!bin/bash

# again, think about ways you could make this code more flexible

# counts the minimum number of chars. in a tweet
wc -c tweets/* | sort -n | head -1 | sed 's/ *\([[:digit:]]\+\) [^[:space:]]\+/\1/' > min_chars.txt

# counts the maximum number of chars. in a tweet
wc -c tweets/* | sort -rn | head -2 | tail -1 | sed 's/ *\([[:digit:]]\+\) [^[:space:]]\+/\1/' > max_chars.txt

# finds the average number of chars. in a tweet 
average=`wc -c tweets/* | sort -rn | head -1 | sed 's/ *\([[:digit:]]\+\) total/\1\/2000/'`
echo $average | bc > avg_chars.txt
