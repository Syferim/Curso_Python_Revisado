# List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de iteráveis

# forma 0, printando uma lista facil
print('forma 0', list(range(10)))


# primeira forma, como criar uma lista
lista = list(range(10))
print('forma 1', lista)


# segunda forma, como criar uma lista
lista = []
for numero in range(10):
    lista.append(numero)

print('forma 2', lista)


# forma 3, como criar uma lista usando list comprehension
lista = [numero for numero in range(10)]
print('forma 3', lista)


# forma 4, como criar uma lista usando  list comprehension e adicionando uma operação junto
lista = [
    numero * 2
    for numero in range(10)
]
print('forma 4', lista)


# Mapeamento de dados em list comphrehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    # produto['preco']
    # {'nome': produto['nome'], 'preco': produto['preco']} # jeito manual
    {**produto, 'preco': produto['preco'] * 1.05}   # jeito pratico, desempacotando o dicionario
                                                    # mudando o preco do produto para + 5%

    if produto['preco'] > 20 else {**produto}       # condicionando o aumento somente se
                                                    # o preço for maior que 20 reais, caso não, não tem aumento

    for produto in produtos
]


# desempacotando a lista
print(*novos_produtos, sep='\n')