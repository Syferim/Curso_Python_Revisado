# Generator expression, Iterables e Iterators em Python
# Dica: todo generator é um iterator, mas um iterator não é um generator
import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() #tem __iter__ e __next__
iterator = iter(iterable) # O mesmo comando de cima, só que mais facil de ler
lista = [n for n in range(10000)] # improdutivo, armazena muitos dados na memória
generator = (n for n in range(1000))    # gera um numero por vez e não armazena na memória
                                        # os numeros anteriores e futuros
print(generator)

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)

# iteraveis tem a responsabilidade de deter os valores
# a unica responsabilidade do iterador é te entregar um valor por vez, ele só sabe
# qual o próximo valor, ele não sabe qual é o primeiro, o anterior, o ultimo valor.


# Os comandos abaixo o iterator não sabe trabalhar, acessar indice, ou usar o len
# print(iterator[1])
# print(len(iterator))

# Ele só sabe usar o next
print(next(iterator))