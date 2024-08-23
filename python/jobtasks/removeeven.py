def func(l):
    for i, c in enumerate(l):
        if isinstance(c, int) and c % 2 == 0:
            del l[i]
    return l

if __name__ == "__main__":
    l = [1, 2, 3, 4, None, 'test', True,(1,2,3)]
    l = func(l)
    print("result is:")
    print(str(l))
