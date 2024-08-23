def func(s):
    if len(s) <= 4 and not s.isdigit():
            s = masq_one(s)
            return s
    if len(s) <= 6 and s.isdigit():
        return s
    s = masq_two(s)
    return s

def masq_one(s):
    temp = list(s)
    temp[1:-1] = '*' * (len(temp) - 2) # two symbols left unmasked so the number of stars '*' equals n - 2
    s = "".join(temp)
    return s

def masq_two(s):
    temp = list(s)
    temp[2:-2] = '*' * (len(temp) - 4) # four symbols left unmasked hence n-4
    s = "".join(temp)
    return s

if __name__ == "__main__":
    s = '1234567'
    result = func(s)
    print(result)
    s = 'aaaaaaa'
    result = func(s)
    print(result)
    s = '123456'
    result = func(s)
    print(result)
    s = 'aaaaaa'
    result = func(s)
    print(result)
    s = '12345'
    result = func(s)
    print(result)
    s = 'aaaaa'
    result = func(s)
    print(result)
    s = '12abcdef56'
    result = func(s)
    print(result)
    s = '12ab'
    result = func(s)
    print(result)
    s = '1221'
    result = func(s)
    print(result)
    s = 'abcd'
    result = func(s)
    print(result)
    s = '123sdaqwe123123sadasdas213123'
    result = func(s)
    print(result)
    s = '1111111111111111111111111111111'
    result = func(s)
    print(result)
    s = 'aaa'
    result = func(s)
    print(result)
    s = '1a1'
    result = func(s)
    print(result)
    s = '121'
    result = func(s)
    print(result)
    s = '1a'
    result = func(s)
    print(result)
    s = '11'
    result = func(s)
    print(result)
    s = 'aa'
    result = func(s)
    print(result)
    s = '1'
    result = func(s)
    print(result)
    s = 'a'
    result = func(s)
    print(result)
