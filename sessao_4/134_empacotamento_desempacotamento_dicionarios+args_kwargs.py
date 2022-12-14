"""
*args - valores não nomeados, exemplos nesta atividade: 1, 2
**kwargs - valores nomeados, exemplos nesta atividade: nome='Joana', qlq=123
"""


a, b = 1, 2
a, b = b, a
# print (a,b)

pessoa = {
    'nome' : 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}
# print(pessoa, dados_pessoa)

pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa)



# a, b = pessoa.items()
# (a1, a2), (b1, b2) = pessoa.items
# print(a, b)
# print(a1, a2)
# print(b1, b2)


# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
def mostro_arumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args) # exibe 1 e 2 (args)
    for chave, valor in kwargs.items():
        print(chave, valor) # exibe a chave e o valor dos nomeados (kwargs)



# mostro_arumentos_nomeados(1, 2, nome='Joana', qlq=123)  # 1 e 2 são não nomeados (args)
                                                        # nome e qlq são nomeados (kwargs)

mostro_arumentos_nomeados(1, 2, **pessoas_completa)
# pessoas_completa juntou os dois dicionarios e a chamada de função acima tem 1 e 2 como
# valores não nomeados (*args) e pessoas_completa como valores nomeados (**kwargs)


configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_arumentos_nomeados(**configuracoes)