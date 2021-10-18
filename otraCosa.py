import random as r
import pprint as p
print(r.random())

x = [r.random for i in range(10)]
print(x)
p.pprint(x)