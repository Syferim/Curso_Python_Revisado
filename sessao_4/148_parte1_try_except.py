# Try, except, else e finally
string = 'Luiz' #str
print(isinstance(string, str)) # questionando se a instancia Luiz é um str


try:
    a = 18
    b = 0 # se estiver comentado dará NameError
    print('linha1'[1000]) # se não estiver comentado dará TypeError
    c = a / b # dará ZeroDivisionError por tentar divisão por zero
    print('linha2')
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError') # os tipos de erros são classes
    print('MSG', error)
    print('MSG', error.__class__.__name__)
except Exception:
    print('erro desconhecido')
    # Resto dos erros não conhecidos

print('CONTINUAR')