p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
#print(p1['nome']) # neste método falha se nome estiver comentado
# print(p1.get('nome')) # neste método não falha com nome comentado e retorna None

# nome = p1.pop('nome') # remove a chave nome, porem retorna o valor para a variavel ao mesmo tempo
# print(nome)
# print(p1)

# ultima_chave = p1.popitem() # renome a ultima chave do dicionario e retorna seu valor para a variavel
# print(ultima_chave)
# print(p1)


# p1.update({
#     'nome': 'novo valor', # atualiza o valor de nome
#     'idade': 30, # adiciona uma nova chave e valor
# })
# print(p1)

# p1.update(nome='novo valor', idade=30)
# print(p1)

tupla = (('nome', 'novo valor'), ('idade', 30))
p1.update(tupla)
print(p1)
