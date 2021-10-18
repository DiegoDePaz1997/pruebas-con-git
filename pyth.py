#comienzo del proyecto

x = input('hola mundo')

if x:
    print('como te va')
else:
    print('pues no, no te queria hablar')

for i in range(len(x)):
    if i == 43:
        break
    print('hola mundo ', i)
else:
    print('todo termino bien')
    print('cosas'*3)