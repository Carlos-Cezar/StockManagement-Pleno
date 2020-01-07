import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

id = 0

quantidade = 71

while quantidade != 0:
  quantidade = quantidade - 1
  id = id + 1
  print('"TV46-{:02d}": "TV_46_{:02d}", '.format(id, id))


  ### "TV_43_{:02d}": "Em estoque", ### disponiveis

  ###"TV46-{:02d}": "TV_46_{:02d}", ### codigo de barras
