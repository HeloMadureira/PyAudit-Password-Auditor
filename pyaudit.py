#!/usr/bin/env python3
import argparse
import sys
import time
# Importando nossos módulos (Detector e Cracker)
from modules import detector, cracker

# --- IDENTIDADE VISUAL ---
def print_banner():
    print("""\033[1;36m
    ██████╗ ██╗   ██╗ █████╗ ██╗   ██╗██████╗ ██╗████████╗
    ██╔══██╗╚██╗ ██╔╝██╔══██╗██║   ██║██╔══██╗██║╚══██╔══╝
    ██████╔╝ ╚████╔╝ ███████║██║   ██║██║  ██║██║   ██║  
    ██╔═══╝   ╚██╔╝  ██╔══██║██║   ██║██║  ██║██║   ██║  
    ██║        ██║   ██║  ██║╚██████╔╝██████╔╝██║   ██║  
    ╚═╝        ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝   ╚═╝  
    ------------------------------------------------------
    🔥 FERRAMENTA DE ELITE PARA AUDITORIA DE SENHAS 🔥
    ------------------------------------------------------
    \033[0m""")

# --- FLUXO PRINCIPAL ---
def main():
    parser = argparse.ArgumentParser(description="Ferramenta de Auditoria")
    parser.add_argument("-f", "--file", help="Arquivo de hashes (alvo)", required=True)
    parser.add_argument("-w", "--wordlist", help="Caminho da wordlist", default="/usr/share/wordlists/rockyou.txt")
    parser.add_argument("-m", "--mode", choices=['analise', 'ataque'], help="Modo de operação", required=True)
    args = parser.parse_args()

    print_banner()
    print(f"[*] Alvo: {args.file}")
    print(f"[*] Wordlist: {args.wordlist}")
    print(f"[*] Modo: \033[1;31m{args.mode.upper()}\033[0m") # Vermelho para ficar agressivo
    print("-" * 50)
    time.sleep(1)

    # --- LÓGICA DO ATAQUE ---
    try:
        with open(args.file, 'r') as f:
            total_quebradas = 0
           
            for linha in f:
                target_hash = linha.strip()
                if not target_hash: continue

                # 1. Identificar o tipo
                tipo_algo = detector.identificar_tipo(target_hash)
               
                if args.mode == 'analise':
                    # Apenas mostra o tipo
                    print(f"[*] Hash: {target_hash[:15]}... -> \033[1;33m{tipo_algo}\033[0m")
               
                elif args.mode == 'ataque':
                    # Tenta quebrar
                    sys.stdout.write(f"[*] Atacando {target_hash[:10]}... ({tipo_algo}) -> ")
                    sys.stdout.flush()
                   
                    if tipo_algo == "Desconhecido":
                        print("Ignorado (Tipo não suportado)")
                        continue
                       
                    # Chama o nosso CRACKER.PY
                    senha_descoberta = cracker.quebrar_senha(target_hash, tipo_algo, args.wordlist)
                   
                    if senha_descoberta:
                        print(f"\033[1;32mSENHA ENCONTRADA: {senha_descoberta}\033[0m")
                        total_quebradas += 1
                    else:
                        print("\033[1;31mFALHA (Não está na lista)\033[0m")

            if args.mode == 'ataque':
                print("-" * 50)
                print(f"RESULTADO FINAL: {total_quebradas} senhas quebradas com sucesso.")

    except FileNotFoundError:
        print("\n[!] Erro: Arquivo alvo não encontrado.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
