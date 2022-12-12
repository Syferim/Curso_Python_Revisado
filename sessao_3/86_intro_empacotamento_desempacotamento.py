'''
desempacotando uma lista
o _ (underline) serve como nome de variavel para lixo, que não quer usar
os dois primeiros _ foi usado para ignorar os dois primeiros nomes
depois foi capiturado o terceiro nome em "nome3"
então foi criado *_ para colocar o resto (o lixo), perceba que não precisa nem ter
mais itens para por no *_, ele aceita ficar vazio
'''

_, _, nome3, *_ = ['Maria', 'Helena', 'Luiz']
print( nome3, _)