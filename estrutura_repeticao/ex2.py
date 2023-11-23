""" 
    2. Escreva um programa que recebe 15 números e imprime seus quadrados.
"""

cont = 0
while cont < 15:
    num = int(input("Digite um número: "))
    print('O quadrado')
    quadrado = num*num
    print(quadrado)
    cont += 1


print(cont)