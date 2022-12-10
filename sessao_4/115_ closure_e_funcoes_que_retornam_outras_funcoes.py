"""
Closure e funções que retornam  outras funções
"""

def criar_saudacao( saudacao): # este parametro foi guardado
    def saudar(nome): # este só receberá la em baixo no print
        return f'{saudacao}, {nome}!' # aqui ele une o guardado e o recebido depois
    return saudar   # quando vc retorna o saudar sem os parenteses 'saudar()'
                    # vc não finalizou a função, então vc não retorna um resultado
                    # mas sim, retorna a função inteira com o resultado engatilhado
                    # nos parametros.

# em s1 sauvou a função inteira na memória
#em s2 criou uma outra funcao iggual em outro canto da memoria
# ou seja, são duas copias separadas da mesma funcao
# a edição de uma não muda a outra.
fala_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')
print(fala_bom_dia('Luiz')) # isto é closure, ou seja, ele precisa fechar a função
print(falar_boa_noite('Maria')) # a funcao estava engatilhada, mas não retornada o resultado
# veioa funcao engatilhada com o resultado não retornado, ao puxar
# falar_bom_dia ou falar_boa_noite com ()
# a funcao finalmente executa e retorna o resultado.

for nome in ['Maria', 'Joana', 'Luiz']:
    print(fala_bom_dia(nome))
    print(falar_boa_noite(nome))