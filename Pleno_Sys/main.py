from getpass import getpass
from datetime import datetime
from termcolor import colored
import pytz
import json
import os


## clear command ###
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()

ids = ['henrique@pleno', 'carlos@9100', 'rogerio@', 'rodrigo@']
tz = pytz.timezone('America/Sao_Paulo')

### ↓ Estoque Notebooks ↓ ###

with open('disponiveis/notes_disponiveis_dicionario', 'r') as f:
    notes_disponiveis_dicionario = json.load(f)

with open('eventos/notes_evento_dicionario', 'r') as f:
    notes_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras', 'r') as f:
    codigo_de_barras = json.load(f)

### ↑ Estoque Notebooks ↑ ###

### ↓ Estoque TV 42 ↓ ###

with open('disponiveis/tv42_disponiveis_dicionario', 'r') as f:
    tv42_disponiveis_dicionario = json.load(f)

with open('eventos/tv42_evento_dicionario', 'r') as f:
    tv42_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv42', 'r') as f:
    codigo_de_barras_tv42 = json.load(f)

### ↑ Estoque TV 42 ↑ ###


### ↓ Estoque TV 22 ↓ ###

with open('disponiveis/tv22_disponiveis_dicionario', 'r') as f:
    tv22_disponiveis_dicionario = json.load(f)

with open('eventos/tv22_evento_dicionario', 'r') as f:
    tv22_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv22', 'r') as f:
    codigo_de_barras_tv22 = json.load(f)

### ↑ Estoque TV 22 ↑ ###


### ↓ Estoque TV 28 ↓ ###

with open('disponiveis/tv28_disponiveis_dicionario', 'r') as f:
    tv28_disponiveis_dicionario = json.load(f)

with open('eventos/tv28_evento_dicionario', 'r') as f:
    tv28_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv28', 'r') as f:
    codigo_de_barras_tv28 = json.load(f)

### ↑ Estoque TV 28 ↑ ###


### ↓ Estoque TV 32 ↓ ###

with open('disponiveis/tv32_disponiveis_dicionario', 'r') as f:
    tv32_disponiveis_dicionario = json.load(f)

with open('eventos/tv32_evento_dicionario', 'r') as f:
    tv32_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv32', 'r') as f:
    codigo_de_barras_tv32 = json.load(f)

### ↑ Estoque TV 32 ↑ ###


### ↓ Estoque TV 43 ↓ ###

with open('disponiveis/tv43_disponiveis_dicionario', 'r') as f:
    tv43_disponiveis_dicionario = json.load(f)

with open('eventos/tv43_evento_dicionario', 'r') as f:
    tv43_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv43', 'r') as f:
    codigo_de_barras_tv43 = json.load(f)

### ↑ Estoque TV 43 ↑ ###


### ↓ Estoque TV 46 ↓ ###

with open('disponiveis/tv46_disponiveis_dicionario', 'r') as f:
    tv46_disponiveis_dicionario = json.load(f)

with open('eventos/tv46_evento_dicionario', 'r') as f:
    tv46_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv46', 'r') as f:
    codigo_de_barras_tv46 = json.load(f)

### ↑ Estoque TV 46 ↑ ###


### ↓ Estoque TV 49 ↓ ###

with open('disponiveis/tv49_disponiveis_dicionario', 'r') as f:
    tv49_disponiveis_dicionario = json.load(f)

with open('eventos/tv49_evento_dicionario', 'r') as f:
    tv49_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv49', 'r') as f:
    codigo_de_barras_tv49 = json.load(f)

### ↑ Estoque TV 49 ↑ ###


### ↓ Estoque TV 55 ↓ ###

with open('disponiveis/tv55_disponiveis_dicionario', 'r') as f:
    tv55_disponiveis_dicionario = json.load(f)

with open('eventos/tv55_evento_dicionario', 'r') as f:
    tv55_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv55', 'r') as f:
    codigo_de_barras_tv55 = json.load(f)

### ↑ Estoque TV 55 ↑ ###


### ↓ Estoque TV 65 ↓ ###

with open('disponiveis/tv65_disponiveis_dicionario', 'r') as f:
    tv65_disponiveis_dicionario = json.load(f)

with open('eventos/tv65_evento_dicionario', 'r') as f:
    tv65_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv65', 'r') as f:
    codigo_de_barras_tv65 = json.load(f)

### ↑ Estoque TV 65 ↑ ###


### ↓ Estoque TV 72 ↓ ###

with open('disponiveis/tv72_disponiveis_dicionario', 'r') as f:
    tv72_disponiveis_dicionario = json.load(f)

with open('eventos/tv72_evento_dicionario', 'r') as f:
    tv72_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv72', 'r') as f:
    codigo_de_barras_tv72 = json.load(f)

### ↑ Estoque TV 72 ↑ ###


### ↓ Estoque TV 75 ↓ ###

with open('disponiveis/tv75_disponiveis_dicionario', 'r') as f:
    tv75_disponiveis_dicionario = json.load(f)

with open('eventos/tv75_evento_dicionario', 'r') as f:
    tv75_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv75', 'r') as f:
    codigo_de_barras_tv75 = json.load(f)

### ↑ Estoque TV 75 ↑ ###


### ↓ Estoque TV 84 ↓ ###

with open('disponiveis/tv84_disponiveis_dicionario', 'r') as f:
    tv84_disponiveis_dicionario = json.load(f)

with open('eventos/tv84_evento_dicionario', 'r') as f:
    tv84_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv84', 'r') as f:
    codigo_de_barras_tv84 = json.load(f)

### ↑ Estoque TV 84 ↑ ###


### ↓ Estoque vw 47 ↓ ###

with open('disponiveis/vw47_disponiveis_dicionario', 'r') as f:
    vw47_disponiveis_dicionario = json.load(f)

with open('eventos/vw47_evento_dicionario', 'r') as f:
    vw47_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_vw47', 'r') as f:
    codigo_de_barras_vw47 = json.load(f)

### ↑ Estoque vw 47 ↑ ###


### ↓ Estoque vw 55 ↓ ###

with open('disponiveis/vw55_disponiveis_dicionario', 'r') as f:
    vw55_disponiveis_dicionario = json.load(f)

with open('eventos/vw55_evento_dicionario', 'r') as f:
    vw55_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_vw55', 'r') as f:
    codigo_de_barras_vw55 = json.load(f)


### ↑ Estoque vw 55 ↑ ###


### ↓ Login ↓ ###

def login():
    global id
    id = getpass("Insira seu ID: ")
    if id in ids:
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | connectado ás {} |".format(id, datetime.now(tz)))
        logs.close()
        print("\nConectado com sucesso. ")
        menu()
    else:
        print(colored("ERROR: ID não está registrada.", 'yellow'))
        login()


### ↑ Login ↑ ###

### ↓ PRINT NOTES ↓ ###

def print_notes_disponiveis():
    print(colored("\n↓ Notebooks no estoque ↓", 'green'))
    for key, value in notes_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ Notebooks no estoque ↑", 'green'))


def print_notes_evento():
    print(colored("\n↓ Notebooks em eventos ↓", 'red'))
    for key, value in notes_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ Notebooks em eventos ↑", 'red'))
    print(colored('Total de notes em eventos: ' + str(len(notes_evento_dicionario.keys())), 'red'))


### ↑ PRINT NOTES ↑ ###

### ↓ PRINT TV42 ↓ ###

def print_tv42_disponiveis():
    print(colored("\n↓ TV's 42\" no estoque ↓", 'green'))
    for key, value in tv42_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 42\" no estoque ↑", 'green'))
    print(colored('Total de TV\'s 42\" em estoque: ' + str(len(tv42_disponiveis_dicionario.keys())), 'green'))


def print_tv42_evento():
    print(colored("\n↓ TV's 42\" em eventos ↓", 'red'))
    for key, value in tv42_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 42\" em eventos ↑", 'red'))
    print(colored('Total de TV\'s 42\" em eventos: ' + str(len(tv42_evento_dicionario.keys())), 'red'))


### ↑ PRINT TV42 ↑ ###


### ↓ PRINT TV22 ↓ ###

def print_tv22_disponiveis():
    print(colored("\n↓ TV's 22\" no estoque ↓", 'green'))
    for key, value in tv22_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 22\" no estoque ↑", 'green'))
    print(colored('Total de TV\'s 22\" em estoque: ' + str(len(tv22_disponiveis_dicionario.keys())), 'green'))


def print_tv22_evento():
    print(colored("\n↓ TV's 22\" em eventos ↓", 'red'))
    for key, value in tv22_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 22\" em eventos ↑", 'red'))
    print(colored('Total de TV\'s 22\" em eventos: ' + str(len(tv22_evento_dicionario.keys())), 'red'))


### ↑ PRINT TV22 ↑ ###


### ↓ PRINT TV28 ↓ ###

def print_tv28_disponiveis():
    print(colored("\n↓ TV's 28\" no estoque ↓", 'green'))
    for key, value in tv28_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 28\" no estoque ↑", 'green'))
    print(colored('Total de TV\'s 28\" em estoque: ' + str(len(tv28_disponiveis_dicionario.keys())), 'green'))


def print_tv28_evento():
    print(colored("\n↓ TV's 28\" em eventos ↓", 'red'))
    for key, value in tv28_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 28\" em eventos ↑", 'red'))
    print(colored('Total de TV\'s 28\" em eventos: ' + str(len(tv28_evento_dicionario.keys())), 'red'))


### ↑ PRINT TV28 ↑ ###


### ↓ PRINT TV32 ↓ ###

def print_tv32_disponiveis():
    print(colored("\n↓ TV's 32\" no estoque ↓", 'green'))
    for key, value in tv32_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 32\" no estoque ↑", 'green'))
    print(colored('Total de TV\'s 32\" em estoque: ' + str(len(tv32_disponiveis_dicionario.keys())), 'green'))


def print_tv32_evento():
    print(colored("\n↓ TV's 32\" em eventos ↓", 'red'))
    for key, value in tv32_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 32\" em eventos ↑", 'red'))
    print(colored('Total de TV\'s 32\" em eventos: ' + str(len(tv32_evento_dicionario.keys())), 'red'))


### ↑ PRINT TV32 ↑ ###


### ↓ PRINT TV43 ↓ ###

def print_tv43_disponiveis():
    print(colored("\n↓ TV's 43\" no estoque ↓", 'green'))
    for key, value in tv43_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 43\" no estoque ↑", 'green'))
    print(colored('Total de TV\'s 43\" em estoque: ' + str(len(tv43_disponiveis_dicionario.keys())), 'green'))


def print_tv43_evento():
    print(colored("\n↓ TV's 43\" em eventos ↓", 'red'))
    for key, value in tv43_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 43\" em eventos ↑", 'red'))
    print(colored('Total de TV\'s 43\" em eventos: ' + str(len(tv43_evento_dicionario.keys())), 'red'))


### ↑ PRINT TV43 ↑ ###


### ↓ PRINT TV46 ↓ ###

def print_tv46_disponiveis():
    print(colored("\n↓ TV's 46\" no estoque ↓", 'green'))
    for key, value in tv46_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 46\" no estoque ↑", 'green'))
    print(colored('Total de TV\'s 46\" em estoque: ' + str(len(tv46_disponiveis_dicionario.keys())), 'green'))


def print_tv46_evento():
    print(colored("\n↓ TV's 46\" em eventos ↓", 'red'))
    for key, value in tv46_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 46\" em eventos ↑", 'red'))
    print(colored('Total de TV\'s 46\" em eventos: ' + str(len(tv46_evento_dicionario.keys())), 'red'))


### ↑ PRINT TV46 ↑ ###


### ↓ PRINT TV49 ↓ ###

def print_tv49_disponiveis():
    print(colored("\n↓ TV's 49\" no estoque ↓", 'green'))
    for key, value in tv49_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 49\" no estoque ↑", 'green'))
    print(colored('Total de TV\'s 49\" em estoque: ' + str(len(tv49_disponiveis_dicionario.keys())), 'green'))


def print_tv49_evento():
    print(colored("\n↓ TV's 49\" em eventos ↓", 'red'))
    for key, value in tv49_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 49\" em eventos ↑", 'red'))
    print(colored('Total de TV\'s 49\" em eventos: ' + str(len(tv49_evento_dicionario.keys())), 'red'))


### ↑ PRINT TV49 ↑ ###


### ↓ PRINT TV55 ↓ ###

def print_tv55_disponiveis():
    print(colored("\n↓ TV's 55\" no estoque ↓", 'green'))
    for key, value in tv55_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 55\" no estoque ↑", 'green'))
    print(colored('Total de TV\'s 55\" em estoque: ' + str(len(tv55_disponiveis_dicionario.keys())), 'green'))


def print_tv55_evento():
    print(colored("\n↓ TV's 55\" em eventos ↓", 'red'))
    for key, value in tv55_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 55\" em eventos ↑", 'red'))
    print(colored('Total de TV\'s 55\" em eventos: ' + str(len(tv55_evento_dicionario.keys())), 'red'))


### ↑ PRINT TV55 ↑ ###

### ↓ PRINT TV65 ↓ ###

def print_tv65_disponiveis():
    print(colored("\n↓ TV's 65\" no estoque ↓", 'green'))
    for key, value in tv65_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 65\" no estoque ↑", 'green'))
    print(colored('Total de TV\'s 65\" em estoque: ' + str(len(tv65_disponiveis_dicionario.keys())), 'green'))


def print_tv65_evento():
    print(colored("\n↓ TV's 65\" em eventos ↓", 'red'))
    for key, value in tv65_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 65\" em eventos ↑", 'red'))
    print(colored('Total de TV\'s 65\" em eventos: ' + str(len(tv65_evento_dicionario.keys())), 'red'))


### ↑ PRINT TV65 ↑ ###

### ↓ PRINT TV72 ↓ ###

def print_tv72_disponiveis():
    print(colored("\n↓ TV's 72\" no estoque ↓", 'green'))
    for key, value in tv72_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 72\" no estoque ↑", 'green'))
    print(colored('Total de TV\'s 72\" em estoque: ' + str(len(tv72_disponiveis_dicionario.keys())), 'green'))


def print_tv72_evento():
    print(colored("\n↓ TV's 72\" em eventos ↓", 'red'))
    for key, value in tv72_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 72\" em eventos ↑", 'red'))
    print(colored('Total de TV\'s 72\" em eventos: ' + str(len(tv72_evento_dicionario.keys())), 'red'))


### ↑ PRINT TV72 ↑ ###

### ↓ PRINT TV75 ↓ ###

def print_tv75_disponiveis():
    print(colored("\n↓ TV's 75\" no estoque ↓", 'green'))
    for key, value in tv75_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 75\" no estoque ↑", 'green'))
    print(colored('Total de TV\'s 75\" em estoque: ' + str(len(tv75_disponiveis_dicionario.keys())), 'green'))


def print_tv75_evento():
    print(colored("\n↓ TV's 75\" em eventos ↓", 'red'))
    for key, value in tv75_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 75\" em eventos ↑", 'red'))
    print(colored('Total de TV\'s 75\" em eventos: ' + str(len(tv75_evento_dicionario.keys())), 'red'))


### ↑ PRINT TV75 ↑ ###

### ↓ PRINT TV84 ↓ ###

def print_tv84_disponiveis():
    print(colored("\n↓ TV's 84\" no estoque ↓", 'green'))
    for key, value in tv84_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 84\" no estoque ↑", 'green'))
    print(colored('Total de TV\'s 84\" em estoque: ' + str(len(tv84_disponiveis_dicionario.keys())), 'green'))


def print_tv84_evento():
    print(colored("\n↓ TV's 84\" em eventos ↓", 'red'))
    for key, value in tv84_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 84\" em eventos ↑", 'red'))
    print(colored('Total de TV\'s 84\" em eventos: ' + str(len(tv84_evento_dicionario.keys())), 'red'))


### ↑ PRINT TV84 ↑ ###

### ↓ PRINT vw47 ↓ ###

def print_vw47_disponiveis():
    print(colored("\n↓ vw's 47\" no estoque ↓", 'green'))
    for key, value in vw47_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ vw's 47\" no estoque ↑", 'green'))
    print(colored('Total de vw\'s 47\" em estoque: ' + str(len(vw47_disponiveis_dicionario.keys())), 'green'))


def print_vw47_evento():
    print(colored("\n↓ vw's 47\" em eventos ↓", 'red'))
    for key, value in vw47_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ vw's 47\" em eventos ↑", 'red'))
    print(colored('Total de vw\'s 47\" em eventos: ' + str(len(vw47_evento_dicionario.keys())), 'red'))


### ↑ PRINT vw47 ↑ ###

### ↓ PRINT vw55 ↓ ###

def print_vw55_disponiveis():
    print(colored("\n↓ vw's 55\" no estoque ↓", 'green'))
    for key, value in vw55_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ vw's 55\" no estoque ↑", 'green'))
    print(colored('Total de vw\'s 55\" em estoque: ' + str(len(vw55_disponiveis_dicionario.keys())), 'green'))


def print_vw55_evento():
    print(colored("\n↓ vw's 55\" em eventos ↓", 'red'))
    for key, value in vw55_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ vw's 55\" em eventos ↑", 'red'))
    print(colored('Total de vw\'s 55\" em eventos: ' + str(len(vw55_evento_dicionario.keys())), 'red'))


### ↑ PRINT vw55 ↑ ###


### Menu Principal ###

def menu():
    escolha = input(
        '\nQual estoque você gostaria de acessar, escolha o número da ação:\n \n[1] Notebooks \n[2] TV\'s \n[3] Leds \n[9] Sair \nPleno:')
    if escolha == "1":
        cls()
        print("\nRedirecionado para o estoque de notebooks.")
        main()
    elif escolha == "2":
        cls()
        modelo = input(
            "\nQual modelo você gostaria?\n \n[1] TV 22\" \n[2] TV 28\" \n[3] TV 32\" \n[4] TV 42\" \n[5] TV 43\" \n[6] TV 46\" \n[7] TV 49\" \n[8] TV 55\" \n[9] Vw 55\" \n[10] Vw 47\" \n[11] TV 65\"  \n[12] TV 72\" \n[13] TV 75\" \n[14] TV 84\"   \nPleno: ")
        if modelo == "1":
            print("\nRedirecionado para o estoque de TV\'s 22\".")
            tv22()
        elif modelo == "2":
            print("\nRedirecionado para o estoque de TV\'s 28\".")
            tv28()
        elif modelo == "3":
            print("\nRedirecionado para o estoque de TV\'s 32\".")
            tv32()
        elif modelo == "4":
            print("\nRedirecionado para o estoque de TV\'s 42\".")
            tv42()
        elif modelo == "5":
            print("\nRedirecionado para o estoque de TV\'s 43\".")
            tv43()
        elif modelo == "6":
            print("\nRedirecionado para o estoque de TV\'s 46\".")
            tv46()
        elif modelo == "7":
            print("\nRedirecionado para o estoque de TV\'s 49\".")
            tv49()
        elif modelo == "8":
            print("\nRedirecionado para o estoque de TV\'s 55\".")
            tv55()
        elif modelo == "9":
            print("\nRedirecionado para o estoque de Vw\'s 55\".")
            vw55()
        elif modelo == "10":
            print("\nRedirecionado para o estoque de Vw\'s 47\".")
            vw47()
        elif modelo == "11":
            print("\nRedirecionado para o estoque de TV\'s 65\".")
            tv65()
        elif modelo == "12":
            print("\nRedirecionado para o estoque de TV\'s 72\".")
            tv72()
        elif modelo == "13":
            print("\nRedirecionado para o estoque de TV\'s 75\".")
            tv75()
        elif modelo == "14":
            print("\nRedirecionado para o estoque de TV\'s 84\".")
            tv84()
        else:
            print(colored("ERROR: Opção inválida.", 'yellow'))
            menu()
    elif escolha == "3":
        print("Woking on it")
        menu()
    elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()
    else:
        print(colored('Error: Opção inválida', 'yellow'))
        menu()


### Menu Principal ###

### ↓ Escolhas TV 49 ↓ ###
def tv49():
    escolha = input(
        '\nTV 49: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_tv49()
    elif escolha == "2":
        retorno_tv49()

    elif escolha == "3":
        cls()
        print_tv49_disponiveis()
        print_tv49_evento()
        tv49()

    elif escolha == "4":
        cls()
        print('Redirecionado para o menu principal.')
        menu()

    elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()

    else:
        print(colored('Error: Opção inválida', 'yellow'))
        tv49()


### ↑ Escolhas TV 49 ↑ ###
### ↓ Funções TV 49 ↓ ###

def retirar_tv49():
    cls()
    print_tv49_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_tv49:
        note_selecionado = codigo_de_barras_tv49.get(codigo_escaneado)
        if note_selecionado in tv49_disponiveis_dicionario:
            tv49_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou TV 49\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            tv49_evento_dicionario[note_selecionado] = (evento, data)
            with open("tv49_disponiveis_dicionario", 'w') as f:
                json.dump(tv49_disponiveis_dicionario, f)
            with open("tv49_evento_dicionario", 'w') as f:
                json.dump(tv49_evento_dicionario, f)
            cls()
            print_tv49_disponiveis()
            print_tv49_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra TV 49\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_tv49_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_tv49:
                        note_selecionado = codigo_de_barras_tv49.get(codigo_escaneado)
                        if note_selecionado in tv49_disponiveis_dicionario:
                            tv49_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou TV 49\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            tv49_evento_dicionario[note_selecionado] = (evento, data)
                            with open("tv49_disponiveis_dicionario", 'w') as f:
                                json.dump(tv49_disponiveis_dicionario, f)
                            with open("tv49_evento_dicionario", 'w') as f:
                                json.dump(tv49_evento_dicionario, f)
                            cls()
                            print_tv49_disponiveis()
                            print_tv49_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_tv49()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    tv49()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            tv49()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv49()


def retorno_tv49():
    cls()
    print_tv49_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_tv49:
        note_selecionado = codigo_de_barras_tv49.get(codigo_escaneado)
        if note_selecionado in tv49_evento_dicionario:
            tv49_evento_dicionario.pop(note_selecionado)
            tv49_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("tv49_evento_dicionario", 'w') as f:
                json.dump(tv49_evento_dicionario, f)
            with open("tv49_disponiveis_dicionario", 'w') as f:
                json.dump(tv49_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou TV 49\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_tv49_disponiveis()
            print_tv49_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra TV 49\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_tv49()
                elif confirmar == "2":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    menu()
                else:
                    print(colored("ERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retorno()

            confirmar_retorno()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em evento.", 'yellow'))
            tv49()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv49()


### ↑ Funções TV 49 ↑ ###


### ↓ Escolhas TV 22 ↓ ###
def tv22():
    escolha = input(
        '\nTV 22: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_tv22()
    elif escolha == "2":
        retorno_tv22()

    elif escolha == "3":
        cls()
        print_tv22_disponiveis()
        print_tv22_evento()
        tv22()

    elif escolha == "4":
        cls()
        print('Redirecionado para o menu principal.')
        menu()

    elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()

    else:
        print(colored('Error: Opção inválida', 'yellow'))
        tv22()


### ↑ Escolhas TV 22 ↑ ###
### ↓ Funções TV 22 ↓ ###

def retirar_tv22():
    cls()
    print_tv22_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_tv22:
        note_selecionado = codigo_de_barras_tv22.get(codigo_escaneado)
        if note_selecionado in tv22_disponiveis_dicionario:
            tv22_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou TV 22\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            tv22_evento_dicionario[note_selecionado] = (evento, data)
            with open("tv22_disponiveis_dicionario", 'w') as f:
                json.dump(tv22_disponiveis_dicionario, f)
            with open("tv22_evento_dicionario", 'w') as f:
                json.dump(tv22_evento_dicionario, f)
            cls()
            print_tv22_disponiveis()
            print_tv22_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra TV 22\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_tv22_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_tv22:
                        note_selecionado = codigo_de_barras_tv22.get(codigo_escaneado)
                        if note_selecionado in tv22_disponiveis_dicionario:
                            tv22_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou TV 22\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            tv22_evento_dicionario[note_selecionado] = (evento, data)
                            with open("tv22_disponiveis_dicionario", 'w') as f:
                                json.dump(tv22_disponiveis_dicionario, f)
                            with open("tv22_evento_dicionario", 'w') as f:
                                json.dump(tv22_evento_dicionario, f)
                            cls()
                            print_tv22_disponiveis()
                            print_tv22_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_tv22()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    tv22()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            tv22()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv22()


def retorno_tv22():
    cls()
    print_tv22_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_tv22:
        note_selecionado = codigo_de_barras_tv22.get(codigo_escaneado)
        if note_selecionado in tv22_evento_dicionario:
            tv22_evento_dicionario.pop(note_selecionado)
            tv22_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("tv22_evento_dicionario", 'w') as f:
                json.dump(tv22_evento_dicionario, f)
            with open("tv22_disponiveis_dicionario", 'w') as f:
                json.dump(tv22_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou TV 22\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_tv22_disponiveis()
            print_tv22_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra TV 22\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_tv22()
                elif confirmar == "2":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    menu()
                else:
                    print(colored("ERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retorno()

            confirmar_retorno()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em evento.", 'yellow'))
            tv22()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv22()


### ↑ Funções TV 22 ↑ ###


### ↓ Escolhas TV 28 ↓ ###
def tv28():
    escolha = input(
        '\nTV 28: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_tv28()
    elif escolha == "2":
        retorno_tv28()

    elif escolha == "3":
        cls()
        print_tv28_disponiveis()
        print_tv28_evento()
        tv28()

    elif escolha == "4":
        cls()
        print('Redirecionado para o menu principal.')
        menu()

    elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()

    else:
        print(colored('Error: Opção inválida', 'yellow'))
        tv28()


### ↑ Escolhas TV 28 ↑ ###
### ↓ Funções TV 28 ↓ ###

def retirar_tv28():
    cls()
    print_tv28_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_tv28:
        note_selecionado = codigo_de_barras_tv28.get(codigo_escaneado)
        if note_selecionado in tv28_disponiveis_dicionario:
            tv28_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou TV 28\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            tv28_evento_dicionario[note_selecionado] = (evento, data)
            with open("tv28_disponiveis_dicionario", 'w') as f:
                json.dump(tv28_disponiveis_dicionario, f)
            with open("tv28_evento_dicionario", 'w') as f:
                json.dump(tv28_evento_dicionario, f)
            cls()
            print_tv28_disponiveis()
            print_tv28_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra TV 28\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_tv28_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_tv28:
                        note_selecionado = codigo_de_barras_tv28.get(codigo_escaneado)
                        if note_selecionado in tv28_disponiveis_dicionario:
                            tv28_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou TV 28\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            tv28_evento_dicionario[note_selecionado] = (evento, data)
                            with open("tv28_disponiveis_dicionario", 'w') as f:
                                json.dump(tv28_disponiveis_dicionario, f)
                            with open("tv28_evento_dicionario", 'w') as f:
                                json.dump(tv28_evento_dicionario, f)
                            cls()
                            print_tv28_disponiveis()
                            print_tv28_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_tv28()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    tv28()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            tv28()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv28()


def retorno_tv28():
    cls()
    print_tv28_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_tv28:
        note_selecionado = codigo_de_barras_tv28.get(codigo_escaneado)
        if note_selecionado in tv28_evento_dicionario:
            tv28_evento_dicionario.pop(note_selecionado)
            tv28_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("tv28_evento_dicionario", 'w') as f:
                json.dump(tv28_evento_dicionario, f)
            with open("tv28_disponiveis_dicionario", 'w') as f:
                json.dump(tv28_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou TV 28\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_tv28_disponiveis()
            print_tv28_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra TV 28\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_tv28()
                elif confirmar == "2":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    menu()
                else:
                    print(colored("ERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retorno()

            confirmar_retorno()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em evento.", 'yellow'))
            tv28()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv28()


### ↑ Funções TV 28 ↑ ###


### ↓ Escolhas TV 32 ↓ ###
def tv32():
    escolha = input(
        '\nTV 32: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_tv32()
    elif escolha == "2":
        retorno_tv32()

    elif escolha == "3":
        cls()
        print_tv32_disponiveis()
        print_tv32_evento()
        tv32()

    elif escolha == "4":
        cls()
        print('Redirecionado para o menu principal.')
        menu()

    elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()

    else:
        print(colored('Error: Opção inválida', 'yellow'))
        tv32()


### ↑ Escolhas TV 32 ↑ ###
### ↓ Funções TV 32 ↓ ###

def retirar_tv32():
    cls()
    print_tv32_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_tv32:
        note_selecionado = codigo_de_barras_tv32.get(codigo_escaneado)
        if note_selecionado in tv32_disponiveis_dicionario:
            tv32_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou TV 32\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            tv32_evento_dicionario[note_selecionado] = (evento, data)
            with open("tv32_disponiveis_dicionario", 'w') as f:
                json.dump(tv32_disponiveis_dicionario, f)
            with open("tv32_evento_dicionario", 'w') as f:
                json.dump(tv32_evento_dicionario, f)
            cls()
            print_tv32_disponiveis()
            print_tv32_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra TV 32\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_tv32_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_tv32:
                        note_selecionado = codigo_de_barras_tv32.get(codigo_escaneado)
                        if note_selecionado in tv32_disponiveis_dicionario:
                            tv32_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou TV 32\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            tv32_evento_dicionario[note_selecionado] = (evento, data)
                            with open("tv32_disponiveis_dicionario", 'w') as f:
                                json.dump(tv32_disponiveis_dicionario, f)
                            with open("tv32_evento_dicionario", 'w') as f:
                                json.dump(tv32_evento_dicionario, f)
                            cls()
                            print_tv32_disponiveis()
                            print_tv32_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_tv32()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    tv32()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            tv32()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv32()


def retorno_tv32():
    cls()
    print_tv32_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_tv32:
        note_selecionado = codigo_de_barras_tv32.get(codigo_escaneado)
        if note_selecionado in tv32_evento_dicionario:
            tv32_evento_dicionario.pop(note_selecionado)
            tv32_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("tv32_evento_dicionario", 'w') as f:
                json.dump(tv32_evento_dicionario, f)
            with open("tv32_disponiveis_dicionario", 'w') as f:
                json.dump(tv32_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou TV 32\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_tv32_disponiveis()
            print_tv32_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra TV 32\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_tv32()
                elif confirmar == "2":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    menu()
                else:
                    print(colored("ERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retorno()

            confirmar_retorno()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em evento.", 'yellow'))
            tv32()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv32()


### ↑ Funções TV 32 ↑ ###


### ↓ Escolhas TV 55 ↓ ###
def tv55():
    escolha = input(
        '\nTV 55: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_tv55()
    elif escolha == "2":
        retorno_tv55()

    elif escolha == "3":
        cls()
        print_tv55_disponiveis()
        print_tv55_evento()
        tv55()

    elif escolha == "4":
        cls()
        print('Redirecionado para o menu principal.')
        menu()

    elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()

    else:
        print(colored('Error: Opção inválida', 'yellow'))
        tv55()


### ↑ Escolhas TV 55 ↑ ###
### ↓ Funções TV 55 ↓ ###

def retirar_tv55():
    cls()
    print_tv55_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_tv55:
        note_selecionado = codigo_de_barras_tv55.get(codigo_escaneado)
        if note_selecionado in tv55_disponiveis_dicionario:
            tv55_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou TV 55\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            tv55_evento_dicionario[note_selecionado] = (evento, data)
            with open("tv55_disponiveis_dicionario", 'w') as f:
                json.dump(tv55_disponiveis_dicionario, f)
            with open("tv55_evento_dicionario", 'w') as f:
                json.dump(tv55_evento_dicionario, f)
            cls()
            print_tv55_disponiveis()
            print_tv55_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra TV 55\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_tv55_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_tv55:
                        note_selecionado = codigo_de_barras_tv55.get(codigo_escaneado)
                        if note_selecionado in tv55_disponiveis_dicionario:
                            tv55_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou TV 55\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            tv55_evento_dicionario[note_selecionado] = (evento, data)
                            with open("tv55_disponiveis_dicionario", 'w') as f:
                                json.dump(tv55_disponiveis_dicionario, f)
                            with open("tv55_evento_dicionario", 'w') as f:
                                json.dump(tv55_evento_dicionario, f)
                            cls()
                            print_tv55_disponiveis()
                            print_tv55_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_tv55()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    tv55()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            tv55()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv55()


def retorno_tv55():
    cls()
    print_tv55_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_tv55:
        note_selecionado = codigo_de_barras_tv55.get(codigo_escaneado)
        if note_selecionado in tv55_evento_dicionario:
            tv55_evento_dicionario.pop(note_selecionado)
            tv55_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("tv55_evento_dicionario", 'w') as f:
                json.dump(tv55_evento_dicionario, f)
            with open("tv55_disponiveis_dicionario", 'w') as f:
                json.dump(tv55_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou TV 55\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_tv55_disponiveis()
            print_tv55_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra TV 55\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_tv55()
                elif confirmar == "2":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    menu()
                else:
                    print(colored("ERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retorno()

            confirmar_retorno()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em evento.", 'yellow'))
            tv55()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv55()


### ↑ Funções TV 55 ↑ ###

### ↓ Escolhas TV 65 ↓ ###
def tv65():
    escolha = input(
        '\nTV 65: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_tv65()
    elif escolha == "2":
        retorno_tv65()

    elif escolha == "3":
        cls()
        print_tv65_disponiveis()
        print_tv65_evento()
        tv65()

    elif escolha == "4":
        cls()
        print('Redirecionado para o menu principal.')
        menu()

    elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()

    else:
        print(colored('Error: Opção inválida', 'yellow'))
        tv65()


### ↑ Escolhas TV 65 ↑ ###
### ↓ Funções TV 65 ↓ ###

def retirar_tv65():
    cls()
    print_tv65_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_tv65:
        note_selecionado = codigo_de_barras_tv65.get(codigo_escaneado)
        if note_selecionado in tv65_disponiveis_dicionario:
            tv65_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou TV 65\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            tv65_evento_dicionario[note_selecionado] = (evento, data)
            with open("tv65_disponiveis_dicionario", 'w') as f:
                json.dump(tv65_disponiveis_dicionario, f)
            with open("tv65_evento_dicionario", 'w') as f:
                json.dump(tv65_evento_dicionario, f)
            cls()
            print_tv65_disponiveis()
            print_tv65_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra TV 65\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_tv65_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_tv65:
                        note_selecionado = codigo_de_barras_tv65.get(codigo_escaneado)
                        if note_selecionado in tv65_disponiveis_dicionario:
                            tv65_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou TV 65\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            tv65_evento_dicionario[note_selecionado] = (evento, data)
                            with open("tv65_disponiveis_dicionario", 'w') as f:
                                json.dump(tv65_disponiveis_dicionario, f)
                            with open("tv65_evento_dicionario", 'w') as f:
                                json.dump(tv65_evento_dicionario, f)
                            cls()
                            print_tv65_disponiveis()
                            print_tv65_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_tv65()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    tv65()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            tv65()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv65()


def retorno_tv65():
    cls()
    print_tv65_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_tv65:
        note_selecionado = codigo_de_barras_tv65.get(codigo_escaneado)
        if note_selecionado in tv65_evento_dicionario:
            tv65_evento_dicionario.pop(note_selecionado)
            tv65_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("tv65_evento_dicionario", 'w') as f:
                json.dump(tv65_evento_dicionario, f)
            with open("tv65_disponiveis_dicionario", 'w') as f:
                json.dump(tv65_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou TV 65\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_tv65_disponiveis()
            print_tv65_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra TV 65\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_tv65()
                elif confirmar == "2":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    menu()
                else:
                    print(colored("ERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retorno()

            confirmar_retorno()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em evento.", 'yellow'))
            tv65()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv65()


### ↑ Funções TV 65 ↑ ###

### ↓ Escolhas TV 72 ↓ ###
def tv72():
    escolha = input(
        '\nTV 72: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_tv72()
    elif escolha == "2":
        retorno_tv72()

    elif escolha == "3":
        cls()
        print_tv72_disponiveis()
        print_tv72_evento()
        tv72()

    elif escolha == "4":
        cls()
        print('Redirecionado para o menu principal.')
        menu()

    elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()

    else:
        print(colored('Error: Opção inválida', 'yellow'))
        tv72()


### ↑ Escolhas TV 72 ↑ ###
### ↓ Funções TV 72 ↓ ###

def retirar_tv72():
    cls()
    print_tv72_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_tv72:
        note_selecionado = codigo_de_barras_tv72.get(codigo_escaneado)
        if note_selecionado in tv72_disponiveis_dicionario:
            tv72_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou TV 72\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            tv72_evento_dicionario[note_selecionado] = (evento, data)
            with open("tv72_disponiveis_dicionario", 'w') as f:
                json.dump(tv72_disponiveis_dicionario, f)
            with open("tv72_evento_dicionario", 'w') as f:
                json.dump(tv72_evento_dicionario, f)
            cls()
            print_tv72_disponiveis()
            print_tv72_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra TV 72\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_tv72_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_tv72:
                        note_selecionado = codigo_de_barras_tv72.get(codigo_escaneado)
                        if note_selecionado in tv72_disponiveis_dicionario:
                            tv72_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou TV 72\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            tv72_evento_dicionario[note_selecionado] = (evento, data)
                            with open("tv72_disponiveis_dicionario", 'w') as f:
                                json.dump(tv72_disponiveis_dicionario, f)
                            with open("tv72_evento_dicionario", 'w') as f:
                                json.dump(tv72_evento_dicionario, f)
                            cls()
                            print_tv72_disponiveis()
                            print_tv72_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_tv72()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    tv72()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            tv72()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv72()


def retorno_tv72():
    cls()
    print_tv72_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_tv72:
        note_selecionado = codigo_de_barras_tv72.get(codigo_escaneado)
        if note_selecionado in tv72_evento_dicionario:
            tv72_evento_dicionario.pop(note_selecionado)
            tv72_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("tv72_evento_dicionario", 'w') as f:
                json.dump(tv72_evento_dicionario, f)
            with open("tv72_disponiveis_dicionario", 'w') as f:
                json.dump(tv72_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou TV 72\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_tv72_disponiveis()
            print_tv72_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra TV 72\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_tv72()
                elif confirmar == "2":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    menu()
                else:
                    print(colored("ERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retorno()

            confirmar_retorno()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em evento.", 'yellow'))
            tv72()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv72()


### ↑ Funções TV 72 ↑ ###

### ↓ Escolhas TV 75 ↓ ###
def tv75():
    escolha = input(
        '\nTV 75: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_tv75()
    elif escolha == "2":
        retorno_tv75()

    elif escolha == "3":
        cls()
        print_tv75_disponiveis()
        print_tv75_evento()
        tv75()

    elif escolha == "4":
        cls()
        print('Redirecionado para o menu principal.')
        menu()

    elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()

    else:
        print(colored('Error: Opção inválida', 'yellow'))
        tv75()


### ↑ Escolhas TV 75 ↑ ###
### ↓ Funções TV 75 ↓ ###

def retirar_tv75():
    cls()
    print_tv75_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_tv75:
        note_selecionado = codigo_de_barras_tv75.get(codigo_escaneado)
        if note_selecionado in tv75_disponiveis_dicionario:
            tv75_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou TV 75\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            tv75_evento_dicionario[note_selecionado] = (evento, data)
            with open("tv75_disponiveis_dicionario", 'w') as f:
                json.dump(tv75_disponiveis_dicionario, f)
            with open("tv75_evento_dicionario", 'w') as f:
                json.dump(tv75_evento_dicionario, f)
            cls()
            print_tv75_disponiveis()
            print_tv75_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra TV 75\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_tv75_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_tv75:
                        note_selecionado = codigo_de_barras_tv75.get(codigo_escaneado)
                        if note_selecionado in tv75_disponiveis_dicionario:
                            tv75_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou TV 75\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            tv75_evento_dicionario[note_selecionado] = (evento, data)
                            with open("tv75_disponiveis_dicionario", 'w') as f:
                                json.dump(tv75_disponiveis_dicionario, f)
                            with open("tv75_evento_dicionario", 'w') as f:
                                json.dump(tv75_evento_dicionario, f)
                            cls()
                            print_tv75_disponiveis()
                            print_tv75_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_tv75()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    tv75()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            tv75()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv75()


def retorno_tv75():
    cls()
    print_tv75_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_tv75:
        note_selecionado = codigo_de_barras_tv75.get(codigo_escaneado)
        if note_selecionado in tv75_evento_dicionario:
            tv75_evento_dicionario.pop(note_selecionado)
            tv75_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("tv75_evento_dicionario", 'w') as f:
                json.dump(tv75_evento_dicionario, f)
            with open("tv75_disponiveis_dicionario", 'w') as f:
                json.dump(tv75_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou TV 75\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_tv75_disponiveis()
            print_tv75_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra TV 75\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_tv75()
                elif confirmar == "2":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    menu()
                else:
                    print(colored("ERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retorno()

            confirmar_retorno()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em evento.", 'yellow'))
            tv75()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv75()


### ↑ Funções TV 75 ↑ ###

### ↓ Escolhas TV 84 ↓ ###
def tv84():
    escolha = input(
        '\nTV 84: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_tv84()
    elif escolha == "2":
        retorno_tv84()

    elif escolha == "3":
        cls()
        print_tv84_disponiveis()
        print_tv84_evento()
        tv84()

    elif escolha == "4":
        cls()
        print('Redirecionado para o menu principal.')
        menu()

    elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()

    else:
        print(colored('Error: Opção inválida', 'yellow'))
        tv84()


### ↑ Escolhas TV 84 ↑ ###
### ↓ Funções TV 84 ↓ ###

def retirar_tv84():
    cls()
    print_tv84_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_tv84:
        note_selecionado = codigo_de_barras_tv84.get(codigo_escaneado)
        if note_selecionado in tv84_disponiveis_dicionario:
            tv84_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou TV 84\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            tv84_evento_dicionario[note_selecionado] = (evento, data)
            with open("tv84_disponiveis_dicionario", 'w') as f:
                json.dump(tv84_disponiveis_dicionario, f)
            with open("tv84_evento_dicionario", 'w') as f:
                json.dump(tv84_evento_dicionario, f)
            cls()
            print_tv84_disponiveis()
            print_tv84_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra TV 84\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_tv84_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_tv84:
                        note_selecionado = codigo_de_barras_tv84.get(codigo_escaneado)
                        if note_selecionado in tv84_disponiveis_dicionario:
                            tv84_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou TV 84\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            tv84_evento_dicionario[note_selecionado] = (evento, data)
                            with open("tv84_disponiveis_dicionario", 'w') as f:
                                json.dump(tv84_disponiveis_dicionario, f)
                            with open("tv84_evento_dicionario", 'w') as f:
                                json.dump(tv84_evento_dicionario, f)
                            cls()
                            print_tv84_disponiveis()
                            print_tv84_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_tv84()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    tv84()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            tv84()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv84()


def retorno_tv84():
    cls()
    print_tv84_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_tv84:
        note_selecionado = codigo_de_barras_tv84.get(codigo_escaneado)
        if note_selecionado in tv84_evento_dicionario:
            tv84_evento_dicionario.pop(note_selecionado)
            tv84_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("tv84_evento_dicionario", 'w') as f:
                json.dump(tv84_evento_dicionario, f)
            with open("tv84_disponiveis_dicionario", 'w') as f:
                json.dump(tv84_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou TV 84\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_tv84_disponiveis()
            print_tv84_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra TV 84\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_tv84()
                elif confirmar == "2":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    menu()
                else:
                    print(colored("ERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retorno()

            confirmar_retorno()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em evento.", 'yellow'))
            tv84()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv84()


### ↑ Funções TV 84 ↑ ###

### ↓ Escolhas vw 47 ↓ ###
def vw47():
    escolha = input(
        '\nvw 47: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_vw47()
    elif escolha == "2":
        retorno_vw47()

    elif escolha == "3":
        cls()
        print_vw47_disponiveis()
        print_vw47_evento()
        vw47()

    elif escolha == "4":
        cls()
        print('Redirecionado para o menu principal.')
        menu()

    elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()

    else:
        print(colored('Error: Opção inválida', 'yellow'))
        vw47()


### ↑ Escolhas vw 47 ↑ ###
### ↓ Funções vw 47 ↓ ###

def retirar_vw47():
    cls()
    print_vw47_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_vw47:
        note_selecionado = codigo_de_barras_vw47.get(codigo_escaneado)
        if note_selecionado in vw47_disponiveis_dicionario:
            vw47_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou vw 47\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            vw47_evento_dicionario[note_selecionado] = (evento, data)
            with open("vw47_disponiveis_dicionario", 'w') as f:
                json.dump(vw47_disponiveis_dicionario, f)
            with open("vw47_evento_dicionario", 'w') as f:
                json.dump(vw47_evento_dicionario, f)
            cls()
            print_vw47_disponiveis()
            print_vw47_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra vw 47\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_vw47_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_vw47:
                        note_selecionado = codigo_de_barras_vw47.get(codigo_escaneado)
                        if note_selecionado in vw47_disponiveis_dicionario:
                            vw47_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou vw 47\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            vw47_evento_dicionario[note_selecionado] = (evento, data)
                            with open("vw47_disponiveis_dicionario", 'w') as f:
                                json.dump(vw47_disponiveis_dicionario, f)
                            with open("vw47_evento_dicionario", 'w') as f:
                                json.dump(vw47_evento_dicionario, f)
                            cls()
                            print_vw47_disponiveis()
                            print_vw47_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_vw47()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    vw47()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            vw47()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        vw47()


def retorno_vw47():
    cls()
    print_vw47_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_vw47:
        note_selecionado = codigo_de_barras_vw47.get(codigo_escaneado)
        if note_selecionado in vw47_evento_dicionario:
            vw47_evento_dicionario.pop(note_selecionado)
            vw47_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("vw47_evento_dicionario", 'w') as f:
                json.dump(vw47_evento_dicionario, f)
            with open("vw47_disponiveis_dicionario", 'w') as f:
                json.dump(vw47_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou vw 47\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_vw47_disponiveis()
            print_vw47_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra vw 47\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_vw47()
                elif confirmar == "2":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    menu()
                else:
                    print(colored("ERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retorno()

            confirmar_retorno()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em evento.", 'yellow'))
            vw47()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        vw47()


### ↑ Funções vw 47 ↑ ###

### ↓ Escolhas vw 55 ↓ ###
def vw55():
    escolha = input(
        '\nvw 55: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_vw55()
    elif escolha == "2":
        retorno_vw55()

    elif escolha == "3":
        cls()
        print_vw55_disponiveis()
        print_vw55_evento()
        vw55()

    elif escolha == "4":
        cls()
        print('Redirecionado para o menu principal.')
        menu()

    elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()

    else:
        print(colored('Error: Opção inválida', 'yellow'))
        vw55()


### ↑ Escolhas vw 55 ↑ ###
### ↓ Funções vw 55 ↓ ###

def retirar_vw55():
    cls()
    print_vw55_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_vw55:
        note_selecionado = codigo_de_barras_vw55.get(codigo_escaneado)
        if note_selecionado in vw55_disponiveis_dicionario:
            vw55_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou vw 55\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            vw55_evento_dicionario[note_selecionado] = (evento, data)
            with open("vw55_disponiveis_dicionario", 'w') as f:
                json.dump(vw55_disponiveis_dicionario, f)
            with open("vw55_evento_dicionario", 'w') as f:
                json.dump(vw55_evento_dicionario, f)
            cls()
            print_vw55_disponiveis()
            print_vw55_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra vw 55\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_vw55_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_vw55:
                        note_selecionado = codigo_de_barras_vw55.get(codigo_escaneado)
                        if note_selecionado in vw55_disponiveis_dicionario:
                            vw55_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou vw 55\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            vw55_evento_dicionario[note_selecionado] = (evento, data)
                            with open("vw55_disponiveis_dicionario", 'w') as f:
                                json.dump(vw55_disponiveis_dicionario, f)
                            with open("vw55_evento_dicionario", 'w') as f:
                                json.dump(vw55_evento_dicionario, f)
                            cls()
                            print_vw55_disponiveis()
                            print_vw55_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_vw55()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    vw55()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            vw55()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        vw55()


def retorno_vw55():
    cls()
    print_vw55_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_vw55:
        note_selecionado = codigo_de_barras_vw55.get(codigo_escaneado)
        if note_selecionado in vw55_evento_dicionario:
            vw55_evento_dicionario.pop(note_selecionado)
            vw55_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("vw55_evento_dicionario", 'w') as f:
                json.dump(vw55_evento_dicionario, f)
            with open("vw55_disponiveis_dicionario", 'w') as f:
                json.dump(vw55_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou vw 55\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_vw55_disponiveis()
            print_vw55_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra vw 55\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_vw55()
                elif confirmar == "2":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    menu()
                else:
                    print(colored("ERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retorno()

            confirmar_retorno()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em evento.", 'yellow'))
            vw55()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        vw55()


### ↑ Funções vw 55 ↑ ###

### ↓ Escolhas TV 42 ↓ ###
def tv42():
    escolha = input(
        '\nTV 42: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_tv42()
    elif escolha == "2":
        retorno_tv42()

    elif escolha == "3":
        cls()
        print_tv42_disponiveis()
        print_tv42_evento()
        tv42()

    elif escolha == "4":
        cls()
        print('Redirecionado para o menu principal.')
        menu()

    elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()

    else:
        print(colored('Error: Opção inválida', 'yellow'))
        tv42()


### ↑ Escolhas TV 42 ↑ ###
### ↓ Funções TV 42 ↓ ###

def retirar_tv42():
    cls()
    print_tv42_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_tv42:
        note_selecionado = codigo_de_barras_tv42.get(codigo_escaneado)
        if note_selecionado in tv42_disponiveis_dicionario:
            tv42_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou TV 42\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            tv42_evento_dicionario[note_selecionado] = (evento, data)
            with open("tv42_disponiveis_dicionario", 'w') as f:
                json.dump(tv42_disponiveis_dicionario, f)
            with open("tv42_evento_dicionario", 'w') as f:
                json.dump(tv42_evento_dicionario, f)
            cls()
            print_tv42_disponiveis()
            print_tv42_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra TV 42\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_tv42_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_tv42:
                        note_selecionado = codigo_de_barras_tv42.get(codigo_escaneado)
                        if note_selecionado in tv42_disponiveis_dicionario:
                            tv42_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou TV 42\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            tv42_evento_dicionario[note_selecionado] = (evento, data)
                            with open("tv42_disponiveis_dicionario", 'w') as f:
                                json.dump(tv42_disponiveis_dicionario, f)
                            with open("tv42_evento_dicionario", 'w') as f:
                                json.dump(tv42_evento_dicionario, f)
                            cls()
                            print_tv42_disponiveis()
                            print_tv42_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_tv42()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    tv42()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            tv42()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv42()


def retorno_tv42():
    cls()
    print_tv42_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_tv42:
        note_selecionado = codigo_de_barras_tv42.get(codigo_escaneado)
        if note_selecionado in tv42_evento_dicionario:
            tv42_evento_dicionario.pop(note_selecionado)
            tv42_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("tv42_evento_dicionario", 'w') as f:
                json.dump(tv42_evento_dicionario, f)
            with open("tv42_disponiveis_dicionario", 'w') as f:
                json.dump(tv42_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou TV 42\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_tv42_disponiveis()
            print_tv42_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra TV 42\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_tv42()
                elif confirmar == "2":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    menu()
                else:
                    print(colored("ERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retorno()

            confirmar_retorno()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em evento.", 'yellow'))
            tv42()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv42()


### ↑ Funções TV 42 ↑ ###

### ↓ Escolhas TV 43 ↓ ###
def tv43():
    escolha = input(
        '\nTV 43: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_tv43()
    elif escolha == "2":
        retorno_tv43()

    elif escolha == "3":
        cls()
        print_tv43_disponiveis()
        print_tv43_evento()
        tv43()

    elif escolha == "4":
        cls()
        print('Redirecionado para o menu principal.')
        menu()

    elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()

    else:
        print(colored('Error: Opção inválida', 'yellow'))
        tv43()


### ↑ Escolhas TV 43 ↑ ###


### ↓ Funções TV 43 ↓ ###

def retirar_tv43():
    cls()
    print_tv43_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_tv43:
        note_selecionado = codigo_de_barras_tv43.get(codigo_escaneado)
        if note_selecionado in tv43_disponiveis_dicionario:
            tv43_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou TV 43\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            tv43_evento_dicionario[note_selecionado] = (evento, data)
            with open("tv43_disponiveis_dicionario", 'w') as f:
                json.dump(tv43_disponiveis_dicionario, f)
            with open("tv43_evento_dicionario", 'w') as f:
                json.dump(tv43_evento_dicionario, f)
            cls()
            print_tv43_disponiveis()
            print_tv43_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra TV 43\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_tv43_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_tv43:
                        note_selecionado = codigo_de_barras_tv43.get(codigo_escaneado)
                        if note_selecionado in tv43_disponiveis_dicionario:
                            tv43_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou TV 43\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            tv43_evento_dicionario[note_selecionado] = (evento, data)
                            with open("tv43_disponiveis_dicionario", 'w') as f:
                                json.dump(tv43_disponiveis_dicionario, f)
                            with open("tv43_evento_dicionario", 'w') as f:
                                json.dump(tv43_evento_dicionario, f)
                            cls()
                            print_tv43_disponiveis()
                            print_tv43_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_tv43()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    tv43()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            tv43()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv43()


def retorno_tv43():
    cls()
    print_tv43_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_tv43:
        note_selecionado = codigo_de_barras_tv43.get(codigo_escaneado)
        if note_selecionado in tv43_evento_dicionario:
            tv43_evento_dicionario.pop(note_selecionado)
            tv43_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("tv43_evento_dicionario", 'w') as f:
                json.dump(tv43_evento_dicionario, f)
            with open("tv43_disponiveis_dicionario", 'w') as f:
                json.dump(tv43_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou TV 43\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_tv43_disponiveis()
            print_tv43_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra TV 43\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_tv43()
                elif confirmar == "2":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    menu()
                else:
                    print(colored("ERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retorno()

            confirmar_retorno()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em evento.", 'yellow'))
            tv43()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv43()


### ↑ Funções TV 43 ↑ ###


### ↓ Escolhas TV 46 ↓ ###
def tv46():
    escolha = input(
        '\nTV 46: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_tv46()
    elif escolha == "2":
        retorno_tv46()

    elif escolha == "3":
        cls()
        print_tv46_disponiveis()
        print_tv46_evento()
        tv46()

    elif escolha == "4":
        cls()
        print('Redirecionado para o menu principal.')
        menu()

    elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()

    else:
        print(colored('Error: Opção inválida', 'yellow'))
        tv46()


### ↑ Escolhas TV 46 ↑ ###
### ↓ Funções TV 46 ↓ ###

def retirar_tv46():
    cls()
    print_tv46_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_tv46:
        note_selecionado = codigo_de_barras_tv46.get(codigo_escaneado)
        if note_selecionado in tv46_disponiveis_dicionario:
            tv46_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou TV 46\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            tv46_evento_dicionario[note_selecionado] = (evento, data)
            with open("tv46_disponiveis_dicionario", 'w') as f:
                json.dump(tv46_disponiveis_dicionario, f)
            with open("tv46_evento_dicionario", 'w') as f:
                json.dump(tv46_evento_dicionario, f)
            cls()
            print_tv46_disponiveis()
            print_tv46_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra TV 46\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_tv46_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_tv46:
                        note_selecionado = codigo_de_barras_tv46.get(codigo_escaneado)
                        if note_selecionado in tv46_disponiveis_dicionario:
                            tv46_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou TV 46\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            tv46_evento_dicionario[note_selecionado] = (evento, data)
                            with open("tv46_disponiveis_dicionario", 'w') as f:
                                json.dump(tv46_disponiveis_dicionario, f)
                            with open("tv46_evento_dicionario", 'w') as f:
                                json.dump(tv46_evento_dicionario, f)
                            cls()
                            print_tv46_disponiveis()
                            print_tv46_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_tv46()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    tv46()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            tv46()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv46()


def retorno_tv46():
    cls()
    print_tv46_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_tv46:
        note_selecionado = codigo_de_barras_tv46.get(codigo_escaneado)
        if note_selecionado in tv46_evento_dicionario:
            tv46_evento_dicionario.pop(note_selecionado)
            tv46_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("tv46_evento_dicionario", 'w') as f:
                json.dump(tv46_evento_dicionario, f)
            with open("tv46_disponiveis_dicionario", 'w') as f:
                json.dump(tv46_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou TV 46\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_tv46_disponiveis()
            print_tv46_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra TV 46\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_tv46()
                elif confirmar == "2":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    menu()
                else:
                    print(colored("ERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retorno()

            confirmar_retorno()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em evento.", 'yellow'))
            tv46()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        tv46()


### ↑ Funções TV 46 ↑ ###


### ↓ Escolhas Notes ↓ ###
def main():
    escolha = input(
        '\nNotebooks: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar()
    elif escolha == "2":
        retorno()

    elif escolha == "3":
        cls()
        print_notes_disponiveis()
        print_notes_evento()
        main()

    elif escolha == "4":
        cls()
        print('Redirecionado para o menu principal.')
        menu()

    elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()

    else:
        print(colored('Error: Opção inválida', 'yellow'))
        main()


### ↑ Escolhas Notes ↑ ###

### ↓ Funções Notes ↓ ###

def retirar():
    cls()
    print_notes_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras do notebook que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras:
        note_selecionado = codigo_de_barras.get(codigo_escaneado)
        if note_selecionado in notes_disponiveis_dicionario:
            notes_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou o notebook: {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                       datetime.now(tz)))
            logs.close()
            notes_evento_dicionario[note_selecionado] = (evento, data)
            with open("notes_disponiveis_dicionario", 'w') as f:
                json.dump(notes_disponiveis_dicionario, f)
            with open("notes_evento_dicionario", 'w') as f:
                json.dump(notes_evento_dicionario, f)
            cls()
            print_notes_disponiveis()
            print_notes_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outro notebook? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_notes_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras do notebook que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras:
                        note_selecionado = codigo_de_barras.get(codigo_escaneado)
                        if note_selecionado in notes_disponiveis_dicionario:
                            notes_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou o notebook: {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                                evento,
                                                                                                datetime.now(tz)))
                            logs.close()
                            notes_evento_dicionario[note_selecionado] = (evento, data)
                            with open("notes_disponiveis_dicionario", 'w') as f:
                                json.dump(notes_disponiveis_dicionario, f)
                            with open("notes_evento_dicionario", 'w') as f:
                                json.dump(notes_evento_dicionario, f)
                            cls()
                            print_notes_disponiveis()
                            print_notes_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    main()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            main()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        main()


def retorno():
    cls()
    print_notes_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras do notebook que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras:
        note_selecionado = codigo_de_barras.get(codigo_escaneado)
        if note_selecionado in notes_evento_dicionario:
            notes_evento_dicionario.pop(note_selecionado)
            notes_disponiveis_dicionario[note_selecionado] = 'Na unidade.'
            with open("notes_evento_dicionario", 'w') as f:
                json.dump(notes_evento_dicionario, f)
            with open("notes_disponiveis_dicionario", 'w') as f:
                json.dump(notes_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou o notebook: {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_notes_disponiveis()
            print_notes_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outro notebook? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno()
                elif confirmar == "2":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    main()
                else:
                    print(colored("ERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retorno()

            confirmar_retorno()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em evento.", 'yellow'))
            main()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        main()


### ↑ Funções Notes ↑ ###

login()