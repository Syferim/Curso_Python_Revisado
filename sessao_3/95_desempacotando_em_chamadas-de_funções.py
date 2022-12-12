string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# p, b, *_, ap, u = lista
# print(p,u)

# for nome in lista:
#     print(nome, end=' ')

print(*lista) # passa cada item da lista no print separados por espaço
print(*string) # separa cada letra da string por espaço
print(*tupla) # printa cada item da tupla separado por espaço
print()

print(*string, sep=('-')) # o mesm oque o de cima, porem separa cada letra por traço
print()

# sep: separador de cada pedaço do item
# end: separador de cada final de item

print(*lista, sep='\n')