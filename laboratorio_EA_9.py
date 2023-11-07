"""Script criado para auxiliar a resolução da lista 9, da disciplina de Lab EA."""
import matplotlib.pyplot as plt


"""
    Entrada: frequência de ressonância sem amostra, frequeência de ressonância com amostra.
    Saída: DeltaFr.
"""
def deltafreq(freqr_sa, freqr_ca):
    deltafr = freqr_sa - freqr_ca
    if deltafr < 0:
        deltafr = deltafr * (-1)
    print(deltafr)
    return deltafr



"""
    Entrada: dieletrico sem amostra, dieletrico com amostra.
    Saída: DeltaDiel.
"""
def deltadiel(dielr_sa, dielr_ca):
    deltadiel = dielr_sa - dielr_ca
    if deltadiel < 0:
        deltadiel = deltadiel * (-1)
    print(deltadiel)
    return deltadiel



def sensibilidade(freqr_sa, freqrs_ca, deltar_sa, deltasr_ca):
    deltafr_list = []
    for freq in freqrs_ca:
        deltafr = deltafreq(freqr_sa, freq)
        print(f"O valor de DELTA F: {deltafr} para frequencia ressonancia no ar {freqr_sa} e frequencia de ressonancia da amostra {freq}")
        deltafr_list.append(deltafr)
    print(deltafr_list)

    deltadielr_list = []
    for dielr in deltasr_ca:
        deltadiels = deltadiel(deltar_sa, dielr)
        print(f"O valor de DELTA Er: {deltadiels} para Er no ar {deltar_sa} e Er da amostra {dielr}")
        deltadielr_list.append(deltadiels)

    print(deltadielr_list)
    sensibilidade_duroid = deltafr_list[0] / deltadielr_list[0]
    print(f'Sensibilidade do Duroid - {sensibilidade_duroid}')

    sensibilidade_fr4 = deltafr_list[1] / deltadielr_list[1]
    print(f'Sensibilidade do FR4 - {sensibilidade_fr4}')

    sensibilidade_3006 = deltafr_list[2] / deltadielr_list[2]
    print(f'Sensibilidade do 3006 - {sensibilidade_3006}')

    sensibilidade_3010 = deltafr_list[3] / deltadielr_list[3]
    print(f'Sensibilidade do 3010 - {sensibilidade_3010}')

    soma = sensibilidade_duroid + sensibilidade_fr4 + sensibilidade_3006 + sensibilidade_3010
    media = soma / 4
    print(soma, media)
    return deltadielr_list, deltafr_list


"""
    Calcula o erro percentual de uma amostra de elementos dielétricos.
    Entrada: elemento "base", elemento "o".
    Saída: erro percentual 
"""
def erropercentual(er_base, er_o):
    
    deltaer = er_base - er_o

    if deltaer < 0:
        deltaer = deltaer * (-1)

    print(deltaer)
    
    if er_base < 0:
        er_base = er_base * (-1)
    print(er_base)
    var = deltaer / er_base
    print(var)
    erro = ( var ) * 100
    return erro




"""
    Dados referente a antena A
    Lista de dados contendo frequeência de ressonância com amostra,
    Lista de dados contendo dieletrico com amostra.
    Todos os valores em GHz.
"""
freqr_sa = 1.5315       #Valor em GHz
dielr_sa = 0.7545
freqr_ca_antenaA = [1.4692, 1.4068, 1.3444, 1.2651]       #Valores das frequẽncias de ressonância para cada dielétrico testado



dielr_ca_base = [2.2, 4.4, 6.15, 10.2]
dielr_antenaA = [2.6213, 4.8291, 7.3753, 11.0992]

"""Sensibilidade"""
run_sensibilidade = sensibilidade(freqr_sa, freqr_ca_antenaA, dielr_sa, dielr_antenaA)


"""Calcule o erro percentual para cada amostra de Er - Duroid"""
#RT/Duroid( 2.2 )
epsila_duroid_base = 2.2
epsila_duroid_medido = 2.6213
erro_duroid = erropercentual(epsila_duroid_base, epsila_duroid_medido)
print(f"erro percentual entre Er_base_duroid - {epsila_duroid_base}, Er_medido_duroid - {epsila_duroid_medido} \
      erro percentual {erro_duroid} %")



"""Calcule o erro percentual para cada amostra de Er - FR4"""
#FR4( 4.4 )
epsila_fr4_base = 4.4
epsila_fr4_medido = 4.8291
erro_fr4 = erropercentual(epsila_fr4_base, epsila_fr4_medido)
print(f"erro percentual entre Er_base_FR4 - {epsila_fr4_base}, Er_medido_fr4 - {epsila_fr4_medido} \
    erro percentual {erro_fr4} %")



"""Calcule o erro percentual para cada amostra de Er - RO3006"""
#RO3006( 6.15 )
epsila_3006_base = 6.15
epsila_3006_medido = 7.3753
erro_3006 = erropercentual(epsila_3006_base, epsila_3006_medido)
print(f"erro percentual entre Er_base_3006 - {epsila_3006_base}, Er_medido_fr4 - {epsila_3006_medido} \
    erro percentual {erro_3006} %")



"""Calcule o erro percentual para cada amostra de Er - RO3010"""
#RO3010( 10.2 )
epsila_3010_base = 10.2
epsila_3010_medido = 11.0992
erro_3010 = erropercentual(epsila_3010_base, epsila_3010_medido)
print(f"erro percentual entre Er_base_3010 - {epsila_3010_base}, Er_medido_fr4 - {epsila_3010_medido} \
    erro percentual {erro_3010} %")




freqr_ca_antenaA = [1.5315, 1.4692, 1.4068, 1.3444, 1.2651]
dielr_antenaA = [0.7545, 2.6213, 4.8291, 7.3753, 11.0992]
cores = ['r', 'g', 'b', 'c', 'm']
nomes = ['Vázio', 'Duroid', 'FR4', 'RO3006', 'R03010']



def plotar_grafico_com_cores_e_nomes(vetor1, vetor2, cores, nomes):
    if len(vetor1) != len(vetor2) or len(vetor1) != len(cores) or len(vetor1) != len(nomes):
        raise ValueError("Os vetores, cores e nomes devem ter o mesmo comprimento.")

    plt.figure(figsize=(10, 6))  # Define o tamanho da figura

    for i in range(len(vetor1)):
        plt.scatter(vetor1[i], vetor2[i], color=cores[i], label=nomes[i])
    
    plt.xlabel("Frequência de Ressonância - GHz")
    plt.ylabel("Permissividade Dieletrica")
    plt.title("Gráfico de Dispersão com Cores e Nomes")
    
    # Adiciona uma legenda com os nomes
    plt.legend()
    
    plt.grid(True)
    plt.show()

run_grafico = plotar_grafico_com_cores_e_nomes(freqr_ca_antenaA, dielr_antenaA, cores, nomes)