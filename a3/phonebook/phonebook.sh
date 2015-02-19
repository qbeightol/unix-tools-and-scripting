#! bin/bash

separator="\([[:space:]]\|\.\|-\)\?"
cat phone-data.txt | grep -o "\((\?[0-9]\{3\})\?\)\?"$separator"[0-9]\{3\}"$separator"[0-9]\{4\}"