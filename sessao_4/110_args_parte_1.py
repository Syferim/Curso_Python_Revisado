"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# *args = empacota valores que eu enviar para uma função dentro de uma tupla
# * = desempacota uma tupla para enviar como parametros para uma função

# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


# def soma(x, y):
#    return x + y

def soma(*args):
    total = 0
    args = list(args)
    print(args, type(args))
    for numero in args:
        total = total + numero
    return total


total_soma = (soma(1, 2, 3, 4, 5, 6))
print(total_soma)

total_soma = sum((1, 2, 3, 4, 5, 6))    # tem que haver dois pares de parenteses
print(total_soma)                       # para somar mais de 2 numeros


numeros = 1,2,3,4,5,6,7,78,10
outra_soma = soma(*numeros) # tem que haver o asterisco no começo ao enviar
print(outra_soma)           # uma tupla para dentro de uma função, pq assim
                            # se envia item por item desempacotados
                            # caso envie sem o asterisco, será enviado tudo junto
                            # fazendo parte do mesmo pacote

print(numeros) # perceba a diferança desses dois prints
print(*numeros) #o primeiro é tupla, o segundo são itens soltos printados em sequencia

