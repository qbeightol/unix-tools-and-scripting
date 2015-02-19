start=0
awk ' BEGIN{FS = ",|:|"}
	NR > 1 {if $2 = "start" {$start=$4 + ($5/60)}
            if $2 = "end" {Activity[$3]+= ($4 + $5/60)-$start}
           }
    END {for (a in Activity) print a ": " Activity[a] " hours"
    ' activity_log.csv