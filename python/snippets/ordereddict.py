import json

from collections import OrderedDict


# An OrderedDict internally maintains a doubly linked list that orders the keys according
# to insertion order.

d = OrderedDict()

d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"

for key in d:
 print(key, d[key])


json.dumps(d)
# '{"foo": 1, "bar": 2, "spam": 3, "grok": 4}'

