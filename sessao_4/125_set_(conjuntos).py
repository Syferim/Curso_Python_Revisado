"""
sets - conjuntos em python (tipo set)
conjuntos são ensinados na matematica
representados graficamente pelo diagrama venn
sets em python são mutaveis, porém aceitam apenas
tipos imutaveis como valor interno
"""

#criando um set
#set(iteravel) ou {1, 2, 3,}

s1 = set() #set vazio
s1 = set('Luiz')
# s1 = {'luiz', 1, 2, 3} #set com dados
print(type(s1))
print(s1)


# sets são eficientes para remover valores duplicados de iteraveis
# - seus valores serão unicos;
# - não aceitam valores mutaveis;
# - não tem indexes;
# - não garantem ordem;
# - são iteraveis ( for, in, not in)
l1 = [1,2,3,3,3,3,3,1]
s1 = set(l1) # transformando em set e eliminando os duplicados
l2 = list(s1) # convertendo em lista novamente com os duplicados limpados
print(s1)
print(l2)

s1 = {1, 2, 3}
print(3 in s1) # comando para localizar o numero 3 dentro do set (boleano=True pq há o 3)


s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Luiz')
print(s1)


# operadores úteis:
# união | união (union) - une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2
print(s3)

s3 = s1 & s2
print(s3)

s3 = s1 - s2
print(s3)

s3 = s1 ^ s2
print(s3)
