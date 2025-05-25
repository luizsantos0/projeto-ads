
import json
import os

def carregar_dados(arquivo):
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)
