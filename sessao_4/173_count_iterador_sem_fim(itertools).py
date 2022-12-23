# count é um iterador sem fim (itertools)
from itertools import count

# START e STEP não é obrigatório, é só para nomear.
c1 = count(start=8, step=8) # Começando do 8 e pulando de 8 em 8, count não tem fim.
r1 = range(16, 100, 8) # Começando do 16 e indo até o 100, pulando de 8 em 8.

print('c1', hasattr(c1, '__iter__')) # count é um iteravel
print('c1', hasattr(c1, '__next__')) # e também é um iterator

print('r1', hasattr(r1, '__iter__')) # range é um iteravel
print('r1', hasattr(r1, '__next__')) # mas não é um iterator

print('count')
for i in c1:
    if i >= 100:
        break
    print(i)

print()

print('range')
for i in r1:
    print(i)