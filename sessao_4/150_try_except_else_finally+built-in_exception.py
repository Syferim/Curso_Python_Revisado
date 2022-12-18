# try, except, else e finally
# FINALLY SEMPRE SERÁ EXECUTADO
# possibilidades de código: try e except | try except e else | try except e finaly |
# try except else e finally | try e else | try e finally
# basicamente try + alguma coisa

try:
    print('ABRI')
    # 8/0
except ZeroDivisionError:
    print('DIVIDIU ZERO')
else: # se o código for executado com sucesso o else é executado
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')