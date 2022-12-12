'''
.<numero de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
< - Centro
Sinal - + ou -
Ex:.: 0>-100,.1f
Conversion flags - !r !s !a
'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.4873648123746:.1f}')
print(f'{1000.4873648123746:,.1f}')
print(f'{1000.4873648123746:0>+10,.1f}') # errado
print(f'{1000.4873648123746:0=+10,.1f}') # certo
