import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    result = str(r.content).split("\\n")
    while '' in result:
        result.remove('')
    while '\'' in result:
        result.remove('\'')
    dict1 = dict(e.split(':') for e in result)
    print(dict1)
    for k,v in dict1.items():
        if v != ' OK':
            print(" problem : " + k + " is " + v)
            sys.exit(-1)
