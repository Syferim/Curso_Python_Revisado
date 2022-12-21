# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

#####################
# Versão manual
# Como retornar as duas listas com a quantidade de itens iguais ao máximo da lista menor
def zipper(l1, l2):
    intervalo = (min(len(l1), len(l2)))
    return [(l1[i], l2[i]) for i in range(intervalo)]


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(l1, l2))
#####################

print()
print()
print()

from itertools import zip_longest  # Necessário para zip_longest apenas

# Versão pronta do Python (zip)
# Guardando em uma variavel
item = (list(zip(l1, l2)))  # O zip não precisa do import acima
print(item)

# Gerando um iterator
print(list(zip(l1, l2)))  # Retorna as listas em relação a menor

print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))  # Retorna a listas em relação a maior
                                # fillvalue usado para os itens novos gerados não sejam
                                # None por padrão e sim o valor passado ao fillvalue
