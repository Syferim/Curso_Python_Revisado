# import sys
import sys as s

# não coloque o nome de variaveis com o mesmo nome dos modulos
from sys import exit, platform
from sys import exit as ex, platform as pf


print(s.platform) # chamando a função platform do modulo import sys com apelido 's'
print(platform) # chamando a função platform do modulo from sys
print(pf) # chamando a função platform com o apelido 'pf'