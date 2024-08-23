# unpacking
p = (4, 5)
x, y = p

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data

grades = [a, b, c, f, a, b, c, f]
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

# unpacking tuples of various length
records = [ ('foo', 1, 2),
            ('bar', 'hello'),
            ('foo', 3, 4), ]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)
    for tag, *args in records:
        if tag == 'foo':
        do_foo(*args)
        elif tag == 'bar':
        do_bar(*args)

# string unpacking
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')








