numeros = 1, 2, 3, 10, 30, 30, 10


def multiplica(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado


resultado = multiplica(*numeros)
print(resultado)


valor = 2

def ispar(x):
    if x%2 == 0:
        return 'par'
    return 'ímpar'

teste = ispar(valor)
print(teste)
