string = ['ABCDE', 10, True, 1.2]  # 5 caracteres *len)

string[-3] = 'maria'
print(string)

print(string[2], type(string[2]))

lista = [10, 20, 30, 40]
lista.append('luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(0, 5)
print(lista)
print(len(lista))

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b # cria uma lista c com os dados da lista a e b
lista_a.extend(lista_b) #atualiza diretamente a lista a, contendo b também
print(lista_c)

lista_a = [1,2,3,4,5,6,7,8,9,10]
print(lista_a)


# gerador de dados D10 em ordem decrescente
# import random
#
# dados = int(input('informe o numero de dados: '))
# resultados = []
#
# for i in range(dados):
#     x = random.randint(1, 10)
#     resultados.append(x)
#
# resultados.sort()
# resultados.reverse()
# print(resultados)
