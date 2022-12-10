def saudacao(msg, nome):
    return f'{msg}, {nome}!'


# perceba que não sabemos quantos parametros vamos receber na função 'executa'
# logo usamos *args para empacotar todos os parametros em um unico parametro
# do tipo tupla e depois na função 'return' usamos *args de novo para desempacotar
# tudo o que está dentro da tupla convertendo novamente em varios parametros
def executa(funcao, *args): # empacota tudo o que foi recebido
    return funcao(*args) # desempacota tudo

print(
    executa(saudacao,'Bom dia', 'Luiz')
)
print(
    executa(saudacao,'Boa noite', 'Maria')
)
