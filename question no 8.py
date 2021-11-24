import itertools 
import collections
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d3= collections.defaultdict(int)

for key, val in itertools.chain(d1.items(), d2.items()):
    d3[key] += val
      
print(dict(d3))