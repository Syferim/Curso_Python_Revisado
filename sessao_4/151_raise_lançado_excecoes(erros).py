# raise - lançando exceções (erros)

# def divide(n, d):
#     try:
#         return n / d
#     except ZeroDivisionError:
#         print('____')
#         raise
#
# print(divide(8, 0))


def divide(n, d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')

print(divide(8, 0))