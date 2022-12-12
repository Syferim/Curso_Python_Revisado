'''
enumerate - enumera iteraveis (indices)
'''

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# lista_enumerada = enumerate(lista) #maneira errada, não crie variavel com inumerate


for item in enumerate(lista): # use o inumerate direto no for
    print(item)

for item in enumerate(lista): # assim pode reutilizar o mesmo inumerate
    print(item)

lista_enumerada = list(enumerate(lista)) # criada uma lista com varias tuplas com os dados do inumerate
print(lista_enumerada)

# jeito 1, menos usual
for item in enumerate(lista): #o enumerate mostra o valor e o indice
    a, b = item # aqui salvei o indice no a e o valor no b, desempacotando de item
    print(a, b) # printei indice(a) e valor(b) soltos
    print(item) # este printe faz o mesmo, mas em formato tupla padrão

#jeito 2, mais usual
for indice, nome in enumerate(lista): #o mesmo do de cima, só que mais facil
    print(indice, nome)
    


