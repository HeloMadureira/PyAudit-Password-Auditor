import re

def identificar_tipo(hash_string):
    # Remove espaços em branco antes e depois
    hash_string = hash_string.strip()
    tamanho = len(hash_string)

    # Verifica se tem caracteres inválidos (tem que ser só 0-9 e a-f)
    if not re.match(r'^[0-9a-fA-F]+$', hash_string):
        return "Formato Inválido"

    # A mágica: O tamanho diz qual é o algoritmo
    if tamanho == 32:
        return "MD5"
    elif tamanho == 40:
        return "SHA-1"
    elif tamanho == 64:
        return "SHA-256"
    elif tamanho == 128:
        return "SHA-512"
    else:
        return "Desconhecido"
