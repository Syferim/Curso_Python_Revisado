#Cuidado com valores imutaveis
lista_a = ['Luiz', "maria"]
lista_b = lista_a #isso aqui não gerou uma copia separada, está ligada a primeira lista

lista_a[0] = 'Qualquer outra coisa' #o que mudou na lista_a, também mudou na lista_b
print(lista_b)
#==========================================
lista_a = ['Luiz', "maria"]
lista_b = lista_a.copy() #deste jeito realmente cria uma cópia separada

lista_a[0] = 'Qualquer outra coisa' #agora aqui só afeta a lista_a
print(lista_b)

