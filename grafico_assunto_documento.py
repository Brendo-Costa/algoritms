"""Criar gráfico para introdução do TCC"""
import matplotlib.pyplot as plt




def grafico_assunto_documento(assuntos, quantidades):
    """Cria um gráfico contendo os assuntos no eixo X e as quantidades no Y."""

    # Cria um gráfico de barras, de cor azum com a largura específica.
    bars = plt.bar(assuntos, quantidades, color='blue', width=0.5)

    # Adicionando os valores no topo de cada barra
    for i, valor in enumerate(quantidades):
        plt.text(i, valor + 1, str(valor), ha='center', va='bottom')

    # Cria o título e as respectivas notas para os eixos.
    plt.title('Assuntos dos Documentos')
    plt.xlabel('Assuntos')
    plt.ylabel('Quantidades')

    # Assuntos que irão na legenda
    assuntos_legenda = [
        'CET - ciências e tecnologia',
        'CBM - ciências biomedicas',
        'CEL - campo eletromagnético',
        'HMN - humanos',
        'TEC - tecnologia',
        'AMB.C - ambiente científico',
        'RNI - radiação não-ionizante',
        'TEL - telefone celular',
        'ORD - ondas de rádio',
        'EXP - exposição'
    ]

    # Cria uma legenda
    plt.legend(bars, assuntos_legenda, title='Assuntos', loc='upper right')


    plt.show()


#Criando vetor com assuntos
assuntos = ['CET', 'CBM', 'CEL', 'HMN', 'TEC', 'AMB.C', 'RNI', 'TEL', 'ORD', 'EXP']
quantidades = [107, 86, 63, 53, 51, 48, 38, 33, 30, 23]

grafico_assunto_documento(assuntos, quantidades)