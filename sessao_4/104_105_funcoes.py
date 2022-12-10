"""
Argumentos nomeados e não nomeados em funções python
argumentos nomeados tem nome com sinal de igual
argumento não nomeado recebe apenas o argumento (valor)
"""

def Python(a, b, c):
    return(a+b-c)


a=Python(1, 2, 3)
print(a)


a=Python(b=1, c=2, a=3)
print(a)


print(1, 2, 3, sep='-')
print(1, 2, 3, sep='')
print(1, 2, 3)