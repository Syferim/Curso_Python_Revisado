"""
o que está dentro de uma função não afeta os valores de fora,
o que está fora pode afetar o que está dentro da função,
mas se usar a função global dentro da função, agora sim o que está dentro
pode afetar o que está fora.

é uma má prática usar o global dentro das funções para alterar valores fora.
"""

x = 1


def escopo():
    global x # aqui torna toda alteração de x dentro da função afetando fora
    x = 10 # x se tornou 10 fora da função tambem

    def outra_funcao():
        x = 11 # aqui não tem global, ou seja, não afetou x fora
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

print(x) # x ainda tinha o valor incial de 1
escopo() # aqui mudou o valor de x por causa do global
print(x) #agora x de fora é 10