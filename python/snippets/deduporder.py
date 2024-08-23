# hashable types:

def dedupe(items):
 seen = set()
 for item in items:
     if item not in seen:
        yield item
        seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
list(dedupe(a))

# unhashable types: 

#def dedupe(items, key=None):
#    seen = set()
#    for item in items:
#        val = item if key is None else key(item)
#        if val not in seen:
#            yield item
#            seen.add(val)