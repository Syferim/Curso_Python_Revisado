# isinstance - para saber se objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Luiz'},
]

for item in lista: # se for tipo set
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str): # se for tipo str
        print('STR')
        print(item.upper(), isinstance(item, set))

    elif isinstance(item, (int, float)): # se for tipo int ou float
        print('NUM')
        print(item, item * 2)

    else:
        print('OUTRO')
        print(item)
