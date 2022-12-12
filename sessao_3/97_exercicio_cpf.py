import random
import re #regular expression
import sys

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))
    print(nove_digitos)

# cpf_enviado_usuario = '746.824.890-70' \
#     .replace('.','') \
#     .replace(' ','') \
#     .replace('-','')
# tudo isto, faz o mesmo que o de baixo, mas usa o re (regular expression)

cpf_enviado_usuario = re.sub(   # substitui tudo
    r'[^0-9]',                  # o que não for de 0 a 9
    '',                         # por nada
    '746.824.890-70'            # destes valores
)

entrada_e_sequencial = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)
if entrada_e_sequencial:
    print('Você enviou dados sequênciais.')
    sys.exit() #se for numeros repetidos, ele sai do código


nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += (int(digito) * contador_regressivo_1)
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += (int(digito) * contador_regressivo_2)
    contador_regressivo_2-=1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0


cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')