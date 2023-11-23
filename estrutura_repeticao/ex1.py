""" 
1. Implemente um programa que recebe um número qualquer repetidas vezes
e só pára quando o número digitado é 22.
"""

#Condição de Início/Continuação
while True:
    #Execução
    num = int(input("Digite um número: "))
    #Condição de Parada
    if num == 22:
        break
    if num == 2:
        print('Você encerrou o código.')
        break