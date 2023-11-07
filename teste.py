

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

def anagrama(palavra1, palavra2):    

    
    for letra in palavra2:
        if not (letra in palavra1):
            return False
    return True

print(anagrama("amor", "roma"))
print(anagrama("girafa", "grafia"))
print(anagrama("argila", "alegria"))
