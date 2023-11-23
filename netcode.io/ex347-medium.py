""" 
    Given an integer array nums and an integer k, return the k most 
    frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""
"""
    Primeiro, é necessário separar quantos 'nums' se repetem.
    - Um dicionário com chave = numero, valor = quantidade

    Segundo, veja os que mais se repete e retorne os 'k' elementos.
    - A função sort() pode ser utilizada para ordenar as chaves por
    ordem crescente/decrescente.

    Terceiro, só quero saber dos 'k' elementos que mais se repetem.
"""
class Solução:
    """Classe responsável por solucionar o problema."""

    def mais_se_repete(self, valores, indice):
        """
            Recebe uma lista de números e um índice, e retorna 
            os 'k' elementos que mais se repetiram.
        """

        quantos_numeros = {}
        for valor in valores:
            if valor in quantos_numeros:
                quantos_numeros[valor] += 1
            else:
                quantos_numeros[valor] = 1
        
        
            
        return quantos_numeros
    

numeros = [1, 2, 3, 4, 1, 2, 1, 1, 2]
k = 2


run = Solução().mais_se_repete(numeros, k)
print(run)