"""Criar funções para a introdução do TCC, capítulo 1."""
import matplotlib.pyplot as plt



def grafico_idioma_documento(idiomas, quantidades):
    """Função cria um gráfico de barras, expondo os idiomas e suas quantidades."""

    # Cria um gráfico de barras tendo os idiomas e as quantidades como entrada. Cada
    # barra tera cor azul, de 0.5 px de largura.
    bars = plt.bar(idiomas, quantidades, color='blue' ,width=0.5)

    # Adiciona as quantidades ao topo da barra.
    for i, valor in enumerate(quantidades):
        plt.text(i, valor+2, str(valor), ha='center', va='bottom')

    # Adiciona título e labels nos eixos X e Y.
    plt.title('Idioma dos Documentos')
    plt.xlabel('Idiomas')
    plt.ylabel('Quantidades')

    # Mostra o gráfico
    plt.show()



# Instância de idiomas
idiomas = [
    'inglês',
    'português',
    'alemão',
    'turco',
    'italiano',
    'polonês',    
]

# Instância de quantidades
quantidades = [161, 2, 2, 1, 1, 1]

# Chama a função
grafico_idioma_documento(idiomas, quantidades)