import hashlib

def quebrar_senha(target_hash, algoritmo, wordlist_path):
    """
    Tenta encontrar a senha correspondente à hash fornecida.
    """
    # Dicionário que mapeia o nome (string) para a função do Python
    algoritmos_suportados = {
        'MD5': hashlib.md5,
        'SHA-1': hashlib.sha1,
        'SHA-256': hashlib.sha256,
        'SHA-512': hashlib.sha512
    }
   
    # Se o detector não souber o que é, a gente pula
    if algoritmo not in algoritmos_suportados:
        return None

    try:
        # Abre a wordlist modo leitura ('r'), ignorando erros de acentuação
        with open(wordlist_path, 'r', errors='ignore') as f:
            for senha in f:
                senha = senha.strip() # Remove o "Enter" do final
               
                # A Mágica: Transforma a senha da lista em hash
                hash_calculada = algoritmos_suportados[algoritmo](senha.encode('utf-8')).hexdigest()
               
                # Compara
                if hash_calculada == target_hash:
                    return senha # ACHOU! Retorna a senha limpa
                   
    except FileNotFoundError:
        return "ERRO: Wordlist não encontrada"
   
    return None # Se rodou a lista toda e não achou
