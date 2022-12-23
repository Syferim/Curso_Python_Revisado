"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.

Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

=================== resultado
lista_soma = [2, 4, 6, 8]
"""

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]


##########################

# A forma geral de qualquer linguagem
lista_soma = []
numero_indice = list(zip(lista_a, lista_b))

for i in range(len(numero_indice)):
    lista_soma.append(sum(numero_indice[i]))

print(lista_soma)

##########################

# Forma meio "Pythonica"
lista_soma = []
for i, _ in enumerate(numero_indice):
    lista_soma.append(sum(numero_indice[i]))

print(lista_soma)

##########################

# Forma mais "Pythonica"
lista_soma = []
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)



