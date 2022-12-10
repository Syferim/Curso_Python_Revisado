palavra_secreta = 'perfume'
letras_acertadas = ''

contador = 0

while contador <=24:
    letra_digitada = input('diga uma letra: ')
    contador+=1

    if len(letra_digitada) > 1:
        print('digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada+='*'
    print(palavra_formada)

    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('você ganhou! parabéns!')
        print('a palavra era: ', palavra_secreta)
        contador=21
