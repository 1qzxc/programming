#!/bin/python3


from datetime import datetime, timedelta
import logging



path = 'logfile.log'

def generateLogs():
    with open(path, 'a') as f:
        for i in range(1, 10):
            d = datetime.today().date() - timedelta(days=i)
            print(str(d), file=f)

def cutLogs():
    
    try:
        with open(path, 'r+') as f:
            lines = f.readlines()
            base = datetime.today().date()
            date_list = [base - timedelta(days=x) for x in range(7)]
            #print(date_list)
            f.seek(0)
            for line in lines:
                if datetime.strptime(line.strip(), "%Y-%m-%d").date() in date_list:
                    print("keeping : " + line)
                    f.write(line)
            f.truncate()          
    except IOError as e:
        print('Failure', e)
    

if __name__ == "__main__":
    generateLogs()
    cutLogs()





