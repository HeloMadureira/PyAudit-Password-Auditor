import re
    

def identificar_tipo(hash: str) -> str:
    # Remove espaços em branco antes e depois
    hash: str    = hash.strip()
    tamanho: int = len(hash)

    # Verifica se tem caracteres inválidos (tem que ser só 0-9 e a-f)
    if not re.match(r'^[0-9a-fA-F]+$', hash):
        return "Formato Inválido"
    
    # A mágica: O tamanho diz qual é o algoritmo
    match tamanho:
        case 32:  return "MD5"
        case 40:  return "SHA-1"
        case 64:  return "SHA-256"
        case 128: return "SHA-512"
        case _:   return "Desconhecido"

