# Generator expression, Iterables e Iterators em Python
# Todo generator é um Iterator, mas nem todo Iterator é um Generator

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() #tem __iter__ e __next__
iterator = iter(iterable) # O mesmo comando de cima, só que mais facil de ler

# iteraveis tem a responsabilidade de deter os valores
# a unica responsabilidade do iterador é te entregar um valor por vez, ele só sabe
# qual o próximo valor, ele não sabe qual é o primeiro, o anterior, o ultimo valor.


# Os comandos abaixo o iterator não sabe trabalhar, acessar indice, ou usar o len
# print(iterator[1])
# print(len(iterator))

# Ele só sabe usar o next
print(next(iterator))