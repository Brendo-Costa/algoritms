""" 
    4. Implemente um programa que recebe o consumo de água de uma
    residência (em metros cúbicos) e calcula o valor da conta. O preço do metro
    cúbico de água é dado pela tabela abaixo: 

    Consumo (m³)                Preço por m³
        té 20                     R$ 8,50
    Maior ou igual a 20           R$ 11,00                      
"""

#Valor do consumo em m³
consumo = float(input("Informe o valor do consumo em m³: "))

#Se o consumo estiver entre 0 <= consumo <= 20
if 0 <= consumo < 20:
    total = consumo * 8.50
    print(f"Valor da conta R${total}")
else:
    total = consumo * 11
    print(f"Valor da conta R${total}")