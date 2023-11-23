""" 
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

# Selecionar cada elemento do array de strings, um de cada vez.
# Percorrer o array
# Perguntar a cada elemento do array, se ela é um anagrama.
# Se for, a palavra que for anagrama do elemento será adicionada a uma lista.
# Se não for anagrama, apenas passe pra o próximo elemento e pergunte.

# Ao final de testar um elemento com todos os outros, teste o segundo elemento
#com todos os outros.
# 

# _0 _1 _2 _3 _4 
# _0 _1 _2 _3 _4 

class Resolução:
    def letras(self, palavra):
        """Recebe uma palavra e retorna um dicinário, onde a chave é a 'letra' e a quantidade de letras na palavra é o 'valor'."""

        letras = {}     #Crio o dicionário para armazenar as letras.
        for letra in palavra:   # Percorro cada letra da palavra.
            if letra in letras: # Se a letra já estiver armazenada no dicionário, eu adiciono +1 a contagem.
                letras[letra] += 1
            else:       #   Se não, eu armazeno-a.
                letras[letra] = 1
        return letras


    def grupo_de_anagramas(self, lista_de_palavras):
        """Recebe uma lista de palavras, e retorna uma lista com anagramas agrupados em listas."""
        
        todos_agrupamentos = []
        for palavra_i in lista_de_palavras:
            letras_i = self.letras(palavra_i)
            
            agrupar = []
            for palavra_j in lista_de_palavras:
                letras_j = self.letras(palavra_j)
                
                if letras_i == letras_j:
                    agrupar.append(palavra_j)
            
            if not agrupar in todos_agrupamentos: 
                todos_agrupamentos.append(agrupar)

        return todos_agrupamentos
    
        
palavras = ['amor', 'roma', 'omar', 'ramo', 'garfo', 'ofrag', 'argor']
run = Resolução().grupo_de_anagramas(palavras)
print(run)