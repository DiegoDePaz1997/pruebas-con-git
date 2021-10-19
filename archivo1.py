import random as r

for i in range(10):
    print(i)



texto = 'esto es un texto'
tex = texto.split().count('esto')


for id,i in enumerate(texto):
    print(f'indice: {id} y la palabra: {i}')
    
x = 'esto lo edite en github'
s = 'por el tama;o de este string, se va a repetir x'

for i in range(len(x)):
    print(x)


print('hola mundo')
print('prueba de sebida al borrar el repositorio local')


def generador(x):
    for i in range(x):
        a = 2**x - 1 
        yield a


def condicion(cond):
    if cond == 0:   return generador(10)
    elif cond == 1: return generador(5)
    elif cond == 2: return generador(3)
    else: return generador(23)


if __name__ == '__main__':
    a = condicion(r.randint(0, 10))
    print(next(a))