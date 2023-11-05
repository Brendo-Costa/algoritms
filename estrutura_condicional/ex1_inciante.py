""" 
    1. Implemente um programa que recebe um número real e calcula: o quadrado
    do número, caso ele seja um número negativo, ou sua raiz quadrada, caso
    contrário.
"""

import math




#Recebendo um valor de entrada (tipo -> real)
num = int(input("Digite o número real: "))
print(num)

#Se o número for negativo, calcule seu quadrado.
if num < 0:
    quadrado = num*num
    print(quadrado)
#Se não, tire sua raiz quadrada.
else:
    raiz = math.sqrt(num)
    print(raiz)
