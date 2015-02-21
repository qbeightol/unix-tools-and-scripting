gawk ' BEGIN{FS = ",|:"}
       NR > 1 {if ($2 == "start work") 
                  Activity["work"]-= ($3+($4/60));
               else if ($2 == "end work")
                  Activity["work"]+= ($3+($4/60));
               if ($2 == "start run") 
                  Activity["run"]-= ($3+($4/60));
               else if ($2 == "end run")
                  Activity["run"]+= ($3+($4/60));
               if ($2 == "start farmers market") 
                  Activity["farmers market"]-= ($3+($4/60));
               else if ($2 == "end farmers market")
                  Activity["farmers market"]+= ($3+($4/60));
              }
       END {for (a in Activity) print a ": " Activity[a] " hours"}
     ' activity_log.csv
