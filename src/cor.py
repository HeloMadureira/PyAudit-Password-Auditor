class Cor:

    @staticmethod
    def vermelho(texto: str) -> str:
        return f'\033[1;31m{texto}\033[0m'

    
    @staticmethod
    def verde(texto: str) -> str:
        return f'\033[1;32m{texto}\033[0m'
    

    @staticmethod
    def amarelo(texto: str) -> str:
        return f'\033[1;33m{texto}\033[0m'
    

    @staticmethod
    def ciano(texto: str) -> str:
        return f'\033[1;36m{texto}\033[0m'