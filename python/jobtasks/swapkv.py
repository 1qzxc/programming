def swap_func(d):
    d = {v: k for k, v in d.items()}
    return d

if __name__ == "__main__":
    d = { "one":1, "two":2,"three":3, "four":4} 
    d = swap_func(d)
    print("result is:")
    print(str(d))
