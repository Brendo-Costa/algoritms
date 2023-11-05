""" 
    2. Implemente um programa que recebe três valores inteiros referentes a uma
    data e a imprime com o mês por extenso. Exemplo de entrada: “10 5 2013”.
    Exemplo de saída: “10 de Maio de 2013”. 
"""

#Receber 3 valores inteiros (dia, mes, ano)

dia = int(input("Informe o dia: "))
mes = int(input("Informe o mes: "))
ano = int(input("Informe o ano: "))

#Se o dia não estiver dentro desse intervalo 1-31, é um número inválido.
if not (0<= dia <= 31):
    print(f"Dia Inválido = = = {dia}.")
#Se o mês não estiver dentro desse intervalo 1-12, é um número inválido.
if not 0<= mes <= 12:
    print(f"Mẽs inválido = = = {mes}.")
#Se o ano não estiver dentro de instervalo, 0 até infinito, é um ano válido. 
if not ano > 0:
    print(f"Ano inválido = = = {ano}.")


#Se o dia estiver entre 0-31 e o mẽs entre 0-12, imprima (DIA do MES do ANO).
if (0<= dia <=31) and (0<= mes <=12):
    if mes == 1:
        print(f"{dia} de Janeiro de {ano}")
    elif mes == 2:
        print(f"{dia} de Fevereiro de {ano}")
    elif mes == 3:
        print(f"{dia} de Março de {ano}")
    elif mes == 4:
        print(f"{dia} de Abril de {ano}")
    elif mes == 5:
        print(f"{dia} de Maio de {ano}")
    elif mes == 6:
        print(f"{dia} de Junho de {ano}")
    elif mes == 7:
        print(f"{dia} de Julho de {ano}")
    elif mes == 8:
        print(f"{dia} de Agosto de {ano}")
    elif mes == 9:
        print(f"{dia} de Setembro de {ano}")
    elif mes == 10:
        print(f"{dia} de Outurbo de {ano}")
    elif mes == 11:
        print(f"{dia} de Novembro de {ano}")
    elif mes == 12:
        print(f"{dia} de Dezembro de {ano}")
