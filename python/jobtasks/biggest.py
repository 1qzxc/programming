def func(s):
    l = s.split(";")
    n = 0.0
    for num in l:
        if n < float(num):
            n = float(num)
    return n

if __name__ == "__main__":
    s = "123;122.5;0.5;0.0;123.5"
    n = func(s)
    print("biggest num is:")
    print(str(n))
