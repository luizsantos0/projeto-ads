
from dados import carregar_dados, salvar_dados
from seguranca import hash_senha, verificar_senha
from estatisticas import calcular_media, calcular_moda, calcular_mediana
from datetime import datetime

USUARIOS = 'data/usuarios.json'
ACESSOS = 'data/acessos.json'

def cadastrar_usuario():
    usuarios = carregar_dados(USUARIOS)
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    senha = input("Senha: ")
    usuarios.append({'nome': nome, 'idade': idade, 'senha': hash_senha(senha)})
    salvar_dados(USUARIOS, usuarios)
    print("Usuário cadastrado.")

def login():
    usuarios = carregar_dados(USUARIOS)
    nome = input("Nome: ")
    senha = input("Senha: ")

    for u in usuarios:
        if u['nome'] == nome and verificar_senha(senha, u['senha']):
            print("Login realizado!")
            registrar_acesso(nome)
            return nome
    print("Falha no login.")
    return None

def registrar_acesso(nome):
    acessos = carregar_dados(ACESSOS)
    from datetime import datetime
    acessos.append({'usuario': nome, 'data_hora': datetime.now().isoformat()})
    salvar_dados(ACESSOS, acessos)

def gerar_estatisticas():
    usuarios = carregar_dados(USUARIOS)
    acessos = carregar_dados(ACESSOS)

    idades = [u['idade'] for u in usuarios]
    num_acessos = len(acessos)

    print("\n--- Estatísticas ---")
    print(f"Número de Usuários: {len(usuarios)}")
    print(f"Total de Acessos: {num_acessos}")
    print(f"Idade - Média: {calcular_media(idades):.2f}, Moda: {calcular_moda(idades)}, Mediana: {calcular_mediana(idades)}")

def main():
    while True:
        print("\n1. Cadastrar\n2. Login\n3. Estatísticas\n4. Sair")
        op = input("Opção: ")

        if op == '1':
            cadastrar_usuario()
        elif op == '2':
            user = login()
            if user:
                print(f"Bem-vindo, {user}!")
        elif op == '3':
            gerar_estatisticas()
        elif op == '4':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
