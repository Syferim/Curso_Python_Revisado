# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product
def print_iter(iterator):
    print(*list(combinations(pessoas, 2)), sep='\n')
pessoas = [
    'João', 'Joana', 'Luiz', 'Leticia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliester']
]

# print_iter(combinations(pessoas, 2))

print_iter(product(camisetas))
