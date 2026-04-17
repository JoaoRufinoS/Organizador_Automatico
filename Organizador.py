import os
import shutil
import sys

def organizar_pasta():
    caminho_origem = os.path.normpath(os.path.expanduser("~/Downloads"))
    
    extensoes = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'],
        'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
        'Executaveis': ['.exe', '.msi', '.bat', '.sh'],
        'Compactados': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
        'Musicas': ['.mp3', '.wav', '.flac']
    }

    if not os.path.exists(caminho_origem):
        return

    print("Organizando arquivos... Aguarde.")

    for arquivo in os.listdir(caminho_origem):
        caminho_completo_arquivo = os.path.join(caminho_origem, arquivo)

        if os.path.isdir(caminho_completo_arquivo) or arquivo == "Organizador.py":
            continue

        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()

        movido = False
        for pasta_destino, lista_extensoes in extensoes.items():
            if extensao in lista_extensoes:
                caminho_subpasta = os.path.join(caminho_origem, pasta_destino)

                if not os.path.exists(caminho_subpasta):
                    os.makedirs(caminho_subpasta)

                try:
                    shutil.move(caminho_completo_arquivo, os.path.join(caminho_subpasta, arquivo))

                    print(f"Arquivo enviado para {pasta_destino}")
                    movido = True
                except:
                    pass
                break
        
        if not movido and extensao != "":
            pasta_outros = os.path.join(caminho_origem, "Outros")
            if not os.path.exists(pasta_outros):
                os.makedirs(pasta_outros)
            try:
                shutil.move(caminho_completo_arquivo, os.path.join(pasta_outros, arquivo))
            except:
                pass

    print("\nPronto! Tudo organizado com sucesso.")

if __name__ == "__main__":
    organizar_pasta()