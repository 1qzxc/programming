

#! /usr/bin/python

# Role : Add or subtract delay to a srt file
# Author : http://shebangthedolphins.net/
# 1.0 first version

import argparse
import re, sys
from datetime import datetime, timedelta
import shutil
from tempfile import mkstemp
from os import path

###START PARSER : https://docs.python.org/3/library/argparse.html
parser = argparse.ArgumentParser(description='add/subtract delay on a srt file',prog='shebangthesubtitles.py', usage='%(prog)s /movies/mysubtitle.srt -1.400')
parser.add_argument('file', help='srt file path')
parser.add_argument('delay', help='delay in seconds with 0.000 format')
args = parser.parse_args()
###END PARSER

###FUNCTION
def timeop (hours, minutes, seconds, milliseconds, delay):
        "function which add or subtract delayed time then return result"
        time_src = datetime(year=1983, month=12, day=12, hour=int(hours), minute=int(minutes), second=int(seconds), microsecond=int(milliseconds)).timestamp()
        result = time_src + delay
        return result

###CHECK ARGUMENTS
try:
        delay = float(args.delay)
except:
        print("Error, float argument needed.")
        parser.print_help()
        sys.exit(1)

if not path.exists(args.file):
        print("Error, file doesn't exist.")
        parser.print_help()
        sys.exit(1)


fs = open(args.file, 'r') #open srt file, read mode
fd, name = mkstemp() #returns a tuple containing an OS-level handle to an open file and the absolute pathname of that file, in that order.
fout = open(name, 'w') #open temp file, write mode
while 1:
        txt = fs.readline()
        if re.match(".*-->.*", txt): #if ".*-->.*" characters is in current line
                seq=txt.split(" --> ")
                hours_start, minutes_start, seconds_start = seq[0].split(":")
                hours_start = hours_start[-1:]
                seconds_start, milliseconds_start = seconds_start.split(",")
                milliseconds_start = int(milliseconds_start) * 1000
                new_start = timeop(hours_start, minutes_start, seconds_start, milliseconds_start, delay)

                hours_end, minutes_end, seconds_end = seq[1].split(":")
                hours_end = hours_end[-1:]
                seconds_end, milliseconds_end = seconds_end.split(",")
                milliseconds_end = int(milliseconds_end) * 1000
                new_end = timeop(hours_end, minutes_end, seconds_end, milliseconds_end, delay)

                txt = re.sub(seq[0], datetime.fromtimestamp(new_start).strftime('%H:%M:%S,%f')[:-3], txt)
                txt = re.sub(seq[1], datetime.fromtimestamp(new_end).strftime('%H:%M:%S,%f')[:-3], txt) + "\n"
                fout.write(txt) #write to tmp file
        else:
                fout.write(txt) #write to tmp file

        if txt == "":
                break
fout.close() #close tmp file
shutil.move(name, args.file.split(".srt")[0] + "_new.srt") #copy tmp file to srtfile_new.srt
fs.close() #close srt file



#import sys
#
#
#
#def main(filename)
#    with open(filename, 'w+') as file:
#        integer = int(file.readline())
#        print(integer)
#        # sets the file pointer? at the first byte 
#        # so that the write method will overwrite the first bytes of data
#        file.seek(0)
#        file.write(str(integer + 1))
#   
#
#if __name__ == "__main__":
#    filename = sys.argv[0]
#    main(filename)
