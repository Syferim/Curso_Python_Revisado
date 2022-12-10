'''
Métodos úteis dos dicionários em Python
Len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave específicada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro

aula 2
shallow copy - cópia raza
deep copy - cópia profunda
'''
 import copy

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda 3',
    'idade': 900,
}

pessoa.setdefault('idade', None)
print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))


for chave in pessoa.keys():  # o comando "for chave in pessoa:" tambem funciona
    print(chave)  # para keys não precisa escrever o ".keys()"

for chave in pessoa.values():
    print(chave)

for chave, valor in pessoa.items():
    print(chave, valor)

d1 = {
    'c1': 1,
    'c2': 1,
    'l1': [0, 1, 2],
}
d2 = copy.cd1

d2['c1'] = 1000
d2['11'][1] = 9999

print(d1)
print(21)
