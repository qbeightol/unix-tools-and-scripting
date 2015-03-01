#! /bin/bash
today=`date | gawk '{print $1}'`
gawk -v today=$today '{FS = " : "}{if($1==today) print $2}' myweekly_act.txt | mailx -s "reminder!" qeb2@cornell.edu
