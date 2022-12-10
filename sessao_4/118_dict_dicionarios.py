# pessoa = dict(nome='Luizz Otávio', sobrenome = 'Miranda') # método menos usado

# método mais usado
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [  # uma lista com dois dicionários dentro
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}

print(pessoa, type(pessoa))
print()
print(pessoa['nome'])
print(pessoa['sobrenome'])
print()
for chave in pessoa:
    print(chave, pessoa[chave])