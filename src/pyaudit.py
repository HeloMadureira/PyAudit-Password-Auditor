#!/usr/bin/env python3

import sys
import time
import detector
import cracker
from argparse import ArgumentParser
from parser   import valide_input
from cor      import Cor


class PyAudit:

    def __init__(self):
        self.args: ArgumentParser  = valide_input()
        self.senhas_quebradas: int = 0
        self.hashes: dict[str]     = {}     
    


    def execute(self):
        self.print_banner()
        self.print_cabecalho()
        self.analise_arquivo()
        
        match self.args.mode:
            case 'analise': self.analise()
            case 'ataque':  self.quebre_senhas()


    
    @staticmethod
    def print_banner():
        print(Cor.ciano("""
        ██████╗ ██╗   ██╗ █████╗ ██╗   ██╗██████╗ ██╗████████╗
        ██╔══██╗╚██╗ ██╔╝██╔══██╗██║   ██║██╔══██╗██║╚══██╔══╝
        ██████╔╝ ╚████╔╝ ███████║██║   ██║██║  ██║██║   ██║  
        ██╔═══╝   ╚██╔╝  ██╔══██║██║   ██║██║  ██║██║   ██║  
        ██║        ██║   ██║  ██║╚██████╔╝██████╔╝██║   ██║  
        ╚═╝        ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝   ╚═╝  
        ------------------------------------------------------
        🔥 FERRAMENTA DE ELITE PARA AUDITORIA DE SENHAS 🔥
        ------------------------------------------------------
        """))
    


    def print_cabecalho(self):
        print(f"[*] Alvo: {self.args.file}")
        print(f"[*] Wordlist: {self.args.wordlist}")
        print(f"[*] Modo: {Cor.vermelho(self.args.mode.upper())}")
        print("-" * 50)
        time.sleep(1)



    @staticmethod
    def abortar(erro: str):
        print(f'\n[!] {erro}')
        sys.exit()



    def analise_arquivo(self):
        try:   self.pegue_dados_do_arquivo()
        except FileNotFoundError: self.abortar(f'Arquivo {self.args.file} não encontrado')
        except Exception as e:    self.abortar(f'Erro desconhecido: {e}')


    
    def pegue_dados_do_arquivo(self):
        with open(self.args.file, 'r') as arquivo:
            for linha in arquivo:
                hash: str = linha.strip()
                if not hash: continue

                tipo = detector.identificar_tipo(hash)
                self.hashes[hash] = tipo

    

    def analise(self):
        for hash, tipo in self.hashes.items():
            print(f"[*] Hash: {hash[:15]}... -> {Cor.amarelo(tipo)}")


    
    def quebre_senhas(self):
        for hash, tipo in self.hashes.items():
            self.mostrar_progresso(hash, tipo)

            if tipo == "Desconhecido":
                print("Ignorado (Tipo não suportado)")
                continue

            # Chama o nosso CRACKER.PY
            resultado, texto = cracker.quebrar_senha(hash, tipo, self.args.wordlist)

            match resultado:
                case False: print(Cor.vermelho(texto))
                case True:  self.mostrar_senha_quebrada(texto)
        
        self.mostrar_resultados()



    @staticmethod
    def mostrar_progresso(hash: str, tipo: str):
        sys.stdout.write(f"[*] Atacando {hash[:10]}... ({tipo}) -> ")
        sys.stdout.flush()



    def mostrar_senha_quebrada(self, senha_descoberta: str):
        texto: str = f"SENHA ENCONTRADA: {senha_descoberta}"
        print(f"{Cor.verde(texto)}")

        self.senhas_quebradas += 1

    

    def mostrar_resultados(self):
        print("-" * 50)
        print(f"RESULTADO FINAL: {self.senhas_quebradas} senhas quebradas com sucesso.")





if __name__ == "__main__":
    try:
        pyaudit: PyAudit = PyAudit()
        pyaudit.execute()
    except KeyboardInterrupt:
        sys.exit()
