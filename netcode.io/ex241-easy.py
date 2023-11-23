

def all_letters(letters):
    """Recebe uma palavra e retorna um dicionário contendo como chave = letra, valor = qtd_letras."""
    
    letters_account = {}    # Dicionário para armazenar, como chave = letter, valor = letter accounts.

    for letter in letters:
        # Se a chave = letter estiver presente no dicionário letters_account.
        if letter in letters_account:
            # Some 1 a chave.
            letters_account[letter] += 1
        else:
            # Caso aquela chave não esteja contida ainda no dicionário letters_account, grave ele.
            letters_account[letter] = 1

    # Retorne o dicionário com a contagem de todas as letras da palavra.
    return letters_account


def isAnagram(s, t):
    """Testa se """
    letters_s = all_letters(s)
    letters_t = all_letters(t)

    if letters_s == letters_t:
        return True
    else:
        return False


print(isAnagram('roma', 'amor'))
