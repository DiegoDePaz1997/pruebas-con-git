import random as r
import pprint as p
print(r.random())

x = [r.random for i in range(10)]
print(x)
p.pprint(x)

p.pprint('otras cosas')

print('que solo ocupan espacio')



x = [i**2 for i in range(10) if i%2 ==0]
print(x)
print(' '.join(x))


print('esto va a estar en master')
print('esto no va a esta en python_generador')