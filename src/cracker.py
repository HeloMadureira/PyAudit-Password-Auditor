import hashlib


ALGORITMOS_SUPORTADOS = {
        'MD5':     hashlib.md5,
        'SHA-1':   hashlib.sha1,
        'SHA-256': hashlib.sha256,
        'SHA-512': hashlib.sha512
}


def quebrar_senha(hash: str, tipo: str, wordlist_path: str) -> tuple[bool, str]:   
    # Se o detector não souber o que é, a gente pula
    if tipo not in ALGORITMOS_SUPORTADOS:
        return False, 'Algoritimo não suportado'

    try:
        # Abre a wordlist modo leitura ('r'), ignorando erros de acentuação
        with open(wordlist_path, 'r', errors='ignore') as f:
            for senha in f:
                senha = senha.strip() # Remove o "Enter" do final
               
                # A Mágica: Transforma a senha da lista em hash
                hash_calculada = ALGORITMOS_SUPORTADOS[tipo](senha.encode('utf-8')).hexdigest()
               
                # Compara
                if hash_calculada == hash:
                    return True, senha # ACHOU! Retorna a senha limpa
                   
    except FileNotFoundError:
        return False, 'Arquivo não encontrado'
   
    return False, 'Não encontado na lista' # Se rodou a lista toda e não achou
