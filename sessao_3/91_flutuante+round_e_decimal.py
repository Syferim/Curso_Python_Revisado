import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3) # retorna a soma errada pela imprecisão do de como o ponto flutuante
                # é salvo na memória

print(f'{numero_3:.2f}') # retorna corretamente, mas somente em formato string
print(round(numero_3, 2)) #retorna corretamente como numero

numero_1 = decimal.Decimal('0.1') # usando decimal.Decimal retorna o numero tambem
numero_2 = decimal.Decimal('0.7') # porém é mais complexo que usar round
numero_3 = numero_1 + numero_2
print(numero_3)