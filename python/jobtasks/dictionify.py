from collections import Counter

def func(s):
    d = dict(Counter(s).items())
    return d

if __name__ == "__main__":
    s = "special string"
    d = func(s)
    print("result is:")
    print(str(d))

