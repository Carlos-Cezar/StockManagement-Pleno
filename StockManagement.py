from getpass import getpass
from datetime import datetime
from termcolor import colored
import pytz
import json
import os

##clear command###
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()



ids = ['henrique@pleno', 'carlos@pleno', 'rogerio@pleno', 'rodrigo@pleno']
tz = pytz.timezone('America/Sao_Paulo')

### ↓ Estoque ↓ ###


with open('notes_disponiveis_dicionario', 'r') as f:
  notes_disponiveis_dicionario = json.load(f)

with open('notes_evento_dicionario', 'r') as f:
  notes_evento_dicionario = json.load(f)


#### testing ### 

with open('codigo_de_barras', 'r') as f:
  codigo_de_barras = json.load(f)


### ↑ Estoque ↑ ### 


### ↓ Login ↓ ###

def login():
 global id
 id = getpass("Insira seu ID: ")
 if id in ids:
   logs = open("logs.txt","a+")
   logs.write("\nID: {} | connectado ás {} |".format(id,datetime.now(tz)))
   logs.close()
   print("\nConectado com sucesso. ")
   main()
 else:
   print("ID não está registrada.")
   login()
 
### ↑ Login ↑ ###

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


### ↓ Escolhas ↓ ###
def main():
  escolha = input('\nO que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Sair \nPleno:')
 
  if escolha == "1":
   retirar()
  elif escolha == "2":
   retorno()
 
  elif escolha == "3":
    cls()
    print_notes_disponiveis()
    print_notes_evento()
    print(colored('Total de notes em eventos: ' + str(len(notes_evento_dicionario.keys())), 'red'))
    main()
 
  elif escolha == "4":
    logs = open("logs.txt","a+")
    logs.write("\nID: {} | foi desconnectado ás {} |".format(id, datetime.now(tz)))
    logs.close()
    cls()
    print("Você foi desconectado com sucesso.")
    login()
 
  else:
    print('Error: Digite o numero "1", numero "2" ou número "3".')
    main()

### ↑ Escolhas ↑ ###
 
### ↓ Funções ↓ ###
 
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
     logs = open("logs.txt","a+")
     logs.write("\nID: {} |Retirou o notebook: {} | para o {} | ás {} |".format(id, note_selecionado, evento, datetime.now(tz)))
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
       confirmar = input('\nGostaria de retirar outro notebook? \n[1] Sim \n[2] Não \nPleno:')
       if confirmar == "1":
         retirar()
       elif confirmar == "2":
         print("Ok, você será redirecionado para o inicio do programa.")
         cls()
         main()
       else:
         print("Número da ação inválido.")
     confirmar_retirada()
   else:
     print(colored("\nCódigo de barras escaneado inválido ou não está em estoque.", 'yellow'))
     main()
     
 else:
   print("Código de barras escaneado inválido.")
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
     logs = open("logs.txt","a+")
     logs.write("\nID: {} |Retornou o notebook: {} | às {} |".format(id, note_selecionado, datetime.now(tz)))
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
         print("Número da ação inválido.")
         confirmar_retorno()
     confirmar_retorno()
   else:
     print(colored("\nCódigo de barras escaneado inválido ou não está em evento.", 'yellow'))
     main()
 else:
   print("Código de barras escaneado inválido.")
   main()
 
### ↑ Funções ↑ ###

login()
