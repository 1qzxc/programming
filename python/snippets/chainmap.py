a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }


from collections import ChainMap
c = ChainMap(a,b)
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)

values = ChainMap()
values['x'] = 1

# Add a new mapping
values = values.new_child()
values['x'] = 2

# Add a new mapping
values = values.new_child()
values['x'] = 3