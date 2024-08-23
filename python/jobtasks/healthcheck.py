import sys
import requests
import time
import urllib
import validators

if __name__ == "__main__":
    counter = int(sys.argv[1])
    url = sys.argv[2]
    if validators.url(url):
        while(True):
            r = requests.get(url)    
            if r.status_code == 200:
                print("Checking '" + url + "'. Result: OK(" + str(r.status_code) +")")
            if r.status_code != 200:
                print("ERR({" + str(r.status_code) + "})")
            time.sleep(counter)
    else:
        print("URL parsing error: " + url)


