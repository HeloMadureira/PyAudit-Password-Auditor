from argparse import ArgumentParser


def valide_input() -> ArgumentParser:
    parser = ArgumentParser(description="Ferramenta de Auditoria")
    parser.add_argument("-f", "--file", help="Arquivo de hashes (alvo)", required=True)
    parser.add_argument("-w", "--wordlist", help="Caminho da wordlist", default="/usr/share/wordlists/rockyou.txt")
    parser.add_argument("-m", "--mode", choices=['analise', 'ataque'], help="Modo de operação", required=True)
    return parser.parse_args()