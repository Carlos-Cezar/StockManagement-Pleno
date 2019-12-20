from getpass import getpass
from datetime import datetime
import pytz
import json


ids = ['cenrique@pleno', 'carlos@pleno', 'rogerio@pleno', 'rodrigo@pleno']
tz = pytz.timezone('America/Sao_Paulo')

### ↓ Estoque ↓ ###

with open('notes_disponiveis_dicionario', 'r') as f:
  notes_disponiveis_dicionario = json.load(f)

with open('notes_evento_dicionario', 'r') as f:
  notes_evento_dicionario = json.load(f)


### ↑ Estoque ↑ ### 


### ↓ Login ↓ ###

def login():
 global id
 id = getpass("Insira seu ID: ")
 if id in ids:
   logs = open("logs.txt","a+")
   logs.write("\nID: {} | connectado às {} |".format(id,datetime.now(tz)))
   logs.close()
   print("\nConectado com sucesso. ")
   main()
 else:
   print("ID não está registrada.")
   login()
 
### ↑ Login ↑ ###

def print_notes_disponiveis():
  print("\n↓ Notebooks no estoque ↓")
  for key, value in notes_disponiveis_dicionario.items():
    print(key, ' : ', value)
  print("↑ Notebooks no estoque ↑") 

def print_notes_evento():
  print("\n↓ Notebooks em eventos ↓")
  for key, value in notes_evento_dicionario.items():
    print(key, ' : ', value)
  print("↑ Notebooks em eventos ↑") 


### ↓ Escolhas ↓ ###
def main():
  escolha = input('\nO que você gostaria de fazer, escolha o número da ação: \n1. Retirar \n2. Retorno \n3. Checar estoque \n4. Sair \nPleno:')
 
  if escolha == "1":
   retirar()
  elif escolha == "2":
   retorno()
 
  elif escolha == "3":
    print_notes_disponiveis()
    print_notes_evento()
    main()
 
  elif escolha == "4":
    logs = open("logs.txt","a+")
    logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
    logs.close()
    print("Você foi desconectado com sucesso.")
    login()
 
  else:
    print('Error: Digite o numero "1", numero "2" ou número "3".')
    main()

### ↑ Escolhas ↑ ###
 
### ↓ Funções ↓ ###
 
def retirar():
 print_notes_disponiveis()
 note_selecionado = input("\nDigite o id do notebook que você deseja retirar:")
 note_selecionado = note_selecionado.upper()
 if note_selecionado in notes_disponiveis_dicionario:
   notes_disponiveis_dicionario.pop(note_selecionado)
   evento = input("Nome do evento:")
   data = input("Data de retorno:")
   logs = open("logs.txt","a+")
   logs.write("\nID: {} |Retirou o notebook: {} | para o evento: {} | às {} |".format(id, note_selecionado, evento, datetime.now(tz)))
   logs.close()
   notes_evento_dicionario[note_selecionado] = (evento, data)
   with open("notes_disponiveis_dicionario", 'w') as f:
     json.dump(notes_disponiveis_dicionario, f)
   with open("notes_evento_dicionario", 'w') as f:
     json.dump(notes_evento_dicionario, f)
   print_notes_disponiveis()
   print_notes_evento()
   print("Notebook {} retirado com sucesso.".format(note_selecionado)
   )
   def confirmar_retirada():
     confirmar = input('\nGostaria de retirar outro notebook? \n.1 Sim \n.2 Não \nPleno:')
     if confirmar == "1":
       retirar()
     elif confirmar == "2":
       print("Ok, você será redirecionado para o inicio do programa.")
       main()
     else:
       print("Número da ação inválido.")
       confirmar_retirada()
   confirmar_retirada()
  
 else:
   print("ID do notebook selecionado é inválido.")
   main()
 
def retorno():
 print_notes_evento()
 note_selecionado = input("Digite o número do notebook que você deseja retornar:")
 note_selecionado = note_selecionado.upper()
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
   print_notes_disponiveis()
   print_notes_evento()
   print("Notebook {} retornado com sucesso.".format(note_selecionado))
   def confirmar_retorno():
     confirmar = input('\nGostaria de retornar outro notebook? \n.1 Sim \n.2 Não \nPleno:')
     if confirmar == "1":
       retorno()
     elif confirmar == "2":
       print("Ok, você será redirecionado para o inicio do programa.")
       main()
     else:
       print("Número da ação inválido.")
       confirmar_retorno()
   confirmar_retorno()
 else:
   print("ID do notebook selecionado inválido.")
   main()
 
### ↑ Funções ↑ ###

login()
