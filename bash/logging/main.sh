#!/bin/bash

filename=logfile.log

function generate_logfile() {
# need current date to use it for log generation
  temp=$(date +%s)

# decrement one day for each log entry
  decrement=100000 

  for i in {1..100}
  do
    temp=$(($temp-$decrement))
    date -d @$temp '+%Y-%m-%d' >> $filename
  done

  echo "logfile $filename has been generated"
}

function cut_logfile() {
    echo "deleting logs from a logfle older than 7 days"
    curr=$(date +%s)
    temp=$(($curr-604800))
    
    while read line; do
        linedate=$(echo $line | awk '{ print $1 }')
        inseconds=$(date -d $linedate '+%s')
        if [ "$inseconds" -lt "$temp" ]; then
            echo "removing: " $line
            sed -i "/$line/d" "$filename"
        fi
    done <$filename
    echo "--------- result ---------"
    cat $filename

#    awk -F'[,.]' 'NR==1 || (systime()-mktime($3" "$2" "$1" 0 0 0")) <= 7*24*60*60' $filename
#        awk '$0 <= "$temp"'
}

function main {
    echo "You have started the bash solution"
    echo "Written by Mikhail Morozov"
    generate_logfile
    cut_logfile
}

main
