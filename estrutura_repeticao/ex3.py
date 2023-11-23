""" 3. Implemente um programa que recebe números reais positivos e calcula a
raíz quadrada dos números maiores que 15. O programa deve parar
quando for dado o número -4. """
import math
num = 0

while num != -4:
    num = int(input("Digite um número: "))
    if num > 15:
        raiz = math.sqrt(num)
        print(f'A raiz quadada de {num} é {raiz}.')
    elif num == -4:
        break
    else:
        print(f'O número {num} é menor que 15.')