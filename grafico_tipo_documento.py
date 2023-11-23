"""Criar gráficos para a introdução do TCC."""
import matplotlib.pyplot as plt



def grafico_tipo_documento(tipos, quantidades):
    """
        Recebe um vetor contendo os tipos de documentos encontrados
        na pesquisa e suas respectivas quantidades e cria um gráfico
        de barras.
    """

    #Cria um gráfico de barras, usando as entradas da função.
    plt.bar(tipos, quantidades, color='blue', width=0.5)

    # Adicionando os valores no topo de cada barra
    for i, valor in enumerate(quantidades):
        plt.text(i, valor + 1, str(valor), ha='center', va='bottom')

    #Adicionar título e rotulo nos eixos (x e y)
    plt.title('Tipos de Documento')
    plt.xlabel('Tipo')
    plt.ylabel('Quantidade')

    #Mostrar o gráfico
    plt.show()
    #plt.savefig('tipos_documentos.png')

#Criando o vetor com os tipos e as quantidades
tipos = ['artigos','atas', 'capítulo de livros', 'livros', 'artigos newsletter']
quantidades = [144, 13, 4, 1, 2]

#Chamando a função e passando os parâmetros
grafico_tipo_documento(tipos, quantidades)