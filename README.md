
# 🔐 PyAudit - Ferramenta de Auditoria de Senhas

> **Status:** ✅ Concluído (v1.0)

## 💻 Sobre o Projeto
O **PyAudit** é uma ferramenta de linha de comando (CLI) desenvolvida em Python focada em **Segurança Ofensiva**. O objetivo da ferramenta é automatizar o processo de identificação de hashes e realizar testes de força bruta (brute-force) para auditoria de senhas fracas.

Diferente de scripts simples, o PyAudit foi construído com uma **arquitetura modular**, separando a lógica de detecção, ataque e interface.

## ⚙️ Funcionalidades

* 🔍 **Auto-Detection:** Identifica automaticamente o algoritmo da hash (MD5, SHA-1, SHA-256, SHA-512) baseando-se em heurística de comprimento e regex.
* 🔨 **Ataque de Dicionário:** Realiza quebra de senhas utilizando wordlists personalizadas (ex: rockyou.txt).
* 🖥️ **Interface CLI:** Interface robusta desenvolvida com `argparse`, oferecendo menu de ajuda e flags personalizadas.
* 🎨 **Feedback Visual:** Logs coloridos e indicadores de progresso para melhor experiência do usuário (UX).

## 🛠️ Instalação e Uso

### Pré-requisitos
* Python 3.x
* Sistema Operacional Linux (Kali, Ubuntu, etc) ou macOS.

### Como rodar

**1. Clone o repositório:**
git clone https://www.google.com/search?q=https://github.com/HeloMadureira5/PyAudit.git cd PyAudit


**2. Dê permissão de execução:**
chmod +x pyaudit.py


**3. Execute a ferramenta:**

*Modo de Análise (Apenas identifica o tipo da hash):*
./pyaudit.py -f seu_arquivo.txt -m analise


*Modo de Ataque (Tenta quebrar a senha):*
./pyaudit.py -f seu_arquivo.txt -m ataque


## 📸 Screenshots

![Interface do PyAudit](Captura de Tela 2026-01-02 às 19.23.51.PNG)


## 🧠 Aprendizados
Este projeto foi desenvolvido para aprofundar conhecimentos em:
* Manipulação de Strings e Regex em Python.
* Biblioteca `hashlib` e criptografia.
* Automação de tarefas de Red Team.
* Estruturação de projetos Python (Módulos e Packages).

## ⚠️ Disclaimer
Esta ferramenta foi desenvolvida para fins **educacionais e de auditoria autorizada**. O uso indevido para atacar sistemas sem consentimento é ilegal. A desenvolvedora não se responsabiliza pelo mau uso da ferramenta.

---
Desenvolvido por **Heloísa Madureira** 🚀
