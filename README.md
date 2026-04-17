# 📂 Python File Organizer

> **Status do Projeto:** ✅ Concluído / Estável

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

## 📝 Descrição
Cansado da pasta de Downloads cheia de arquivos misturados? Este script em Python automatiza a organização, movendo cada arquivo para sua pasta específica baseada na extensão (.pdf, .jpg, .exe, etc). É a solução perfeita para manter sua produtividade e o sistema limpo.

---

## 🚀 Funcionalidades Principais
* **Organização Inteligente:** Separa Documentos, Imagens, Vídeos, Músicas e Executáveis.
* **Multiplataforma:** Detecta automaticamente o caminho do usuário no Windows e Linux.
* **Blindagem de Erros:** Tratamento de *Encoding* para aceitar arquivos com acentos ou caracteres especiais.
* **Pasta "Outros":** Arquivos não identificados não ficam jogados; eles vão para uma pasta de triagem.

---

## 🛠️ Tecnologias e Bibliotecas
* **Python 3.11+**
* **`os`**: Gerenciamento de diretórios e caminhos.
* **`shutil`**: Operações de alto nível em arquivos (movimentação).
* **`pathlib`**: (Opcional) Manipulação moderna de caminhos.

---

## 📁 Estrutura do Projeto
```text
.
├── Organizador.py      # Script principal
├── README.md           # Documentação do projeto
└── .gitignore          # Arquivos ignorados pelo Git
