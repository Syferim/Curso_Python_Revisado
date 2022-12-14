# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
lista = [4,32,1,34,5,6,6,21]
lista.sort(reverse = True)
#sorted(lista)

print(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# ordenar por nome
def ordena(item):
    print('PRINT', item)
    return item['nome']


lista.sort(key=ordena)
print(lista)
# termina aqui a ordenação por nome

print()

# usando lambda para ordenação da biblioteca por nome
lista.sort(key=lambda item: item['nome'])
print(lista)
# fim  da ordenação

# outro jeito de ordenar
def exibir(lista): #print de cada linha da biblioteca
    for item in lista: # tanto em ordem por nome quanto por sobrenome (l1 e l2)
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome']) # ordena por nome
l2 = sorted(lista, key=lambda item: item['sobrenome']) # ordena por sobrenome
exibir(l1) # ativa a função def exibir
exibir(l2) # ativaa função deve exibir


#fim do outro jeito