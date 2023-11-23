

""""
Anagrama

Uma palavra é um anagrama quando ela consegue ser construída com as
mesmas letras de uma outra palavra, sem adicionar novas letras

amor - roma
girafa - grafia
esticam - camiseta
argila - alegria

"""

"""Teste Mercos - Anagrama"""


"""Saber se com as letras da palavra 1 eu consigo escrever a palavra 2, sem adicionar novas letras."""
"""SABER SE A PALAVRA 2 CONTEM AS LETRAS DA PALAVRA 1, SE SIM, É ANAGRAMA. """

def letras_na_palavra(palavra):

    letras = {}
    for letra in palavra:
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1
    print(letras)
    return letras


if letras_na_palavra('argila') == letras_na_palavra('alegria'):
    print('É anagrama')
else:
    print('Não é anagrama')