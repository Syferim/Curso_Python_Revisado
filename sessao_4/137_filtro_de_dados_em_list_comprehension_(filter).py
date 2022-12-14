# A atividade anterior (135) explicou melhor cada etapa deste código

import pprint

# Função criada para não ficar criando ela sempre que quiser usar pprint com estes parametros
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

# O if antes do for sempre tem else, o if depois do for só tem if
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# desempacotando a lista
# print(*novos_produtos, sep='\n')

# pacote pprint importado, um print mais bonito
# não dá de mandar vários parametros em pprint igual o print acima
pprint.pprint(novos_produtos)
pprint.pprint(novos_produtos, sort_dicts=False, width=40)   # sempre que quiser definir
                        # estes parametros, teria que escrever eles manualmente no pprint
                        # Em vez disso, pode chamar a função criada la em cima do pprint

p(novos_produtos) #chamando a função pprint la de cima



print()
# filtro, inclue o numero na variavel lista se o numero for menor que 5
lista = [n for n in range(10) if n < 5]
print(lista)

print()
# Lembre-se, o que vem a esquerda do for é mapeamento, o que vem a direita é filtro

# Dica 1: Mapeamento quer dizer que to pegando um dado e talvez transformando e jogando em
# outra lista e essas duas listas tem o mesmo tamanho

# Dica 2: Filtro quer dizer que eu posso incluir ou não incluir aquele elemento na minha
# lista e eu posso combinar as duas se eu quiser
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco']* 1.05) > 10
]
p(novos_produtos)
