current_directory = "/home/redzz"
import os

def cmd_pwd():
    print(os.getcwd())

def cmd_info():
    print("NEXUS v0.1 - Seu ambiente computacional") 

def cmd_help():
        print(f"Comandos disponiveis: {list(comandos.keys())}")

def cmd_about():
     print("Nexus e um projeto independente criado por 'redzz' como uma forma de se aprofundar mais em seus estudos")

def cmd_version():
     print(f"A versao atual e {version}")
version = "0.1"

def cmd_calculator():
    a = float(input("Digite o primeiro numero:"))
    b = float(input("Digite o segundo numero: "))
    operacao = input("operacao (+, -, *, /): ")
    if operacao == "+":
        result = a + b

    elif operacao == "-":
        result = a - b
    elif operacao == "*":
        result = a * b
    elif operacao == "/":
        try:
            result = a / b
        except ZeroDivisionError:
            print("Nao e possivel dividir por zero")
            result = None
    else:
        print("Operação inválida")
        result = None

    if result is not None:
        print(f"Resultado: {result}")

def cmd_ls():
    itens = os.listdir(os.getcwd())
    for item in itens:
        print(item)

def cmd_cd():
    pasta = input("Qual pasta voce deseja ir? ")
    try:
        os.chdir(pasta)
    except FileNotFoundError:
        print(f"A pasta '{pasta}' nao existe")
    except NotADirectoryError:
        print(f"'{pasta}' nao e uma pasta")
    except PermissionError:
        print("Permissao negada")

def cmd_mkdir():
    nome = input("Digite o nome da pasta que voce deseja criar: ")
    try:
        os.mkdir(nome)
    except FileExistsError:
        print(f"A pasta '{nome}' ja existe")

def cmd_touch():
    nome = input("Digite o nome do aquivo: ")
    with open(nome, "a") as arquivo:
        pass

def cmd_cat():
    nome = input("Digite o nome do arquivo: ")
    try:
        with open(nome, "r") as arquivo:
         conteudo = arquivo.read()
        print(conteudo)
    except FileNotFoundError:
        print(f"O arquivo '{nome}' não existe")

def cmd_rm():
    nome = input("Digite o nome do aquivo para apagar: ")
    try:
        os.remove(nome)
    except FileNotFoundError:
        print(f"A pasta '{nome}' nao existe")

def cmd_notes():
    acao = input("O que voce deseja fazer? (add/list): ")

    if acao == "add":
        texto = input("Digite sua nota: ")
        with open("notes.txt", "a") as arquivo:
            arquivo.write(texto + "\n")
    elif acao == "list":
         with open("notes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for i, linha in enumerate(linhas, start=1):
                print(f"{i}. {linha.strip()}")


comandos = {
    "info": cmd_info,
    "help": cmd_help,
    "about": cmd_about,
    "version": cmd_version,
    "calculator": cmd_calculator,
    "pwd": cmd_pwd,
    "ls": cmd_ls,
    "cd": cmd_cd,
    "mkdir": cmd_mkdir,
    "touch": cmd_touch,
    "cat": cmd_cat,
    "rm": cmd_rm,
    "notes": cmd_notes,
}

while True:
    texto = input("> ")

    if texto == "exit":
        break

    if texto in comandos:
        comandos[texto]()
    else:
        print(f"Comando '{texto}' não existe")

