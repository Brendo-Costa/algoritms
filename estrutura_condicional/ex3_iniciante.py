"""
    3. Implemente um programa que recebe um número inteiro e determina se ele
    é divisível por 6. 
"""

#Recebendo o número inteiro
num = int(input("Informe um número inteiro: "))

#Divisível por 6
divisao = num % 6
if not (divisao == 0):
    print(f"O número 20{num} não é divisível por 6. O resto da divisão deveria dar 0 e deu {divisao}.")
else:
    print(f"{num} é divisível por 6. Dado que o resto da díviisão deu {divisao}")