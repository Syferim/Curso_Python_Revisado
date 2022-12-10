# exercicios
# crie funções que duplicam, triplicam e quadriplicam
# o numero recebido como parametro


def criar_multiplicador(multiplicador): # multiplicador definido como 2, 3, 4
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar # engatilha a resposta do numero du./tri./quadruplicado

duplicar = criar_multiplicador(2)       # cria um copia da função engatilhada para duplicar
triplicar = criar_multiplicador(3)      # aqui uma segunda copia com triplicar
quadruplicar = criar_multiplicador(4)   # terceira copia da função com quadruplicar
print(duplicar(2)) # chama a função e a função engatilhada executa
print(triplicar(2)) # executa a segunda copia
print(quadruplicar(2)) # executa a terceira copia
