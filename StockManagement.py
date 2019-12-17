from getpass import getpass
from datetime import datetime
import pytz
 
notes_disponiveis = ["01C", "02C", "03C"]
notes_evento = []
ids = ['Henrique2019', 'Carlos9100']
tz = pytz.timezone('America/Sao_Paulo')

### ↓ Estoque ↓ ###

notes_disponiveis_dicionario = {
  "01C": "Na unidade.",
  "02C": "Na unidade.",
  "03C": "Na unidade."
}

notes_evento_dicionario = {

}

### ↑ Estoque ↑ ### 

### ↓ Login ↓ ###

def login():
 global id
 id = getpass("Insira seu ID: ")
 if id in ids:
   logs = open("logs.txt","a+")
   logs.write("\nID: {} | connectado às {} |".format(id,datetime.now(tz)))
   logs.close()
   main()
 else:
   print("ID não está registrada.")
   login()
 
### ↑ Login ↑ ###
 
### ↓ Escolhas ↓ ###
def main():
  escolha = input('O que você gostaria de fazer, escolha o número da ação: \n1. Retirar \n2. Retorno \n3. Checar estoque \n4. Sair \n: ')
 
  if escolha == "1":
   retirar()
  elif escolha == "2":
   retorno()
 
  elif escolha == "3":
    print("Notebooks disponiveis: " + str(notes_disponiveis_dicionario))
    print("Notebooks em evento: " + str(notes_evento_dicionario))
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
def confirmar_retirada():
  confirmar = input('Gostarian de retirar outro notebook? \n.1 Sim \n.2 Não \n: ')
  if confirmar == "1":
    retirar()
  elif confirmar == "2":
    print("Ok, você será redirecionado para o inicio do programa.")
    main()
 
### ↓ Funções ↓ ###
 
def retirar():
 print("Notebooks no estoque: " + str(notes_disponiveis_dicionario))
 note_selecionado = input("Digite o número do notebook que você deseja retirar:\n: ")
 if note_selecionado in notes_disponiveis_dicionario:
   notes_disponiveis_dicionario.pop(note_selecionado)
   evento = input("Nome do evento?\n")
   notes_evento_dicionario[note_selecionado] = evento
   print(notes_disponiveis_dicionario)
   print(notes_evento_dicionario)
   print("Notebook {} retirado com sucesso.".format(note_selecionado)
   )
   def confirmar_retirada():
     confirmar = input('Gostarian de retirar outro notebook? \n.1 Sim \n.2 Não \n: ')
     if confirmar == "1":
       retirar()
     elif confirmar == "2":
       print("Ok, você será redirecionado para o inicio do programa.")
       main()
   confirmar_retirada()
  
 else:
   print("Notebook selecionado não está na unidade.")
   retirar()
 
def retorno():
 print("Notebooks em uso: " + str(notes_evento))
 note_selecionado = input("Digite o número do notebook que você deseja retornar:\n")
 if note_selecionado in notes_evento:
   notes_evento.remove(note_selecionado)
   notes_disponiveis.append(note_selecionado)
   notes_evento.sort()
   notes_disponiveis.sort()
   print(notes_disponiveis)
   print(notes_evento)
   print("Notebook {} retornado com sucesso.".format(note_selecionado))
   confirmar = input('Gostaria de retornar outro notebook? \n.1 Sim \n.2 Não \n: ')
   if confirmar == "1":
     retorno()
   elif confirmar == "2":
     print("Ok, você será redirecionado para inicio do programa.")
     main()
 else:
   print("Notebook selecionado não é válido.")
   retorno()
 
### ↑ Funções ↑ ###

login()
 

