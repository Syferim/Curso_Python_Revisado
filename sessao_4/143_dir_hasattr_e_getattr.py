string = 'luiz'
metodo = 'upper'

print(string)


# checa se existe o método upper na variavel que tem um valor str
if hasattr(string, metodo):
    print('Existe upper')
    # print(string.upper())
    print(getattr(string, metodo)()) #obtem o metodo escrito na variavel "metodo"
    # print(string)
else:
    print('Não existe o método', metodo)

"""
Dica: hasattr checa se existe um metodo, então, com getattr se obtem este metodo
neste caso, checou se em string havia o metodo upper escrito na variavel metodo
então descobriu-se que sim "True", logo o getattr obteve o metodo (converteu o texto
dentro da variavel "metodo" em um metodo real e executou o upper e escreveu o nome em
maiúsculo
"""