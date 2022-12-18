# def generator(n=0, maximum=10):
#     yield 1 # Pausar
#     print('Continuando...')
#     yield 2 # Pausar
#     print('Mais uma...')
#     yield 3 # Pausar
#     print('Vou terminar...')
#
#
# gen = generator(n=0)
# for n in gen:
#     print(n)



def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n >= maximum:
            return



gen = generator()
for n in gen:
    print(n)

print()
gen = generator(n=5, maximum=8)
for n in gen:
    print(n)

print()
gen = generator(maximum=8)
for n in gen:
    print(n)



