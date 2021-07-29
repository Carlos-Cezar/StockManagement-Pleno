from getpass import getpass
from datetime import datetime
from termcolor import colored
import pytz
import json
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Informatica").sheet1


## clear command ###
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

ids = ['henrique@pleno', 'carlos@9100', 'rogerio@', 'rodrigo@']
admins = ['carlos@admin', 'rogerio@admin', 'rodrigo@admin', 'henrique@admin']
tz = pytz.timezone('America/Sao_Paulo')


### ↓ Estoque Notebooks ↓ ###

with open('disponiveis/notes_disponiveis_dicionario', 'r') as f:
    notes_disponiveis_dicionario = json.load(f)

with open('eventos/notes_evento_dicionario', 'r') as f:
    notes_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras', 'r') as f:
    codigo_de_barras = json.load(f)

with open('fora_de_uso/notes_fora_de_uso', 'r') as f:
    notes_fora_de_uso = json.load(f)

### ↑ Estoque Notebooks ↑ ###


### ↓ Estoque Controladora ↓ ###

with open('disponiveis/controladora_disponiveis_dicionario', 'r') as f:
    controladora_disponiveis_dicionario = json.load(f)

with open('eventos/controladora_evento_dicionario', 'r') as f:
    controladora_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_controladora', 'r') as f:
    codigo_de_barras_controladora = json.load(f)

with open('fora_de_uso/controladora_fora_de_uso', 'r') as f:
    controladora_fora_de_uso = json.load(f)
### ↑ Estoque Controladora ↑ ###



### ↓ Estoque video_wall_4k ↓ ###

with open('disponiveis/video_wall_4k_disponiveis_dicionario', 'r') as f:
    video_wall_4k_disponiveis_dicionario = json.load(f)

with open('eventos/video_wall_4k_evento_dicionario', 'r') as f:
    video_wall_4k_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_video_wall_4k', 'r') as f:
    codigo_de_barras_video_wall_4k = json.load(f)

with open('fora_de_uso/video_wall_4k_fora_de_uso', 'r') as f:
    video_wall_4k_fora_de_uso = json.load(f)

### ↑ Estoque video_wall_4k ↑ ###



### ↓ Estoque mini_midia ↓ ###

with open('disponiveis/mini_midia_disponiveis_dicionario', 'r') as f:
    mini_midia_disponiveis_dicionario = json.load(f)

with open('eventos/mini_midia_evento_dicionario', 'r') as f:
    mini_midia_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_mini_midia', 'r') as f:
    codigo_de_barras_mini_midia = json.load(f)

with open('fora_de_uso/mini_midia_fora_de_uso', 'r') as f:
    mini_midia_fora_de_uso = json.load(f)

### ↑ Estoque mini_midia ↑ ###



### ↓ Estoque triplo_had ↓ ###

with open('disponiveis/triplo_had_disponiveis_dicionario', 'r') as f:
    triplo_had_disponiveis_dicionario = json.load(f)

with open('eventos/triplo_had_evento_dicionario', 'r') as f:
    triplo_had_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_triplo_had', 'r') as f:
    codigo_de_barras_triplo_had = json.load(f)

with open('fora_de_uso/triplo_had_fora_de_uso', 'r') as f:
    triplo_had_fora_de_uso = json.load(f)

### ↑ Estoque triplo_had ↑ ###


### ↓ Estoque placa_de_captura ↓ ###

with open('disponiveis/placa_de_captura_disponiveis_dicionario', 'r') as f:
    placa_de_captura_disponiveis_dicionario = json.load(f)

with open('eventos/placa_de_captura_evento_dicionario', 'r') as f:
    placa_de_captura_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_placa_de_captura', 'r') as f:
    codigo_de_barras_placa_de_captura = json.load(f)

with open('fora_de_uso/placa_de_captura_fora_de_uso', 'r') as f:
    placa_de_captura_fora_de_uso = json.load(f)

### ↑ Estoque placa_de_captura ↑ ###



### ↓ Estoque cpu ↓ ###

with open('disponiveis/cpu_disponiveis_dicionario', 'r') as f:
    cpu_disponiveis_dicionario = json.load(f)

with open('eventos/cpu_evento_dicionario', 'r') as f:
    cpu_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_cpu', 'r') as f:
    codigo_de_barras_cpu = json.load(f)

with open('fora_de_uso/cpu_fora_de_uso', 'r') as f:
    cpu_fora_de_uso = json.load(f)

### ↑ Estoque cpu ↑ ###



### ↓ Estoque mac ↓ ###

with open('disponiveis/mac_disponiveis_dicionario', 'r') as f:
    mac_disponiveis_dicionario = json.load(f)

with open('eventos/mac_evento_dicionario', 'r') as f:
    mac_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_mac', 'r') as f:
    codigo_de_barras_mac = json.load(f)

with open('fora_de_uso/mac_fora_de_uso', 'r') as f:
    mac_fora_de_uso = json.load(f)

### ↑ Estoque mac ↑ ###



### ↓ Estoque ac800 ↓ ###

with open('disponiveis/ac800_disponiveis_dicionario', 'r') as f:
    ac800_disponiveis_dicionario = json.load(f)

with open('eventos/ac800_evento_dicionario', 'r') as f:
    ac800_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_ac800', 'r') as f:
    codigo_de_barras_ac800 = json.load(f)

with open('fora_de_uso/ac800_fora_de_uso', 'r') as f:
    ac800_fora_de_uso = json.load(f)

### ↑ Estoque ac800 ↑ ###



### ↓ Estoque caixa_de_som_pq ↓ ###

with open('disponiveis/caixa_de_som_pq_disponiveis_dicionario', 'r') as f:
    caixa_de_som_pq_disponiveis_dicionario = json.load(f)

with open('eventos/caixa_de_som_pq_evento_dicionario', 'r') as f:
    caixa_de_som_pq_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_caixa_de_som_pq', 'r') as f:
    codigo_de_barras_caixa_de_som_pq = json.load(f)

with open('fora_de_uso/caixa_de_som_pq_fora_de_uso', 'r') as f:
    caixa_de_som_pq_fora_de_uso = json.load(f)

### ↑ Estoque caixa_de_som_pq ↑ ###



### ↓ Estoque caixa_de_som_g ↓ ###

with open('disponiveis/caixa_de_som_g_disponiveis_dicionario', 'r') as f:
    caixa_de_som_g_disponiveis_dicionario = json.load(f)

with open('eventos/caixa_de_som_g_evento_dicionario', 'r') as f:
    caixa_de_som_g_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_caixa_de_som_g', 'r') as f:
    codigo_de_barras_caixa_de_som_g = json.load(f)

with open('fora_de_uso/caixa_de_som_g_fora_de_uso', 'r') as f:
    caixa_de_som_g_fora_de_uso = json.load(f)

### ↑ Estoque caixa_de_som_g ↑ ###


### ↓ Estoque distribuidor_hdmi ↓ ###

with open('disponiveis/distribuidor_hdmi_disponiveis_dicionario', 'r') as f:
    distribuidor_hdmi_disponiveis_dicionario = json.load(f)

with open('eventos/distribuidor_hdmi_evento_dicionario', 'r') as f:
    distribuidor_hdmi_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_distribuidor_hdmi', 'r') as f:
    codigo_de_barras_distribuidor_hdmi = json.load(f)

with open('fora_de_uso/distribuidor_hdmi_fora_de_uso', 'r') as f:
    distribuidor_hdmi_fora_de_uso = json.load(f)

### ↑ Estoque distribuidor_hdmi ↑ ###


### ↓ Estoque teclado_e_mouse ↓ ###

with open('disponiveis/teclado_e_mouse_disponiveis_dicionario', 'r') as f:
    teclado_e_mouse_disponiveis_dicionario = json.load(f)

with open('eventos/teclado_e_mouse_evento_dicionario', 'r') as f:
    teclado_e_mouse_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_teclado_e_mouse', 'r') as f:
    codigo_de_barras_teclado_e_mouse = json.load(f)

with open('fora_de_uso/teclado_e_mouse_fora_de_uso', 'r') as f:
    teclado_e_mouse_fora_de_uso = json.load(f)

### ↑ Estoque teclado_e_mouse ↑ ###


### ↓ Estoque analog_way ↓ ###

with open('disponiveis/analog_way_disponiveis_dicionario', 'r') as f:
    analog_way_disponiveis_dicionario = json.load(f)

with open('eventos/analog_way_evento_dicionario', 'r') as f:
    analog_way_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_analog_way', 'r') as f:
    codigo_de_barras_analog_way = json.load(f)

with open('fora_de_uso/analog_way_fora_de_uso', 'r') as f:
    analog_way_fora_de_uso = json.load(f)
### ↑ Estoque analog_way ↑ ###


### ↓ Estoque LED 3.9 ↓ ###

with open('disponiveis/led39_disponiveis_dicionario', 'r') as f:
    led39_disponiveis_dicionario = json.load(f)

with open('eventos/led39_evento_dicionario', 'r') as f:
    led39_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_led39', 'r') as f:
    codigo_de_barras_led39 = json.load(f)

with open('fora_de_uso/led39_fora_de_uso', 'r') as f:
    led39_fora_de_uso = json.load(f)

### ↑ Estoque LED 3.9 ↑ ###


### ↓ Estoque Distribuidor HDMI ↓ ###

with open('disponiveis/distribuidor_hdmi_disponiveis_dicionario', 'r') as f:
    distribuidor_hdmi_disponiveis_dicionario = json.load(f)

with open('eventos/distribuidor_hdmi_evento_dicionario', 'r') as f:
    distribuidor_hdmi_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_distribuidor_hdmi', 'r') as f:
    codigo_de_barras_distribuidor_hdmi = json.load(f)

with open('fora_de_uso/distribuidor_hdmi_fora_de_uso', 'r') as f:
    distribuidor_hdmi_fora_de_uso = json.load(f)

### ↑ Estoque Distribuidor HDMI ↑ ###


### ↓ Estoque LED 3.0 ↓ ###

with open('disponiveis/led30_disponiveis_dicionario', 'r') as f:
    led30_disponiveis_dicionario = json.load(f)

with open('eventos/led30_evento_dicionario', 'r') as f:
    led30_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_led30', 'r') as f:
    codigo_de_barras_led30 = json.load(f)

with open('fora_de_uso/led30_fora_de_uso', 'r') as f:
    led30_fora_de_uso = json.load(f)

    
### ↑ Estoque LED 3.0 ↑ ###


### ↓ Estoque LED 2.9 ↓ ###

with open('disponiveis/led29_disponiveis_dicionario', 'r') as f:
    led29_disponiveis_dicionario = json.load(f)

with open('eventos/led29_evento_dicionario', 'r') as f:
    led29_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_led29', 'r') as f:
    codigo_de_barras_led29 = json.load(f)

with open('fora_de_uso/led29_fora_de_uso', 'r') as f:
    led29_fora_de_uso = json.load(f)

### ↑ Estoque LED 2.9 ↑ ###


### ↓ Estoque LED 2.6 ↓ ###

with open('disponiveis/led26_disponiveis_dicionario', 'r') as f:
    led26_disponiveis_dicionario = json.load(f)

with open('eventos/led26_evento_dicionario', 'r') as f:
    led26_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_led26', 'r') as f:
    codigo_de_barras_led26 = json.load(f)

with open('fora_de_uso/led26_fora_de_uso', 'r') as f:
    led26_fora_de_uso = json.load(f)

### ↑ Estoque LED 2.6 ↑ ###




### ↓ Estoque TV 42 ↓ ###

with open('disponiveis/tv42_disponiveis_dicionario', 'r') as f:
    tv42_disponiveis_dicionario = json.load(f)

with open('eventos/tv42_evento_dicionario', 'r') as f:
    tv42_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv42', 'r') as f:
    codigo_de_barras_tv42 = json.load(f)

with open('fora_de_uso/tv42_fora_de_uso', 'r') as f:
    tv42_fora_de_uso = json.load(f)

### ↑ Estoque TV 42 ↑ ###


### ↓ Estoque TV 22 ↓ ###

with open('disponiveis/tv22_disponiveis_dicionario', 'r') as f:
    tv22_disponiveis_dicionario = json.load(f)

with open('eventos/tv22_evento_dicionario', 'r') as f:
    tv22_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv22', 'r') as f:
    codigo_de_barras_tv22 = json.load(f)

with open('fora_de_uso/tv22_fora_de_uso', 'r') as f:
    tv22_fora_de_uso = json.load(f)

### ↑ Estoque TV 22 ↑ ###


### ↓ Estoque X1 / X2 ↓ ###

with open('disponiveis/x1_x2_disponiveis_dicionario', 'r') as f:
    x1_x2_disponiveis_dicionario = json.load(f)

with open('eventos/x1_x2_evento_dicionario', 'r') as f:
    x1_x2_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_x1_x2', 'r') as f:
    codigo_de_barras_x1_x2 = json.load(f)

with open('fora_de_uso/x1_x2_fora_de_uso', 'r') as f:
    x1_x2_fora_de_uso = json.load(f)

### ↑ Estoque X1 / X2 ↑ ###


### ↓ Estoque TV 28 ↓ ###

with open('disponiveis/tv28_disponiveis_dicionario', 'r') as f:
  tv28_disponiveis_dicionario = json.load(f)

with open('eventos/tv28_evento_dicionario', 'r') as f:
    tv28_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv28', 'r') as f:
    codigo_de_barras_tv28 = json.load(f)

with open('fora_de_uso/tv28_fora_de_uso', 'r') as f:
    tv28_fora_de_uso = json.load(f)

### ↑ Estoque TV 28 ↑ ###


### ↓ Estoque TV 32 ↓ ###

with open('disponiveis/tv32_disponiveis_dicionario', 'r') as f:
    tv32_disponiveis_dicionario = json.load(f)

with open('eventos/tv32_evento_dicionario', 'r') as f:
    tv32_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv32', 'r') as f:
    codigo_de_barras_tv32 = json.load(f)

with open('fora_de_uso/tv32_fora_de_uso', 'r') as f:
    tv32_fora_de_uso = json.load(f)

### ↑ Estoque TV 32 ↑ ###


### ↓ Estoque TV 43 ↓ ###

with open('disponiveis/tv43_disponiveis_dicionario', 'r') as f:
    tv43_disponiveis_dicionario = json.load(f)

with open('eventos/tv43_evento_dicionario', 'r') as f:
    tv43_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv43', 'r') as f:
    codigo_de_barras_tv43 = json.load(f)

with open('fora_de_uso/tv43_fora_de_uso', 'r') as f:
    tv43_fora_de_uso = json.load(f)

### ↑ Estoque TV 43 ↑ ###


### ↓ Estoque TV 46 ↓ ###

with open('disponiveis/tv46_disponiveis_dicionario', 'r') as f:
    tv46_disponiveis_dicionario = json.load(f)

with open('eventos/tv46_evento_dicionario', 'r') as f:
    tv46_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv46', 'r') as f:
    codigo_de_barras_tv46 = json.load(f)

with open('fora_de_uso/tv46_fora_de_uso', 'r') as f:
    tv46_fora_de_uso = json.load(f)

### ↑ Estoque TV 46 ↑ ###


### ↓ Estoque TV 49 ↓ ###

with open('disponiveis/tv49_disponiveis_dicionario', 'r') as f:
    tv49_disponiveis_dicionario = json.load(f)

with open('eventos/tv49_evento_dicionario', 'r') as f:
    tv49_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv49', 'r') as f:
    codigo_de_barras_tv49 = json.load(f)

with open('fora_de_uso/tv49_fora_de_uso', 'r') as f:
    tv49_fora_de_uso = json.load(f)

### ↑ Estoque TV 49 ↑ ###


### ↓ Estoque TV 55 ↓ ###

with open('disponiveis/tv55_disponiveis_dicionario', 'r') as f:
    tv55_disponiveis_dicionario = json.load(f)

with open('eventos/tv55_evento_dicionario', 'r') as f:
    tv55_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv55', 'r') as f:
    codigo_de_barras_tv55 = json.load(f)

with open('fora_de_uso/tv55_fora_de_uso', 'r') as f:
    tv55_fora_de_uso = json.load(f)

### ↑ Estoque TV 55 ↑ ###


### ↓ Estoque TV 65 ↓ ###

with open('disponiveis/tv65_disponiveis_dicionario', 'r') as f:
    tv65_disponiveis_dicionario = json.load(f)

with open('eventos/tv65_evento_dicionario', 'r') as f:
    tv65_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv65', 'r') as f:
    codigo_de_barras_tv65 = json.load(f)

with open('fora_de_uso/tv65_fora_de_uso', 'r') as f:
    tv65_fora_de_uso = json.load(f)
    
### ↑ Estoque TV 65 ↑ ###


### ↓ Estoque TV 72 ↓ ###

with open('disponiveis/tv72_disponiveis_dicionario', 'r') as f:
    tv72_disponiveis_dicionario = json.load(f)

with open('eventos/tv72_evento_dicionario', 'r') as f:
    tv72_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv72', 'r') as f:
    codigo_de_barras_tv72 = json.load(f)

with open('fora_de_uso/tv72_fora_de_uso', 'r') as f:
    tv72_fora_de_uso = json.load(f)

### ↑ Estoque TV 72 ↑ ###


### ↓ Estoque TV 75 ↓ ###

with open('disponiveis/tv75_disponiveis_dicionario', 'r') as f:
    tv75_disponiveis_dicionario = json.load(f)

with open('eventos/tv75_evento_dicionario', 'r') as f:
    tv75_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv75', 'r') as f:
    codigo_de_barras_tv75 = json.load(f)

with open('fora_de_uso/tv75_fora_de_uso', 'r') as f:
    tv75_fora_de_uso = json.load(f)

### ↑ Estoque TV 75 ↑ ###


### ↓ Estoque TV 84 ↓ ###

with open('disponiveis/tv84_disponiveis_dicionario', 'r') as f:
    tv84_disponiveis_dicionario = json.load(f)

with open('eventos/tv84_evento_dicionario', 'r') as f:
    tv84_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_tv84', 'r') as f:
    codigo_de_barras_tv84 = json.load(f)

with open('fora_de_uso/tv84_fora_de_uso', 'r') as f:
    tv84_fora_de_uso = json.load(f)

### ↑ Estoque TV 84 ↑ ###


### ↓ Estoque vw 47 ↓ ###

with open('disponiveis/vw47_disponiveis_dicionario', 'r') as f:
    vw47_disponiveis_dicionario = json.load(f)

with open('eventos/vw47_evento_dicionario', 'r') as f:
    vw47_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_vw47', 'r') as f:
    codigo_de_barras_vw47 = json.load(f)

with open('fora_de_uso/vw47_fora_de_uso', 'r') as f:
    vw47_fora_de_uso = json.load(f)

### ↑ Estoque vw 47 ↑ ###


### ↓ Estoque vw 55 ↓ ###

with open('disponiveis/vw55_disponiveis_dicionario', 'r') as f:
    vw55_disponiveis_dicionario = json.load(f)

with open('eventos/vw55_evento_dicionario', 'r') as f:
    vw55_evento_dicionario = json.load(f)

with open('codigo_de_barras_f/codigo_de_barras_vw55', 'r') as f:
    codigo_de_barras_vw55 = json.load(f)

with open('fora_de_uso/vw55_fora_de_uso', 'r') as f:
    vw55_fora_de_uso = json.load(f)

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
    elif id in admins:
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | connectado ás {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("\nConectado com sucesso. ")
        print(colored("\nVOCÊ ESTÁ CONNECTADO COMO ADMINISTRADOR ", 'blue'))
        admin_menu()

    else:
        print(colored("ERROR: ID não está registrada.", 'yellow'))
        login()


### ↑ Login ↑ ###





### ↓ ADMIN MENU ↓ ###
def admin_menu():
  escolha = input("\nO que você gostaria de fazer?\n \n[1] Checar estoque  \n[2] Adicionar equipamento para a lista de \"FORA DE USO\" \n[3] Resumo Estoque  \n[9] Sair \nPleno: ")
  if escolha == "1":
    cls()
    lista_de_estoques = ["controladora", "led26", "led29", "led30", "led39", "notes", "tv22", "tv28", "tv32", "tv42", "tv43", "tv46", "tv49", "tv55", "tv65", "tv72", "tv75", "tv84", "vw47", "vw55", "x1_x2", "distribuidor_hdmi", "analog_way", "video_wall_4k", "mini_midia", "teclado_e_mouse", "triplo_had", "placa_de_captura", "cpu", "mac", "ac800", "caixa_de_som_pq", "caixa_de_som_g"]
    estoque_selecionado = input("Qual estoque você gostaria de acessar?\n  \nnotes \ncontroladora \nled26 \nled29 \nled30 \nled39 \ntv22 \ntv28 \ntv32 \ntv42 \ntv43 \ntv46 \ntv49 \ntv55 \ntv65 \ntv72 \ntv75 \ntv84 \nvw47 \nvw55 \nx1_x2 \ndistribuidor_hdmi \nanalog_way \nvideo_wall_4k, \nmini_midia \nteclado_e_mouse \ntriplo had \nplaca_de_captura \ncpu \nmac \nac800 \ncaixa_de_som_pq \ncaixa_de_som_g \n  \nPleno: ")
    if estoque_selecionado in lista_de_estoques:
      print_estoque = "print_{}_disponiveis()".format(estoque_selecionado)
      eval(print_estoque)
      admin_menu()
    else:
      cls()
      print(colored("ERROR: Estoque informado não existe.", 'yellow'))
      admin_menu()
  elif escolha == "2":
    cls()
    lista_de_estoques = ["controladora", "led26", "led29", "led30", "led39", "notes", "tv22", "tv28", "tv32", "tv42", "tv43", "tv46", "tv49", "tv55", "tv65", "tv72", "tv75", "tv84", "vw47", "vw55", "x1_x2", "distribuidor_hdmi", "analog_way", "video_wall_4k", "mini_midia", "teclado_e_mouse", "triplo_had", "placa_de_captura", "cpu", "mac", "ac800", "caixa_de_som_pq", "caixa_de_som_g"]
    estoque = input("Qual estoque você gostaria de acessar?\n  \nnotes \ncontroladora \nled26 \nled29 \nled30 \nled39 \ntv22 \ntv28 \ntv32 \ntv42 \ntv43 \ntv46 \ntv49 \ntv55 \ntv65 \ntv72 \ntv75 \ntv84 \nvw47 \nvw55 \nx1_x2 \ndistribuidor_hdmi \nanalog_way \nvideo_wall_4k, \nmini_midia \nteclado_e_mouse \ntriplo had \nplaca_de_captura \ncpu \nmac \nac800 \ncaixa_de_som_pq \ncaixa_de_som_g \n  \nPleno: ")
    if estoque in lista_de_estoques:
      print_estoque = "print_{}_disponiveis()".format(estoque)
      eval(print_estoque)
      equipamento_selecionado = input("\nDigite o nome do equipamento que você deseja adicionar a lista de \"FORA DE USO\" \n  \nPleno: ")
      retirar_do_estoque = "{}_disponiveis_dicionario.pop(\"{}\")".format(estoque, equipamento_selecionado)
      eval(retirar_do_estoque)
      fora_de_uso = "{}_fora_de_uso.append({})".format(estoque, equipamento_selecionado)
      motivo = input("\nQual é o motivo que o equipamento está sendo movido para list de \"FORA DE USO\" OBS: Informar a data \nPleno: ")
      if estoque == "notes":
        notes_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/notes_disponiveis_dicionario", 'w') as f:
          json.dump(notes_disponiveis_dicionario, f)
        with open("fora_de_uso/notes_fora_de_uso", 'w') as f:
          json.dump(notes_fora_de_uso, f)
        admin_menu()
      elif estoque == "x1_x2":
        x1_x2_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/x1_x2_disponiveis_dicionario", 'w') as f:
          json.dump(x1_x2_disponiveis_dicionario, f)
        with open("fora_de_uso/x1_x2_fora_de_uso", 'w') as f:
          json.dump(x1_x2_fora_de_uso, f)
        admin_menu()
      elif estoque == "tv28":
        tv28_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/tv28_disponiveis_dicionario", 'w') as f:
          json.dump(tv28_disponiveis_dicionario, f)
        with open("fora_de_uso/tv28_fora_de_uso", 'w') as f:
          json.dump(tv28_fora_de_uso, f)
        admin_menu()
      elif estoque == "controladora":
        controladora_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/controladora_disponiveis_dicionario", 'w') as f:
          json.dump(controladora_disponiveis_dicionario, f)
        with open("fora_de_uso/controladora_fora_de_uso", 'w') as f:
          json.dump(controladora_fora_de_uso, f)
        admin_menu()
      elif estoque == "led26":
        led26_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/led26_disponiveis_dicionario", 'w') as f:
          json.dump(led26_disponiveis_dicionario, f)
        with open("fora_de_uso/led26_fora_de_uso", 'w') as f:
          json.dump(led26_fora_de_uso, f)
        admin_menu()
      elif estoque == "led29":
        led29_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/led29_disponiveis_dicionario", 'w') as f:
          json.dump(led29_disponiveis_dicionario, f)
        with open("fora_de_uso/led29_fora_de_uso", 'w') as f:
          json.dump(led29_fora_de_uso, f)
        admin_menu()
      elif estoque == "led30":
        led30_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/led30_disponiveis_dicionario", 'w') as f:
          json.dump(led30_disponiveis_dicionario, f)
        with open("fora_de_uso/led30_fora_de_uso", 'w') as f:
          json.dump(led30_fora_de_uso, f)
        admin_menu()
      elif estoque == "led39":
        led39_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/led39_disponiveis_dicionario", 'w') as f:
          json.dump(led39_disponiveis_dicionario, f)
        with open("fora_de_uso/led39_fora_de_uso", 'w') as f:
          json.dump(led39_fora_de_uso, f)
        admin_menu()
      elif estoque == "tv22":
        tv22_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/tv22_disponiveis_dicionario", 'w') as f:
          json.dump(tv22_disponiveis_dicionario, f)
        with open("fora_de_uso/tv22_fora_de_uso", 'w') as f:
          json.dump(tv22_fora_de_uso, f)
        admin_menu()
      elif estoque == "tv32":
        tv32_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/tv32_disponiveis_dicionario", 'w') as f:
          json.dump(tv32_disponiveis_dicionario, f)
        with open("fora_de_uso/tv32_fora_de_uso", 'w') as f:
          json.dump(tv32_fora_de_uso, f)
        admin_menu()
      elif estoque == "tv42":
        tv42_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/tv42_disponiveis_dicionario", 'w') as f:
          json.dump(tv42_disponiveis_dicionario, f)
        with open("fora_de_uso/tv42_fora_de_uso", 'w') as f:
          json.dump(tv42_fora_de_uso, f)
        admin_menu()
      elif estoque == "tv43":
        tv43_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/tv43_disponiveis_dicionario", 'w') as f:
          json.dump(tv43_disponiveis_dicionario, f)
        with open("fora_de_uso/tv43_fora_de_uso", 'w') as f:
          json.dump(tv43_fora_de_uso, f)
        admin_menu()
      elif estoque == "tv46":
        tv46_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/tv46_disponiveis_dicionario", 'w') as f:
          json.dump(tv46_disponiveis_dicionario, f)
        with open("fora_de_uso/tv46_fora_de_uso", 'w') as f:
          json.dump(tv46_fora_de_uso, f)
        admin_menu()
      elif estoque == "tv49":
        tv49_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/tv49_disponiveis_dicionario", 'w') as f:
          json.dump(tv49_disponiveis_dicionario, f)
        with open("fora_de_uso/tv49_fora_de_uso", 'w') as f:
          json.dump(tv49_fora_de_uso, f)
        admin_menu()
      elif estoque == "tv55":
        tv55_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/tv55_disponiveis_dicionario", 'w') as f:
          json.dump(tv55_disponiveis_dicionario, f)
        with open("fora_de_uso/tv55_fora_de_uso", 'w') as f:
          json.dump(tv55_fora_de_uso, f)
        admin_menu()
      elif estoque == "tv65":
        tv65_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/tv65_disponiveis_dicionario", 'w') as f:
          json.dump(tv65_disponiveis_dicionario, f)
        with open("fora_de_uso/tv65_fora_de_uso", 'w') as f:
          json.dump(tv65_fora_de_uso, f)
        admin_menu()
      elif estoque == "tv72":
        tv72_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/tv72_disponiveis_dicionario", 'w') as f:
          json.dump(tv72_disponiveis_dicionario, f)
        with open("fora_de_uso/tv72_fora_de_uso", 'w') as f:
          json.dump(tv72_fora_de_uso, f)
        admin_menu()
      elif estoque == "tv75":
        tv75_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/tv75_disponiveis_dicionario", 'w') as f:
          json.dump(tv75_disponiveis_dicionario, f)
        with open("fora_de_uso/tv75_fora_de_uso", 'w') as f:
          json.dump(tv75_fora_de_uso, f)
        admin_menu()
      elif estoque == "tv84":
        tv84_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/tv84_disponiveis_dicionario", 'w') as f:
          json.dump(tv84_disponiveis_dicionario, f)
        with open("fora_de_uso/tv84_fora_de_uso", 'w') as f:
          json.dump(tv84_fora_de_uso, f)
        admin_menu()
      elif estoque == "vw47":
        vw47_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/vw47_disponiveis_dicionario", 'w') as f:
          json.dump(vw47_disponiveis_dicionario, f)
        with open("fora_de_uso/vw47_fora_de_uso", 'w') as f:
          json.dump(vw47_fora_de_uso, f)
        admin_menu()
      elif estoque == "vw55":
        vw55_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/vw55_disponiveis_dicionario", 'w') as f:
          json.dump(vw55_disponiveis_dicionario, f)
        with open("fora_de_uso/vw55_fora_de_uso", 'w') as f:
          json.dump(vw55_fora_de_uso, f)
        admin_menu()
      elif estoque == "distribuidor_hdmi":
        distribuidor_hdmi_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/distribuidor_hdmi_disponiveis_dicionario", 'w') as f:
          json.dump(distribuidor_hdmi_disponiveis_dicionario, f)
        with open("fora_de_uso/distribuidor_hdmi_fora_de_uso", 'w') as f:
          json.dump(distribuidor_hdmi_fora_de_uso, f)
        admin_menu()
      elif estoque == "analog_way":
        analog_way_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/analog_way_disponiveis_dicionario", 'w') as f:
          json.dump(analog_way_disponiveis_dicionario, f)
        with open("fora_de_uso/analog_way_fora_de_uso", 'w') as f:
          json.dump(analog_way_fora_de_uso, f)
        admin_menu()
      elif estoque == "video_wall_4k":
        video_wall_4k_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/video_wall_4k_disponiveis_dicionario", 'w') as f:
          json.dump(video_wall_4k_disponiveis_dicionario, f)
        with open("fora_de_uso/video_wall_4k_fora_de_uso", 'w') as f:
          json.dump(video_wall_4k_fora_de_uso, f)
        admin_menu()
      elif estoque == "mini_midia":
        mini_midia_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/mini_midia_disponiveis_dicionario", 'w') as f:
          json.dump(mini_midia_disponiveis_dicionario, f)
        with open("fora_de_uso/mini_midia_fora_de_uso", 'w') as f:
          json.dump(mini_midia_fora_de_uso, f)
        admin_menu()
      elif estoque == "teclado_e_mouse":
        teclado_e_mouse_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/teclado_e_mouse_disponiveis_dicionario", 'w') as f:
          json.dump(teclado_e_mouse_disponiveis_dicionario, f)
        with open("fora_de_uso/teclado_e_mouse_fora_de_uso", 'w') as f:
          json.dump(teclado_e_mouse_fora_de_uso, f)
        admin_menu()
      elif estoque == "triplo_had":
        triplo_had_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/triplo_had_disponiveis_dicionario", 'w') as f:
          json.dump(triplo_had_disponiveis_dicionario, f)
        with open("fora_de_uso/triplo_had_fora_de_uso", 'w') as f:
          json.dump(triplo_had_fora_de_uso, f)
        admin_menu()
      elif estoque == "placa_de_captura":
        placa_de_captura_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/placa_de_captura_disponiveis_dicionario", 'w') as f:
          json.dump(placa_de_captura_disponiveis_dicionario, f)
        with open("fora_de_uso/placa_de_captura_fora_de_uso", 'w') as f:
          json.dump(placa_de_captura_fora_de_uso, f)
        admin_menu()
      elif estoque == "cpu":
        cpu_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/cpu_disponiveis_dicionario", 'w') as f:
          json.dump(cpu_disponiveis_dicionario, f)
        with open("fora_de_uso/cpu_fora_de_uso", 'w') as f:
          json.dump(cpu_fora_de_uso, f)
        admin_menu()
      elif estoque == "mac":
        mac_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/mac_disponiveis_dicionario", 'w') as f:
          json.dump(mac_disponiveis_dicionario, f)
        with open("fora_de_uso/mac_fora_de_uso", 'w') as f:
          json.dump(mac_fora_de_uso, f)
        admin_menu()
      elif estoque == "ac800":
        ac800_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/ac800_disponiveis_dicionario", 'w') as f:
          json.dump(ac800_disponiveis_dicionario, f)
        with open("fora_de_uso/ac800_fora_de_uso", 'w') as f:
          json.dump(ac800_fora_de_uso, f)
        admin_menu()
      elif estoque == "caixa_de_som_pq":
        caixa_de_som_pq_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/caixa_de_som_pq_disponiveis_dicionario", 'w') as f:
          json.dump(caixa_de_som_pq_disponiveis_dicionario, f)
        with open("fora_de_uso/caixa_de_som_pq_fora_de_uso", 'w') as f:
          json.dump(caixa_de_som_pq_fora_de_uso, f)
        admin_menu()
      elif estoque == "caixa_de_som_g":
        caixa_de_som_g_fora_de_uso[equipamento_selecionado] = motivo
        with open("disponiveis/caixa_de_som_g_disponiveis_dicionario", 'w') as f:
          json.dump(caixa_de_som_g_disponiveis_dicionario, f)
        with open("fora_de_uso/caixa_de_som_g_fora_de_uso", 'w') as f:
          json.dump(caixa_de_som_g_fora_de_uso, f)
        admin_menu()
    else:
      print("ERROR")
      admin_menu()


    print("Equipamento movido para lista de \"FORA DE USO\"")
  elif escolha == "3":
      cls()
      print("Resumo estoque")
      # notebooks resumo
      notebooks_resumo = len(notes_evento_dicionario.keys()) + len(notes_disponiveis_dicionario.keys())
      print("\nTotal Notebooks: " + str(notebooks_resumo) + "\n        ↓ Ocorrências notebooks ↓ ")
      for key, value in notes_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências notebooks ↑ ")
      # notebooks resumo
      # controladora resumo
      controladora_resumo = len(controladora_evento_dicionario.keys()) + len(controladora_disponiveis_dicionario.keys())
      print("\nTotal controladora: " + str(controladora_resumo) + "\n        ↓ Ocorrências controladora ↓ ")
      for key, value in controladora_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências controladora ↑ ")
      # controladora resumo
      # led 2.6 resumo
      led26_resumo = len(led26_evento_dicionario.keys()) + len(led26_disponiveis_dicionario.keys())
      print("\nTotal led 2.6: " + str(led26_resumo) + "\n        ↓ Ocorrências led 2.6 ↓ ")
      for key, value in led26_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências led 2.6 ↑ ")
      # led 2.6 resumo
      # led 2.9 resumo
      led29_resumo = len(led29_evento_dicionario.keys()) + len(led29_disponiveis_dicionario.keys())
      print("\nTotal led 2.9: " + str(led29_resumo) + "\n        ↓ Ocorrências led 2.9 ↓ ")
      for key, value in led29_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências led 2.9 ↑ ")
      # led 2.9 resumo
      # led 3.0 resumo
      led30_resumo = len(led30_evento_dicionario.keys()) + len(led30_disponiveis_dicionario.keys())
      print("\nTotal led 3.0: " + str(led30_resumo) + "\n        ↓ Ocorrências led 3.0 ↓ ")
      for key, value in led30_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências led 3.0 ↑ ")
      # led 3.0 resumo
      # led 3.9 resumo
      led39_resumo = len(led39_evento_dicionario.keys()) + len(led39_disponiveis_dicionario.keys())
      print("\nTotal led 3.9: " + str(led39_resumo) + "\n        ↓ Ocorrências led 3.9 ↓ ")
      for key, value in led39_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências led 3.9 ↑ ")
      # led 3.9 resumo
      # tv22 resumo
      tv22_resumo = len(tv22_evento_dicionario.keys()) + len(tv22_disponiveis_dicionario.keys())
      print("\nTotal tv 22\": " + str(tv22_resumo) + "\n        ↓ Ocorrências tv 22\" ↓ ")
      for key, value in tv22_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências tv 22\" ↑ ")
      # tv22 resumo
      # tv28 resumo
      tv28_resumo = len(tv28_evento_dicionario.keys()) + len(tv28_disponiveis_dicionario.keys())
      print("\nTotal tv 28\": " + str(tv28_resumo) + "\n        ↓ Ocorrências tv 28\" ↓ ")
      for key, value in tv28_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências tv 28\" ↑ ")
      # tv28 resumo
      # tv32 resumo
      tv32_resumo = len(tv32_evento_dicionario.keys()) + len(tv32_disponiveis_dicionario.keys())
      print("\nTotal tv 32\": " + str(tv32_resumo) + "\n        ↓ Ocorrências tv 32\" ↓ ")
      for key, value in tv32_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências tv 32\" ↑ ")
      # tv32 resumo
      # tv42 resumo
      tv42_resumo = len(tv42_evento_dicionario.keys()) + len(tv42_disponiveis_dicionario.keys())
      print("\nTotal tv 42\": " + str(tv42_resumo) + "\n        ↓ Ocorrências tv 42\" ↓ ")
      for key, value in tv42_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências tv 42\" ↑ ")
      # tv42 resumo
      # tv43 resumo
      tv43_resumo = len(tv43_evento_dicionario.keys()) + len(tv43_disponiveis_dicionario.keys())
      print("\nTotal tv 43\": " + str(tv43_resumo) + "\n        ↓ Ocorrências tv 43\" ↓ ")
      for key, value in tv43_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências tv 43\" ↑ ")
      # tv43 resumo
      # tv46 resumo
      tv46_resumo = len(tv46_evento_dicionario.keys()) + len(tv46_disponiveis_dicionario.keys())
      print("\nTotal tv 46\": " + str(tv46_resumo) + "\n        ↓ Ocorrências tv 46\" ↓ ")
      for key, value in tv46_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências tv 46\" ↑ ")
      # tv46 resumo
      # tv49 resumo
      tv49_resumo = len(tv49_evento_dicionario.keys()) + len(tv49_disponiveis_dicionario.keys())
      print("\nTotal tv 49\": " + str(tv49_resumo) + "\n        ↓ Ocorrências tv 49\" ↓ ")
      for key, value in tv49_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências tv 49\" ↑ ")
      # tv49 resumo
      # tv55 resumo
      tv55_resumo = len(tv55_evento_dicionario.keys()) + len(tv55_disponiveis_dicionario.keys())
      print("\nTotal tv 55\": " + str(tv55_resumo) + "\n        ↓ Ocorrências tv 55\" ↓ ")
      for key, value in tv55_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências tv 55\" ↑ ")
      # tv55 resumo
      # tv65 resumo
      tv65_resumo = len(tv65_evento_dicionario.keys()) + len(tv65_disponiveis_dicionario.keys())
      print("\nTotal tv 65\": " + str(tv65_resumo) + "\n        ↓ Ocorrências tv 65\" ↓ ")
      for key, value in tv65_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências tv 65\" ↑ ")
      # tv65 resumo
      # tv72 resumo
      tv72_resumo = len(tv72_evento_dicionario.keys()) + len(tv72_disponiveis_dicionario.keys())
      print("\nTotal tv 72\": " + str(tv72_resumo) + "\n        ↓ Ocorrências tv 72\" ↓ ")
      for key, value in tv72_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências tv 72\" ↑ ")
      # tv72 resumo
      # tv75 resumo
      tv75_resumo = len(tv75_evento_dicionario.keys()) + len(tv75_disponiveis_dicionario.keys())
      print("\nTotal tv 75\": " + str(tv75_resumo) + "\n        ↓ Ocorrências tv 75\" ↓ ")
      for key, value in tv75_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências tv 75\" ↑ ")
      # tv75 resumo
      # tv84 resumo
      tv84_resumo = len(tv84_evento_dicionario.keys()) + len(tv84_disponiveis_dicionario.keys())
      print("\nTotal tv 84\": " + str(tv84_resumo) + "\n        ↓ Ocorrências tv 84\" ↓ ")
      for key, value in tv84_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências tv 84\" ↑ ")
      # tv84 resumo
      # vw47 resumo
      vw47_resumo = len(vw47_evento_dicionario.keys()) + len(vw47_disponiveis_dicionario.keys())
      print("\nTotal vw 47\": " + str(vw47_resumo) + "\n        ↓ Ocorrências vw 47\" ↓ ")
      for key, value in vw47_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências vw 47\" ↑ ")
      # vw47 resumo
      # vw55 resumo
      vw55_resumo = len(vw55_evento_dicionario.keys()) + len(vw55_disponiveis_dicionario.keys())
      print("\nTotal vw 55\": " + str(vw55_resumo) + "\n        ↓ Ocorrências vw 55\" ↓ ")
      for key, value in vw55_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências vw 55\" ↑ ")
      # vw55 resumo
      # x1_x2 resumo
      x1_x2_resumo = len(x1_x2_evento_dicionario.keys()) + len(x1_x2_disponiveis_dicionario.keys())
      print("\nTotal x1_x2: " + str(x1_x2_resumo) + "\n        ↓ Ocorrências x1_x2 ↓ ")
      for key, value in x1_x2_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências x1_x2 ↑ ")
      # x1_x2 resumo
      # distribuidor_hdmi resumo
      distribuidor_hdmi_resumo = len(distribuidor_hdmi_evento_dicionario.keys()) + len(distribuidor_hdmi_disponiveis_dicionario.keys())
      print("\nTotal distribuidor_hdmi: " + str(distribuidor_hdmi_resumo) + "\n        ↓ Ocorrências distribuidor_hdmi ↓ ")
      for key, value in distribuidor_hdmi_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências distribuidor_hdmi ↑ ")
      # distribuidor_hdmi resumo
      # analog_way resumo
      analog_way_resumo = len(analog_way_evento_dicionario.keys()) + len(analog_way_disponiveis_dicionario.keys())
      print("\nTotal analog_way: " + str(analog_way_resumo) + "\n        ↓ Ocorrências analog_way ↓ ")
      for key, value in analog_way_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências analog_way ↑ ")
      # analog_way resumo
      # video_wall_4k resumo
      video_wall_4k_resumo = len(video_wall_4k_evento_dicionario.keys()) + len(video_wall_4k_disponiveis_dicionario.keys())
      print("\nTotal video_wall_4k: " + str(video_wall_4k_resumo) + "\n        ↓ Ocorrências video_wall_4k ↓ ")
      for key, value in video_wall_4k_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências video_wall_4k ↑ ")
      # video_wall_4k resumo
      # mini_midia resumo
      mini_midia_resumo = len(mini_midia_evento_dicionario.keys()) + len(mini_midia_disponiveis_dicionario.keys())
      print("\nTotal mini_midia: " + str(mini_midia_resumo) + "\n        ↓ Ocorrências mini_midia ↓ ")
      for key, value in mini_midia_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências mini_midia ↑ ")
      # mini_midia resumo
      # teclado_e_mouse resumo
      teclado_e_mouse_resumo = len(teclado_e_mouse_evento_dicionario.keys()) + len(teclado_e_mouse_disponiveis_dicionario.keys())
      print("\nTotal teclado_e_mouse: " + str(teclado_e_mouse_resumo) + "\n        ↓ Ocorrências teclado_e_mouse ↓ ")
      for key, value in teclado_e_mouse_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências teclado_e_mouse ↑ ")
      # teclado_e_mouse resumo
      # triplo_had resumo
      triplo_had_resumo = len(triplo_had_evento_dicionario.keys()) + len(triplo_had_disponiveis_dicionario.keys())
      print("\nTotal triplo_had: " + str(triplo_had_resumo) + "\n        ↓ Ocorrências triplo_had ↓ ")
      for key, value in triplo_had_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências triplo_had ↑ ")
      # triplo_had resumo
      # placa_de_captura resumo
      placa_de_captura_resumo = len(placa_de_captura_evento_dicionario.keys()) + len(placa_de_captura_disponiveis_dicionario.keys())
      print("\nTotal placa_de_captura: " + str(placa_de_captura_resumo) + "\n        ↓ Ocorrências placa_de_captura ↓ ")
      for key, value in placa_de_captura_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências placa_de_captura ↑ ")
      # placa_de_captura resumo
      # cpu resumo
      cpu_resumo = len(cpu_evento_dicionario.keys()) + len(cpu_disponiveis_dicionario.keys())
      print("\nTotal cpu: " + str(cpu_resumo) + "\n        ↓ Ocorrências cpu ↓ ")
      for key, value in cpu_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências cpu ↑ ")
      # cpu resumo
      # mac resumo
      mac_resumo = len(mac_evento_dicionario.keys()) + len(mac_disponiveis_dicionario.keys())
      print("\nTotal mac: " + str(mac_resumo) + "\n        ↓ Ocorrências mac ↓ ")
      for key, value in mac_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências mac ↑ ")
      # mac resumo
      # ac800 resumo
      ac800_resumo = len(ac800_evento_dicionario.keys()) + len(ac800_disponiveis_dicionario.keys())
      print("\nTotal ac800: " + str(ac800_resumo) + "\n        ↓ Ocorrências ac800 ↓ ")
      for key, value in ac800_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências ac800 ↑ ")
      # ac800 resumo
      # caixa_de_som_pq resumo
      caixa_de_som_pq_resumo = len(caixa_de_som_pq_evento_dicionario.keys()) + len(caixa_de_som_pq_disponiveis_dicionario.keys())
      print("\nTotal caixa_de_som_pq: " + str(caixa_de_som_pq_resumo) + "\n        ↓ Ocorrências caixa_de_som_pq ↓ ")
      for key, value in caixa_de_som_pq_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências caixa_de_som_pq ↑ ")
      # caixa_de_som_pq resumo
      # caixa_de_som_g resumo
      caixa_de_som_g_resumo = len(caixa_de_som_g_evento_dicionario.keys()) + len(caixa_de_som_g_disponiveis_dicionario.keys())
      print("\nTotal caixa_de_som_g: " + str(caixa_de_som_g_resumo) + "\n        ↓ Ocorrências caixa_de_som_g ↓ ")
      for key, value in caixa_de_som_g_fora_de_uso.items():
          print(key, ': ', value)
      print("        ↑ Ocorrências caixa_de_som_g ↑ ")
      # caixa_de_som_g resumo
      admin_menu()
  elif escolha == "9":
        logs = open("logs.txt", "a+")
        logs.write("\nID: {} | foi desconnectado às {} |".format(id, datetime.now(tz)))
        logs.close()
        cls()
        print("Você foi desconectado com sucesso.")
        login()
  else:
    cls()
    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
    admin_menu()

### ↑ ADMIN MENU ↑ ###


### ↓ PRINT NOTES ↓ ###

def print_notes_disponiveis():
    print(colored("\n↓ Notebooks no estoque ↓", 'green'))
    for key, value in notes_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ Notebooks no estoque ↑", 'green'))
    print(colored('Total de notes em estoque: ' + str(len(notes_disponiveis_dicionario.keys())), 'green'))


def print_notes_evento():
    print(colored("\n↓ Notebooks em eventos ↓", 'red'))
    for key, value in notes_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ Notebooks em eventos ↑", 'red'))
    print(colored('Total de notes em eventos: ' + str(len(notes_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ Notebooks em FORA DE USO ↓", 'yellow'))
    for key, value in notes_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ Notebooks em FORA DE USO ↑", 'yellow'))
    print(colored('Total de notes em FORA DE USO: ' + str(len(notes_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT NOTES ↑ ###



### ↓ PRINT CONTROLADORA ↓ ###

def print_controladora_disponiveis():
    print(colored("\n↓ Controladoras no estoque ↓", 'green'))
    for key, value in controladora_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ Controladoras no estoque ↑", 'green'))
    print(colored('Total de Controladoras\" em estoque: ' + str(len(controladora_disponiveis_dicionario.keys())), 'green'))


def print_controladora_evento():
    print(colored("\n↓ Controladoras\" em eventos ↓", 'red'))
    for key, value in controladora_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ Controladoras em eventos ↑", 'red'))
    print(colored('Total de Controladoras\" em eventos: ' + str(len(controladora_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ controladoras em FORA DE USO ↓", 'yellow'))
    for key, value in controladora_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ controladoras em FORA DE USO ↑", 'yellow'))
    print(colored('Total de controladora em FORA DE USO: ' + str(len(controladora_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT CONTROLADORA ↑ ###


### ↓ PRINT analog_way ↓ ###

def print_analog_way_disponiveis():
    print(colored("\n↓ analog_way no estoque ↓", 'green'))
    for key, value in analog_way_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ analog_way no estoque ↑", 'green'))
    print(colored('Total de analog_way em estoque: ' + str(len(analog_way_disponiveis_dicionario.keys())), 'green'))


def print_analog_way_evento():
    print(colored("\n↓ analog_way em eventos ↓", 'red'))
    for key, value in analog_way_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ analog_way em eventos ↑", 'red'))
    print(colored('Total de analog_way em eventos: ' + str(len(analog_way_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ analog_way em FORA DE USO ↓", 'yellow'))
    for key, value in analog_way_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ analog_way em FORA DE USO ↑", 'yellow'))
    print(colored('Total de analog_way em FORA DE USO: ' + str(len(analog_way_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT analog_way ↑ ###


### ↓ PRINT video_wall_4k ↓ ###

def print_video_wall_4k_disponiveis():
    print(colored("\n↓ video_wall_4k no estoque ↓", 'green'))
    for key, value in video_wall_4k_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ video_wall_4k no estoque ↑", 'green'))
    print(colored('Total de video_wall_4k em estoque: ' + str(len(video_wall_4k_disponiveis_dicionario.keys())), 'green'))


def print_video_wall_4k_evento():
    print(colored("\n↓ video_wall_4k em eventos ↓", 'red'))
    for key, value in video_wall_4k_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ video_wall_4k em eventos ↑", 'red'))
    print(colored('Total de video_wall_4k em eventos: ' + str(len(video_wall_4k_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ video_wall_4k em FORA DE USO ↓", 'yellow'))
    for key, value in video_wall_4k_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ video_wall_4k em FORA DE USO ↑", 'yellow'))
    print(colored('Total de video_wall_4k em FORA DE USO: ' + str(len(video_wall_4k_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT video_wall_4k ↑ ###


### ↓ PRINT mini_midia ↓ ###

def print_mini_midia_disponiveis():
    print(colored("\n↓ mini_midia no estoque ↓", 'green'))
    for key, value in mini_midia_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ mini_midia no estoque ↑", 'green'))
    print(colored('Total de mini_midia em estoque: ' + str(len(mini_midia_disponiveis_dicionario.keys())), 'green'))


def print_mini_midia_evento():
    print(colored("\n↓ mini_midia em eventos ↓", 'red'))
    for key, value in mini_midia_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ mini_midia em eventos ↑", 'red'))
    print(colored('Total de mini_midia em eventos: ' + str(len(mini_midia_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ mini_midia em FORA DE USO ↓", 'yellow'))
    for key, value in mini_midia_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ mini_midia em FORA DE USO ↑", 'yellow'))
    print(colored('Total de mini_midia em FORA DE USO: ' + str(len(mini_midia_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT mini_midia ↑ ###


### ↓ PRINT teclado_e_mouse ↓ ###

def print_teclado_e_mouse_disponiveis():
    print(colored("\n↓ teclado_e_mouse no estoque ↓", 'green'))
    for key, value in teclado_e_mouse_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ teclado_e_mouse no estoque ↑", 'green'))
    print(colored('Total de teclado_e_mouse em estoque: ' + str(len(teclado_e_mouse_disponiveis_dicionario.keys())), 'green'))


def print_teclado_e_mouse_evento():
    print(colored("\n↓ teclado_e_mouse em eventos ↓", 'red'))
    for key, value in teclado_e_mouse_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ teclado_e_mouse em eventos ↑", 'red'))
    print(colored('Total de teclado_e_mouse em eventos: ' + str(len(teclado_e_mouse_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ teclado_e_mouse em FORA DE USO ↓", 'yellow'))
    for key, value in teclado_e_mouse_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ teclado_e_mouse em FORA DE USO ↑", 'yellow'))
    print(colored('Total de teclado_e_mouse em FORA DE USO: ' + str(len(teclado_e_mouse_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT teclado_e_mouse ↑ ###


### ↓ PRINT triplo_had ↓ ###

def print_triplo_had_disponiveis():
    print(colored("\n↓ triplo_had no estoque ↓", 'green'))
    for key, value in triplo_had_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ triplo_had no estoque ↑", 'green'))
    print(colored('Total de triplo_had em estoque: ' + str(len(triplo_had_disponiveis_dicionario.keys())), 'green'))


def print_triplo_had_evento():
    print(colored("\n↓ triplo_had em eventos ↓", 'red'))
    for key, value in triplo_had_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ triplo_had em eventos ↑", 'red'))
    print(colored('Total de triplo_had em eventos: ' + str(len(triplo_had_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ triplo_had em FORA DE USO ↓", 'yellow'))
    for key, value in triplo_had_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ triplo_had em FORA DE USO ↑", 'yellow'))
    print(colored('Total de triplo_had em FORA DE USO: ' + str(len(triplo_had_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT triplo_had ↑ ###


### ↓ PRINT placa_de_captura ↓ ###

def print_placa_de_captura_disponiveis():
    print(colored("\n↓ placa_de_captura no estoque ↓", 'green'))
    for key, value in placa_de_captura_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ placa_de_captura no estoque ↑", 'green'))
    print(colored('Total de placa_de_captura em estoque: ' + str(len(placa_de_captura_disponiveis_dicionario.keys())), 'green'))


def print_placa_de_captura_evento():
    print(colored("\n↓ placa_de_captura em eventos ↓", 'red'))
    for key, value in placa_de_captura_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ placa_de_captura em eventos ↑", 'red'))
    print(colored('Total de placa_de_captura em eventos: ' + str(len(placa_de_captura_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ placa_de_captura em FORA DE USO ↓", 'yellow'))
    for key, value in placa_de_captura_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ placa_de_captura em FORA DE USO ↑", 'yellow'))
    print(colored('Total de placa_de_captura em FORA DE USO: ' + str(len(placa_de_captura_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT placa_de_captura ↑ ###


### ↓ PRINT cpu ↓ ###

def print_cpu_disponiveis():
    print(colored("\n↓ cpu no estoque ↓", 'green'))
    for key, value in cpu_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ cpu no estoque ↑", 'green'))
    print(colored('Total de cpu em estoque: ' + str(len(cpu_disponiveis_dicionario.keys())), 'green'))


def print_cpu_evento():
    print(colored("\n↓ cpu em eventos ↓", 'red'))
    for key, value in cpu_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ cpu em eventos ↑", 'red'))
    print(colored('Total de cpu em eventos: ' + str(len(cpu_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ cpu em FORA DE USO ↓", 'yellow'))
    for key, value in cpu_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ cpu em FORA DE USO ↑", 'yellow'))
    print(colored('Total de cpu em FORA DE USO: ' + str(len(cpu_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT cpu ↑ ###


### ↓ PRINT mac ↓ ###

def print_mac_disponiveis():
    print(colored("\n↓ mac no estoque ↓", 'green'))
    for key, value in mac_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ mac no estoque ↑", 'green'))
    print(colored('Total de mac em estoque: ' + str(len(mac_disponiveis_dicionario.keys())), 'green'))


def print_mac_evento():
    print(colored("\n↓ mac em eventos ↓", 'red'))
    for key, value in mac_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ mac em eventos ↑", 'red'))
    print(colored('Total de mac em eventos: ' + str(len(mac_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ mac em FORA DE USO ↓", 'yellow'))
    for key, value in mac_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ mac em FORA DE USO ↑", 'yellow'))
    print(colored('Total de mac em FORA DE USO: ' + str(len(mac_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT mac ↑ ###


### ↓ PRINT distribuidor_hdmi ↓ ###

def print_distribuidor_hdmi_disponiveis():
    print(colored("\n↓ distribuidor_hdmi no estoque ↓", 'green'))
    for key, value in distribuidor_hdmi_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ distribuidor_hdmi no estoque ↑", 'green'))
    print(colored('Total de distribuidor_hdmi em estoque: ' + str(len(distribuidor_hdmi_disponiveis_dicionario.keys())), 'green'))


def print_distribuidor_hdmi_evento():
    print(colored("\n↓ distribuidor_hdmi em eventos ↓", 'red'))
    for key, value in distribuidor_hdmi_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ distribuidor_hdmi em eventos ↑", 'red'))
    print(colored('Total de distribuidor_hdmi em eventos: ' + str(len(distribuidor_hdmi_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ distribuidor_hdmi em FORA DE USO ↓", 'yellow'))
    for key, value in distribuidor_hdmi_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ distribuidor_hdmi em FORA DE USO ↑", 'yellow'))
    print(colored('Total de distribuidor_hdmi em FORA DE USO: ' + str(len(distribuidor_hdmi_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT distribuidor_hdmi ↑ ###


### ↓ PRINT ac800 ↓ ###

def print_ac800_disponiveis():
    print(colored("\n↓ ac800 no estoque ↓", 'green'))
    for key, value in ac800_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ ac800 no estoque ↑", 'green'))
    print(colored('Total de ac800 em estoque: ' + str(len(ac800_disponiveis_dicionario.keys())), 'green'))


def print_ac800_evento():
    print(colored("\n↓ ac800 em eventos ↓", 'red'))
    for key, value in ac800_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ ac800 em eventos ↑", 'red'))
    print(colored('Total de ac800 em eventos: ' + str(len(ac800_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ ac800 em FORA DE USO ↓", 'yellow'))
    for key, value in ac800_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ ac800 em FORA DE USO ↑", 'yellow'))
    print(colored('Total de ac800 em FORA DE USO: ' + str(len(ac800_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT ac800 ↑ ###


### ↓ PRINT caixa_de_som_g ↓ ###

def print_caixa_de_som_g_disponiveis():
    print(colored("\n↓ caixa_de_som_g no estoque ↓", 'green'))
    for key, value in caixa_de_som_g_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ caixa_de_som_g no estoque ↑", 'green'))
    print(colored('Total de caixa_de_som_g em estoque: ' + str(len(caixa_de_som_g_disponiveis_dicionario.keys())), 'green'))


def print_caixa_de_som_g_evento():
    print(colored("\n↓ caixa_de_som_g em eventos ↓", 'red'))
    for key, value in caixa_de_som_g_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ caixa_de_som_g em eventos ↑", 'red'))
    print(colored('Total de caixa_de_som_g em eventos: ' + str(len(caixa_de_som_g_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ caixa_de_som_g em FORA DE USO ↓", 'yellow'))
    for key, value in caixa_de_som_g_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ caixa_de_som_g em FORA DE USO ↑", 'yellow'))
    print(colored('Total de caixa_de_som_g em FORA DE USO: ' + str(len(caixa_de_som_g_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT caixa_de_som_g ↑ ###


### ↓ PRINT caixa_de_som_pq ↓ ###

def print_caixa_de_som_pq_disponiveis():
    print(colored("\n↓ caixa_de_som_pq no estoque ↓", 'green'))
    for key, value in caixa_de_som_pq_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ caixa_de_som_pq no estoque ↑", 'green'))
    print(colored('Total de caixa_de_som_pq em estoque: ' + str(len(caixa_de_som_pq_disponiveis_dicionario.keys())), 'green'))


def print_caixa_de_som_pq_evento():
    print(colored("\n↓ caixa_de_som_pq em eventos ↓", 'red'))
    for key, value in caixa_de_som_pq_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ caixa_de_som_pq em eventos ↑", 'red'))
    print(colored('Total de caixa_de_som_pq em eventos: ' + str(len(caixa_de_som_pq_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ caixa_de_som_pq em FORA DE USO ↓", 'yellow'))
    for key, value in caixa_de_som_pq_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ caixa_de_som_pq em FORA DE USO ↑", 'yellow'))
    print(colored('Total de caixa_de_som_pq em FORA DE USO: ' + str(len(caixa_de_som_pq_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT caixa_de_som_pq ↑ ###


### ↓ PRINT Distribuidor HDMI ↓ ###

def print_distribuidor_hdmi_disponiveis():
    print(colored("\n↓ Distribuidor HDMI no estoque ↓", 'green'))
    for key, value in distribuidor_hdmi_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ Distribuidor HDMI no estoque ↑", 'green'))
    print(colored('Total de Distribuidor HDMI\" em estoque: ' + str(len(distribuidor_hdmi_disponiveis_dicionario.keys())), 'green'))


def print_distribuidor_hdmi_evento():
    print(colored("\n↓ Distribuidor HDMI\" em eventos ↓", 'red'))
    for key, value in distribuidor_hdmi_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ Distribuidor HDMI em eventos ↑", 'red'))
    print(colored('Total de Distribuidor HDMI\" em eventos: ' + str(len(distribuidor_hdmi_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ distribuidor_hdmis em FORA DE USO ↓", 'yellow'))
    for key, value in distribuidor_hdmi_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ distribuidor_hdmis em FORA DE USO ↑", 'yellow'))
    print(colored('Total de distribuidor_hdmi em FORA DE USO: ' + str(len(distribuidor_hdmi_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT Distribuidor HDMI ↑ ###


### ↓ PRINT LED 3.9 ↓ ###

def print_led39_disponiveis():
    print(colored("\n↓ LED's 3.9\" no estoque ↓", 'green'))
    for key, value in led39_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ LED's 3.9\" no estoque ↑", 'green'))
    print(colored('Total de LED\'s 3.9\" em estoque: ' + str(len(led39_disponiveis_dicionario.keys())), 'green'))


def print_led39_evento():
    print(colored("\n↓ LED's 3.9\" em eventos ↓", 'red'))
    for key, value in led39_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ LED's 3.9\" em eventos ↑", 'red'))
    print(colored('Total de LED\'s 3.9\" em eventos: ' + str(len(led39_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ LED 3.9 em FORA DE USO ↓", 'yellow'))
    for key, value in led39_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ LED 3.9 em FORA DE USO ↑", 'yellow'))
    print(colored('Total de LED 3.9 em FORA DE USO: ' + str(len(led39_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT LED 3.9 ↑ ###


### ↓ PRINT LED 3.0 ↓ ###

def print_led30_disponiveis():
    print(colored("\n↓ LED's 3.0\" no estoque ↓", 'green'))
    for key, value in led30_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ LED's 3.0\" no estoque ↑", 'green'))
    print(colored('Total de LED\'s 3.0\" em estoque: ' + str(len(led30_disponiveis_dicionario.keys())), 'green'))


def print_led30_evento():
    print(colored("\n↓ LED's 3.0\" em eventos ↓", 'red'))
    for key, value in led30_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ LED's 3.0\" em eventos ↑", 'red'))
    print(colored('Total de LED\'s 3.0\" em eventos: ' + str(len(led30_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ LED 3.0 em FORA DE USO ↓", 'yellow'))
    for key, value in led30_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ LED 3.0 em FORA DE USO ↑", 'yellow'))
    print(colored('Total de LED 3.0 em FORA DE USO: ' + str(len(led30_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT LED 3.0 ↑ ###


### ↓ PRINT LED 2.9 ↓ ###

def print_led29_disponiveis():
    print(colored("\n↓ LED's 2.9\" no estoque ↓", 'green'))
    for key, value in led29_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ LED's 2.9\" no estoque ↑", 'green'))
    print(colored('Total de LED\'s 2.9\" em estoque: ' + str(len(led29_disponiveis_dicionario.keys())), 'green'))


def print_led29_evento():
    print(colored("\n↓ LED's 2.9\" em eventos ↓", 'red'))
    for key, value in led29_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ LED's 2.9\" em eventos ↑", 'red'))
    print(colored('Total de LED\'s 2.9\" em eventos: ' + str(len(led29_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ LED 2.9 em FORA DE USO ↓", 'yellow'))
    for key, value in led29_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ LED 2.9 em FORA DE USO ↑", 'yellow'))
    print(colored('Total de LED 2.9 em FORA DE USO: ' + str(len(led29_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT LED 2.9 ↑ ###


### ↓ PRINT LED 2.6 ↓ ###

def print_led26_disponiveis():
    print(colored("\n↓ LED's 2.6\" no estoque ↓", 'green'))
    for key, value in led26_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ LED's 2.6\" no estoque ↑", 'green'))
    print(colored('Total de LED\'s 2.6\" em estoque: ' + str(len(led26_disponiveis_dicionario.keys())), 'green'))


def print_led26_evento():
    print(colored("\n↓ LED's 2.6\" em eventos ↓", 'red'))
    for key, value in led26_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ LED's 2.6\" em eventos ↑", 'red'))
    print(colored('Total de LED\'s 2.6\" em eventos: ' + str(len(led26_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ LED 2.6 em FORA DE USO ↓", 'yellow'))
    for key, value in led26_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ LED 2.6 em FORA DE USO ↑", 'yellow'))
    print(colored('Total de LED 2.6 em FORA DE USO: ' + str(len(led26_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT LED 2.6 ↑ ###



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
    print(colored("\n↓ TV 42\" em FORA DE USO ↓", 'yellow'))
    for key, value in tv42_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ TV 42\" em FORA DE USO ↑", 'yellow'))
    print(colored('Total de TV 42\" em FORA DE USO: ' + str(len(tv42_fora_de_uso.keys())), 'yellow'))


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
    print(colored("\n↓ TV 22\" em FORA DE USO ↓", 'yellow'))
    for key, value in tv22_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ TV 22\" em FORA DE USO ↑", 'yellow'))
    print(colored('Total de TV 22\" em FORA DE USO: ' + str(len(tv22_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT TV22 ↑ ###


### ↓ PRINT X1/X2 ↓ ###

def print_x1_x2_disponiveis():
    print(colored("\n↓ TV's 22\" no estoque ↓", 'green'))
    for key, value in x1_x2_disponiveis_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 22\" no estoque ↑", 'green'))
    print(colored('Total de TV\'s 22\" em estoque: ' + str(len(x1_x2_disponiveis_dicionario.keys())), 'green'))


def print_x1_x2_evento():
    print(colored("\n↓ TV's 22\" em eventos ↓", 'red'))
    for key, value in x1_x2_evento_dicionario.items():
        print(key, ': ', value)
    print(colored("↑ TV's 22\" em eventos ↑", 'red'))
    print(colored('Total de TV\'s 22\" em eventos: ' + str(len(x1_x2_evento_dicionario.keys())), 'red'))
    print(colored("\n↓ TV 22\" em FORA DE USO ↓", 'yellow'))
    for key, value in x1_x2_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ TV 22\" em FORA DE USO ↑", 'yellow'))
    print(colored('Total de TV 22\" em FORA DE USO: ' + str(len(x1_x2_fora_de_uso.keys())), 'yellow'))


### ↑ PRINT X1/X2 ↑ ###


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
    print(colored("\n↓ TV 28\" em FORA DE USO ↓", 'yellow'))
    for key, value in tv28_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ TV 28\" em FORA DE USO ↑", 'yellow'))
    print(colored('Total de TV 28\" em FORA DE USO: ' + str(len(tv28_fora_de_uso.keys())), 'yellow'))


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
    print(colored("\n↓ TV 32\" em FORA DE USO ↓", 'yellow'))
    for key, value in tv32_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ TV 32\" em FORA DE USO ↑", 'yellow'))
    print(colored('Total de TV 32\" em FORA DE USO: ' + str(len(tv32_fora_de_uso.keys())), 'yellow'))


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
    print(colored("\n↓ TV 43\" em FORA DE USO ↓", 'yellow'))
    for key, value in tv43_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ TV 43\" em FORA DE USO ↑", 'yellow'))
    print(colored('Total de TV 43\" em FORA DE USO: ' + str(len(tv43_fora_de_uso.keys())), 'yellow'))


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
    print(colored("\n↓ TV 46\" em FORA DE USO ↓", 'yellow'))
    for key, value in tv46_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ TV 46\" em FORA DE USO ↑", 'yellow'))
    print(colored('Total de TV 46\" em FORA DE USO: ' + str(len(tv46_fora_de_uso.keys())), 'yellow'))


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
    print(colored("\n↓ TV 49\" em FORA DE USO ↓", 'yellow'))
    for key, value in tv49_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ TV 49\" em FORA DE USO ↑", 'yellow'))
    print(colored('Total de TV 49\" em FORA DE USO: ' + str(len(tv49_fora_de_uso.keys())), 'yellow'))


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
    print(colored("\n↓ TV 55\" em FORA DE USO ↓", 'yellow'))
    for key, value in tv55_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ TV 55\" em FORA DE USO ↑", 'yellow'))
    print(colored('Total de TV 55\" em FORA DE USO: ' + str(len(tv55_fora_de_uso.keys())), 'yellow'))


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
    print(colored("\n↓ TV 65\" em FORA DE USO ↓", 'yellow'))
    for key, value in tv65_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ TV 65\" em FORA DE USO ↑", 'yellow'))
    print(colored('Total de TV 65\" em FORA DE USO: ' + str(len(tv65_fora_de_uso.keys())), 'yellow'))


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
    print(colored("\n↓ TV 72\" em FORA DE USO ↓", 'yellow'))
    for key, value in tv72_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ TV 72\" em FORA DE USO ↑", 'yellow'))
    print(colored('Total de TV 72\" em FORA DE USO: ' + str(len(tv72_fora_de_uso.keys())), 'yellow'))


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
    print(colored("\n↓ TV 75\" em FORA DE USO ↓", 'yellow'))
    for key, value in tv75_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ TV 75\" em FORA DE USO ↑", 'yellow'))
    print(colored('Total de TV 75\" em FORA DE USO: ' + str(len(tv75_fora_de_uso.keys())), 'yellow'))


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
    print(colored("\n↓ TV 84\" em FORA DE USO ↓", 'yellow'))
    for key, value in tv84_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ TV 84\" em FORA DE USO ↑", 'yellow'))
    print(colored('Total de TV 84\" em FORA DE USO: ' + str(len(tv84_fora_de_uso.keys())), 'yellow'))


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
    print(colored("\n↓ vw 47\" em FORA DE USO ↓", 'yellow'))
    for key, value in vw47_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ vw 47\" em FORA DE USO ↑", 'yellow'))
    print(colored('Total de vw 47\" em FORA DE USO: ' + str(len(vw47_fora_de_uso.keys())), 'yellow'))


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
    print(colored("\n↓ vw 55\" em FORA DE USO ↓", 'yellow'))
    for key, value in vw55_fora_de_uso.items():
        print(key, ': ', value)
    print(colored("↑ vw 55\" em FORA DE USO ↑", 'yellow'))
    print(colored('Total de vw 55\" em FORA DE USO: ' + str(len(vw55_fora_de_uso.keys())), 'yellow'))

### ↑ PRINT vw55 ↑ ###


### Menu Principal ###

def menu():
    escolha = input(
        '\nQual estoque você gostaria de acessar, escolha o número da ação:\n \n[1] Notebooks \n[2] TV\'s \n[3] Leds \n[4] Controladoras \n[5] X1/X2 \n[6] Distribuidor HDMI \n[7] Analog Way \n[8] Video Wall 4k \n[10] Mini Midia \n[11] Teclado e Mouse \n[12] Triplo Had \n[13] Placa de Captura \n[14] CPU \n[15] MAC \n[16] AC 800 \n[17] Caixa de som pq \n[18] Caixa de som g \n[9] Sair \nPleno:')
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
        cls()
        modelo_led = input("Qual LED você gostaria?\n  \n[1] LED 2.6 \n[2] LED 2.9 \n[3] LED 3.0 \n[4] LED 3.9 \nPleno: ")
        if modelo_led == "1":
            print("\nRedirecionado para o estoque de LED\'s 2.6\".")
            led26()
        elif modelo_led == "2":
            print("\nRedirecionado para o estoque de LED\'s 2.9\".")
            led29()
        elif modelo_led == "3":
            print("\nRedirecionado para o estoque de LED\'s 3.0\".")
            led30()
        elif modelo_led == "4":
            print("\nRedirecionado para o estoque de LED\'s 3.9\".")
            led39()
        else:
            print(colored("ERROR: Opção inválida.", 'yellow'))
            menu()
    elif escolha == "4":
        print("\nRedirecionado para o estoque de Controladora.")
        controladora()
    elif escolha == "5":
      print("\nRedirecionado para o estoque de X1/X2.")
      x1_x2()
    elif escolha == "6":
        print("\nRedirecionado para o estoque de Distribuidor HDMI.")
        distribuidor_hdmi()
    elif escolha == "7":
        print("\nRedirecionado para o estoque de Analog Way.")
        analog_way()
    elif escolha == "8":
        print("\nRedirecionado para o estoque de Video wall 4k.")
        video_wall_4k()
    elif escolha == "10":
        print("\nRedirecionado para o estoque de Mini Midia.")
        mini_midia()
    elif escolha == "11":
        print("\nRedirecionado para o estoque de Teclado e Mouse.")
        teclado_e_mouse()
    elif escolha == "12":
        print("\nRedirecionado para o estoque de Triplo Had.")
        triplo_had()
    elif escolha == "13":
        print("\nRedirecionado para o estoque de Placa de Captura.")
        placa_de_captura()
    elif escolha == "14":
        print("\nRedirecionado para o estoque de CPU.")
        cpu()
    elif escolha == "15":
        print("\nRedirecionado para o estoque de Mac.")
        mac()
    elif escolha == "16":
        print("\nRedirecionado para o estoque de AC 800.")
        ac800()
    elif escolha == "17":
        print("\nRedirecionado para o estoque de Caixa de som pq.")
        caixa_de_som_pq()
    elif escolha == "18":
        print("\nRedirecionado para o estoque de Caixa de som g.")
        caixa_de_som_g()
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


### ↓ Escolhas X1 - X2 ↓ ###
def x1_x2():
    escolha = input(
        '\nX1 - X2: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_x1_x2()
    elif escolha == "2":
        retorno_x1_x2()

    elif escolha == "3":
        cls()
        print_x1_x2_disponiveis()
        print_x1_x2_evento()
        x1_x2()

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
        x1_x2()


### ↑ Escolhas X1 - X2 ↑ ###
### ↓ Funções X1 - X2 ↓ ###

def retirar_x1_x2():
    cls()
    print_x1_x2_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_x1_x2:
        note_selecionado = codigo_de_barras_x1_x2.get(codigo_escaneado)
        if note_selecionado in x1_x2_disponiveis_dicionario:
            x1_x2_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou X1 - X2\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            x1_x2_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/x1_x2_disponiveis_dicionario", 'w') as f:
                json.dump(x1_x2_disponiveis_dicionario, f)
            with open("eventos/x1_x2_evento_dicionario", 'w') as f:
                json.dump(x1_x2_evento_dicionario, f)
            cls()
            print_x1_x2_disponiveis()
            print_x1_x2_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra X1 - X2\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_x1_x2_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_x1_x2:
                        note_selecionado = codigo_de_barras_x1_x2.get(codigo_escaneado)
                        if note_selecionado in x1_x2_disponiveis_dicionario:
                            x1_x2_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou X1 - X2\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            x1_x2_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/x1_x2_disponiveis_dicionario", 'w') as f:
                                json.dump(x1_x2_disponiveis_dicionario, f)
                            with open("eventos/x1_x2_evento_dicionario", 'w') as f:
                                json.dump(x1_x2_evento_dicionario, f)
                            cls()
                            print_x1_x2_disponiveis()
                            print_x1_x2_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_x1_x2()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    x1_x2()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            x1_x2()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        x1_x2()


def retorno_x1_x2():
    cls()
    print_x1_x2_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_x1_x2:
        note_selecionado = codigo_de_barras_x1_x2.get(codigo_escaneado)
        if note_selecionado in x1_x2_evento_dicionario:
            x1_x2_evento_dicionario.pop(note_selecionado)
            x1_x2_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/x1_x2_evento_dicionario", 'w') as f:
                json.dump(x1_x2_evento_dicionario, f)
            with open("disponiveis/x1_x2_disponiveis_dicionario", 'w') as f:
                json.dump(x1_x2_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou X1 - X2\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_x1_x2_disponiveis()
            print_x1_x2_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra X1 - X2\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_x1_x2()
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
            x1_x2()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        x1_x2()


### ↑ Funções X1 - X2 ↑ ###


### ↓ Escolhas Controladora ↓ ###
def controladora():
    escolha = input(
        '\nControladora: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_controladora()
    elif escolha == "2":
        retorno_controladora()

    elif escolha == "3":
        cls()
        print_controladora_disponiveis()
        print_controladora_evento()
        controladora()

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
        controladora()


### ↑ Escolhas Controladora ↑ ###
### ↓ Funções Controladora ↓ ###

def retirar_controladora():
    cls()
    print_controladora_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_controladora:
        note_selecionado = codigo_de_barras_controladora.get(codigo_escaneado)
        if note_selecionado in controladora_disponiveis_dicionario:
            controladora_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou Controladora\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            controladora_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/controladora_disponiveis_dicionario", 'w') as f:
                json.dump(controladora_disponiveis_dicionario, f)
            with open("eventos/controladora_evento_dicionario", 'w') as f:
                json.dump(controladora_evento_dicionario, f)
            cls()
            print_controladora_disponiveis()
            print_controladora_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra Controladora\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_controladora_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_controladora:
                        note_selecionado = codigo_de_barras_controladora.get(codigo_escaneado)
                        if note_selecionado in controladora_disponiveis_dicionario:
                            controladora_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou Controladora\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            controladora_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/controladora_disponiveis_dicionario", 'w') as f:
                                json.dump(controladora_disponiveis_dicionario, f)
                            with open("eventos/controladora_evento_dicionario", 'w') as f:
                                json.dump(controladora_evento_dicionario, f)
                            cls()
                            print_controladora_disponiveis()
                            print_controladora_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_controladora()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    controladora()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            controladora()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        controladora()


def retorno_controladora():
    cls()
    print_controladora_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_controladora:
        note_selecionado = codigo_de_barras_controladora.get(codigo_escaneado)
        if note_selecionado in controladora_evento_dicionario:
            controladora_evento_dicionario.pop(note_selecionado)
            controladora_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/controladora_evento_dicionario", 'w') as f:
                json.dump(controladora_evento_dicionario, f)
            with open("disponiveis/controladora_disponiveis_dicionario", 'w') as f:
                json.dump(controladora_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou Controladora\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_controladora_disponiveis()
            print_controladora_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra Controladora\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_controladora()
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
            controladora()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        controladora()


### ↑ Funções Controladora ↑ ###


### ↓ Escolhas mini_midia ↓ ###
def mini_midia():
    escolha = input(
        '\nmini_midia: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_mini_midia()
    elif escolha == "2":
        retorno_mini_midia()

    elif escolha == "3":
        cls()
        print_mini_midia_disponiveis()
        print_mini_midia_evento()
        mini_midia()

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
        mini_midia()


### ↑ Escolhas mini_midia ↑ ###
### ↓ Funções mini_midia ↓ ###

def retirar_mini_midia():
    cls()
    print_mini_midia_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_mini_midia:
        note_selecionado = codigo_de_barras_mini_midia.get(codigo_escaneado)
        if note_selecionado in mini_midia_disponiveis_dicionario:
            mini_midia_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou mini_midia\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            mini_midia_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/mini_midia_disponiveis_dicionario", 'w') as f:
                json.dump(mini_midia_disponiveis_dicionario, f)
            with open("eventos/mini_midia_evento_dicionario", 'w') as f:
                json.dump(mini_midia_evento_dicionario, f)
            cls()
            print_mini_midia_disponiveis()
            print_mini_midia_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra mini_midia\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_mini_midia_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_mini_midia:
                        note_selecionado = codigo_de_barras_mini_midia.get(codigo_escaneado)
                        if note_selecionado in mini_midia_disponiveis_dicionario:
                            mini_midia_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou mini_midia\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            mini_midia_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/mini_midia_disponiveis_dicionario", 'w') as f:
                                json.dump(mini_midia_disponiveis_dicionario, f)
                            with open("eventos/mini_midia_evento_dicionario", 'w') as f:
                                json.dump(mini_midia_evento_dicionario, f)
                            cls()
                            print_mini_midia_disponiveis()
                            print_mini_midia_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_mini_midia()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    mini_midia()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            mini_midia()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        mini_midia()


def retorno_mini_midia():
    cls()
    print_mini_midia_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_mini_midia:
        note_selecionado = codigo_de_barras_mini_midia.get(codigo_escaneado)
        if note_selecionado in mini_midia_evento_dicionario:
            mini_midia_evento_dicionario.pop(note_selecionado)
            mini_midia_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/mini_midia_evento_dicionario", 'w') as f:
                json.dump(mini_midia_evento_dicionario, f)
            with open("disponiveis/mini_midia_disponiveis_dicionario", 'w') as f:
                json.dump(mini_midia_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou mini_midia\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_mini_midia_disponiveis()
            print_mini_midia_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra mini_midia\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_mini_midia()
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
            mini_midia()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        mini_midia()


### ↑ Funções mini_midia ↑ ###


### ↓ Escolhas teclado_e_mouse ↓ ###
def teclado_e_mouse():
    escolha = input(
        '\nteclado_e_mouse: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_teclado_e_mouse()
    elif escolha == "2":
        retorno_teclado_e_mouse()

    elif escolha == "3":
        cls()
        print_teclado_e_mouse_disponiveis()
        print_teclado_e_mouse_evento()
        teclado_e_mouse()

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
        teclado_e_mouse()


### ↑ Escolhas teclado_e_mouse ↑ ###
### ↓ Funções teclado_e_mouse ↓ ###

def retirar_teclado_e_mouse():
    cls()
    print_teclado_e_mouse_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_teclado_e_mouse:
        note_selecionado = codigo_de_barras_teclado_e_mouse.get(codigo_escaneado)
        if note_selecionado in teclado_e_mouse_disponiveis_dicionario:
            teclado_e_mouse_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou teclado_e_mouse\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            teclado_e_mouse_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/teclado_e_mouse_disponiveis_dicionario", 'w') as f:
                json.dump(teclado_e_mouse_disponiveis_dicionario, f)
            with open("eventos/teclado_e_mouse_evento_dicionario", 'w') as f:
                json.dump(teclado_e_mouse_evento_dicionario, f)
            cls()
            print_teclado_e_mouse_disponiveis()
            print_teclado_e_mouse_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra teclado_e_mouse\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_teclado_e_mouse_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_teclado_e_mouse:
                        note_selecionado = codigo_de_barras_teclado_e_mouse.get(codigo_escaneado)
                        if note_selecionado in teclado_e_mouse_disponiveis_dicionario:
                            teclado_e_mouse_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou teclado_e_mouse\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            teclado_e_mouse_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/teclado_e_mouse_disponiveis_dicionario", 'w') as f:
                                json.dump(teclado_e_mouse_disponiveis_dicionario, f)
                            with open("eventos/teclado_e_mouse_evento_dicionario", 'w') as f:
                                json.dump(teclado_e_mouse_evento_dicionario, f)
                            cls()
                            print_teclado_e_mouse_disponiveis()
                            print_teclado_e_mouse_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_teclado_e_mouse()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    teclado_e_mouse()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            teclado_e_mouse()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        teclado_e_mouse()


def retorno_teclado_e_mouse():
    cls()
    print_teclado_e_mouse_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_teclado_e_mouse:
        note_selecionado = codigo_de_barras_teclado_e_mouse.get(codigo_escaneado)
        if note_selecionado in teclado_e_mouse_evento_dicionario:
            teclado_e_mouse_evento_dicionario.pop(note_selecionado)
            teclado_e_mouse_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/teclado_e_mouse_evento_dicionario", 'w') as f:
                json.dump(teclado_e_mouse_evento_dicionario, f)
            with open("disponiveis/teclado_e_mouse_disponiveis_dicionario", 'w') as f:
                json.dump(teclado_e_mouse_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou teclado_e_mouse\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_teclado_e_mouse_disponiveis()
            print_teclado_e_mouse_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra teclado_e_mouse\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_teclado_e_mouse()
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
            teclado_e_mouse()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        teclado_e_mouse()


### ↑ Funções teclado_e_mouse ↑ ###


### ↓ Escolhas triplo_had ↓ ###
def triplo_had():
    escolha = input(
        '\ntriplo_had: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_triplo_had()
    elif escolha == "2":
        retorno_triplo_had()

    elif escolha == "3":
        cls()
        print_triplo_had_disponiveis()
        print_triplo_had_evento()
        triplo_had()

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
        triplo_had()


### ↑ Escolhas triplo_had ↑ ###
### ↓ Funções triplo_had ↓ ###

def retirar_triplo_had():
    cls()
    print_triplo_had_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_triplo_had:
        note_selecionado = codigo_de_barras_triplo_had.get(codigo_escaneado)
        if note_selecionado in triplo_had_disponiveis_dicionario:
            triplo_had_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou triplo_had\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            triplo_had_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/triplo_had_disponiveis_dicionario", 'w') as f:
                json.dump(triplo_had_disponiveis_dicionario, f)
            with open("eventos/triplo_had_evento_dicionario", 'w') as f:
                json.dump(triplo_had_evento_dicionario, f)
            cls()
            print_triplo_had_disponiveis()
            print_triplo_had_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra triplo_had\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_triplo_had_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_triplo_had:
                        note_selecionado = codigo_de_barras_triplo_had.get(codigo_escaneado)
                        if note_selecionado in triplo_had_disponiveis_dicionario:
                            triplo_had_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou triplo_had\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            triplo_had_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/triplo_had_disponiveis_dicionario", 'w') as f:
                                json.dump(triplo_had_disponiveis_dicionario, f)
                            with open("eventos/triplo_had_evento_dicionario", 'w') as f:
                                json.dump(triplo_had_evento_dicionario, f)
                            cls()
                            print_triplo_had_disponiveis()
                            print_triplo_had_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_triplo_had()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    triplo_had()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            triplo_had()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        triplo_had()


def retorno_triplo_had():
    cls()
    print_triplo_had_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_triplo_had:
        note_selecionado = codigo_de_barras_triplo_had.get(codigo_escaneado)
        if note_selecionado in triplo_had_evento_dicionario:
            triplo_had_evento_dicionario.pop(note_selecionado)
            triplo_had_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/triplo_had_evento_dicionario", 'w') as f:
                json.dump(triplo_had_evento_dicionario, f)
            with open("disponiveis/triplo_had_disponiveis_dicionario", 'w') as f:
                json.dump(triplo_had_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou triplo_had\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_triplo_had_disponiveis()
            print_triplo_had_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra triplo_had\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_triplo_had()
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
            triplo_had()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        triplo_had()


### ↑ Funções triplo_had ↑ ###


### ↓ Escolhas placa_de_captura ↓ ###
def placa_de_captura():
    escolha = input(
        '\nplaca_de_captura: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_placa_de_captura()
    elif escolha == "2":
        retorno_placa_de_captura()

    elif escolha == "3":
        cls()
        print_placa_de_captura_disponiveis()
        print_placa_de_captura_evento()
        placa_de_captura()

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
        placa_de_captura()


### ↑ Escolhas placa_de_captura ↑ ###
### ↓ Funções placa_de_captura ↓ ###

def retirar_placa_de_captura():
    cls()
    print_placa_de_captura_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_placa_de_captura:
        note_selecionado = codigo_de_barras_placa_de_captura.get(codigo_escaneado)
        if note_selecionado in placa_de_captura_disponiveis_dicionario:
            placa_de_captura_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou placa_de_captura\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            placa_de_captura_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/placa_de_captura_disponiveis_dicionario", 'w') as f:
                json.dump(placa_de_captura_disponiveis_dicionario, f)
            with open("eventos/placa_de_captura_evento_dicionario", 'w') as f:
                json.dump(placa_de_captura_evento_dicionario, f)
            cls()
            print_placa_de_captura_disponiveis()
            print_placa_de_captura_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra placa_de_captura\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_placa_de_captura_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_placa_de_captura:
                        note_selecionado = codigo_de_barras_placa_de_captura.get(codigo_escaneado)
                        if note_selecionado in placa_de_captura_disponiveis_dicionario:
                            placa_de_captura_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou placa_de_captura\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            placa_de_captura_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/placa_de_captura_disponiveis_dicionario", 'w') as f:
                                json.dump(placa_de_captura_disponiveis_dicionario, f)
                            with open("eventos/placa_de_captura_evento_dicionario", 'w') as f:
                                json.dump(placa_de_captura_evento_dicionario, f)
                            cls()
                            print_placa_de_captura_disponiveis()
                            print_placa_de_captura_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_placa_de_captura()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    placa_de_captura()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            placa_de_captura()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        placa_de_captura()


def retorno_placa_de_captura():
    cls()
    print_placa_de_captura_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_placa_de_captura:
        note_selecionado = codigo_de_barras_placa_de_captura.get(codigo_escaneado)
        if note_selecionado in placa_de_captura_evento_dicionario:
            placa_de_captura_evento_dicionario.pop(note_selecionado)
            placa_de_captura_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/placa_de_captura_evento_dicionario", 'w') as f:
                json.dump(placa_de_captura_evento_dicionario, f)
            with open("disponiveis/placa_de_captura_disponiveis_dicionario", 'w') as f:
                json.dump(placa_de_captura_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou placa_de_captura\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_placa_de_captura_disponiveis()
            print_placa_de_captura_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra placa_de_captura\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_placa_de_captura()
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
            placa_de_captura()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        placa_de_captura()


### ↑ Funções placa_de_captura ↑ ###


### ↓ Escolhas cpu ↓ ###
def cpu():
    escolha = input(
        '\ncpu: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_cpu()
    elif escolha == "2":
        retorno_cpu()

    elif escolha == "3":
        cls()
        print_cpu_disponiveis()
        print_cpu_evento()
        cpu()

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
        cpu()


### ↑ Escolhas cpu ↑ ###
### ↓ Funções cpu ↓ ###

def retirar_cpu():
    cls()
    print_cpu_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_cpu:
        note_selecionado = codigo_de_barras_cpu.get(codigo_escaneado)
        if note_selecionado in cpu_disponiveis_dicionario:
            cpu_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou cpu\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            cpu_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/cpu_disponiveis_dicionario", 'w') as f:
                json.dump(cpu_disponiveis_dicionario, f)
            with open("eventos/cpu_evento_dicionario", 'w') as f:
                json.dump(cpu_evento_dicionario, f)
            cls()
            print_cpu_disponiveis()
            print_cpu_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra cpu\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_cpu_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_cpu:
                        note_selecionado = codigo_de_barras_cpu.get(codigo_escaneado)
                        if note_selecionado in cpu_disponiveis_dicionario:
                            cpu_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou cpu\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            cpu_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/cpu_disponiveis_dicionario", 'w') as f:
                                json.dump(cpu_disponiveis_dicionario, f)
                            with open("eventos/cpu_evento_dicionario", 'w') as f:
                                json.dump(cpu_evento_dicionario, f)
                            cls()
                            print_cpu_disponiveis()
                            print_cpu_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_cpu()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    cpu()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            cpu()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        cpu()


def retorno_cpu():
    cls()
    print_cpu_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_cpu:
        note_selecionado = codigo_de_barras_cpu.get(codigo_escaneado)
        if note_selecionado in cpu_evento_dicionario:
            cpu_evento_dicionario.pop(note_selecionado)
            cpu_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/cpu_evento_dicionario", 'w') as f:
                json.dump(cpu_evento_dicionario, f)
            with open("disponiveis/cpu_disponiveis_dicionario", 'w') as f:
                json.dump(cpu_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou cpu\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_cpu_disponiveis()
            print_cpu_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra cpu\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_cpu()
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
            cpu()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        cpu()


### ↑ Funções cpu ↑ ###


### ↓ Escolhas mac ↓ ###
def mac():
    escolha = input(
        '\nmac: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_mac()
    elif escolha == "2":
        retorno_mac()

    elif escolha == "3":
        cls()
        print_mac_disponiveis()
        print_mac_evento()
        mac()

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
        mac()


### ↑ Escolhas mac ↑ ###
### ↓ Funções mac ↓ ###

def retirar_mac():
    cls()
    print_mac_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_mac:
        note_selecionado = codigo_de_barras_mac.get(codigo_escaneado)
        if note_selecionado in mac_disponiveis_dicionario:
            mac_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou mac\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            mac_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/mac_disponiveis_dicionario", 'w') as f:
                json.dump(mac_disponiveis_dicionario, f)
            with open("eventos/mac_evento_dicionario", 'w') as f:
                json.dump(mac_evento_dicionario, f)
            cls()
            print_mac_disponiveis()
            print_mac_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra mac\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_mac_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_mac:
                        note_selecionado = codigo_de_barras_mac.get(codigo_escaneado)
                        if note_selecionado in mac_disponiveis_dicionario:
                            mac_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou mac\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            mac_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/mac_disponiveis_dicionario", 'w') as f:
                                json.dump(mac_disponiveis_dicionario, f)
                            with open("eventos/mac_evento_dicionario", 'w') as f:
                                json.dump(mac_evento_dicionario, f)
                            cls()
                            print_mac_disponiveis()
                            print_mac_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_mac()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    mac()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            mac()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        mac()


def retorno_mac():
    cls()
    print_mac_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_mac:
        note_selecionado = codigo_de_barras_mac.get(codigo_escaneado)
        if note_selecionado in mac_evento_dicionario:
            mac_evento_dicionario.pop(note_selecionado)
            mac_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/mac_evento_dicionario", 'w') as f:
                json.dump(mac_evento_dicionario, f)
            with open("disponiveis/mac_disponiveis_dicionario", 'w') as f:
                json.dump(mac_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou mac\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_mac_disponiveis()
            print_mac_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra mac\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_mac()
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
            mac()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        mac()


### ↑ Funções mac ↑ ###


### ↓ Escolhas distribuidor_hdmi ↓ ###
def distribuidor_hdmi():
    escolha = input(
        '\ndistribuidor_hdmi: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_distribuidor_hdmi()
    elif escolha == "2":
        retorno_distribuidor_hdmi()

    elif escolha == "3":
        cls()
        print_distribuidor_hdmi_disponiveis()
        print_distribuidor_hdmi_evento()
        distribuidor_hdmi()

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
        distribuidor_hdmi()


### ↑ Escolhas distribuidor_hdmi ↑ ###
### ↓ Funções distribuidor_hdmi ↓ ###

def retirar_distribuidor_hdmi():
    cls()
    print_distribuidor_hdmi_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_distribuidor_hdmi:
        note_selecionado = codigo_de_barras_distribuidor_hdmi.get(codigo_escaneado)
        if note_selecionado in distribuidor_hdmi_disponiveis_dicionario:
            distribuidor_hdmi_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou distribuidor_hdmi\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            distribuidor_hdmi_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/distribuidor_hdmi_disponiveis_dicionario", 'w') as f:
                json.dump(distribuidor_hdmi_disponiveis_dicionario, f)
            with open("eventos/distribuidor_hdmi_evento_dicionario", 'w') as f:
                json.dump(distribuidor_hdmi_evento_dicionario, f)
            cls()
            print_distribuidor_hdmi_disponiveis()
            print_distribuidor_hdmi_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra distribuidor_hdmi\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_distribuidor_hdmi_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_distribuidor_hdmi:
                        note_selecionado = codigo_de_barras_distribuidor_hdmi.get(codigo_escaneado)
                        if note_selecionado in distribuidor_hdmi_disponiveis_dicionario:
                            distribuidor_hdmi_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou distribuidor_hdmi\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            distribuidor_hdmi_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/distribuidor_hdmi_disponiveis_dicionario", 'w') as f:
                                json.dump(distribuidor_hdmi_disponiveis_dicionario, f)
                            with open("eventos/distribuidor_hdmi_evento_dicionario", 'w') as f:
                                json.dump(distribuidor_hdmi_evento_dicionario, f)
                            cls()
                            print_distribuidor_hdmi_disponiveis()
                            print_distribuidor_hdmi_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_distribuidor_hdmi()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    distribuidor_hdmi()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            distribuidor_hdmi()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        distribuidor_hdmi()


def retorno_distribuidor_hdmi():
    cls()
    print_distribuidor_hdmi_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_distribuidor_hdmi:
        note_selecionado = codigo_de_barras_distribuidor_hdmi.get(codigo_escaneado)
        if note_selecionado in distribuidor_hdmi_evento_dicionario:
            distribuidor_hdmi_evento_dicionario.pop(note_selecionado)
            distribuidor_hdmi_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/distribuidor_hdmi_evento_dicionario", 'w') as f:
                json.dump(distribuidor_hdmi_evento_dicionario, f)
            with open("disponiveis/distribuidor_hdmi_disponiveis_dicionario", 'w') as f:
                json.dump(distribuidor_hdmi_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou distribuidor_hdmi\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_distribuidor_hdmi_disponiveis()
            print_distribuidor_hdmi_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra distribuidor_hdmi\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_distribuidor_hdmi()
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
            distribuidor_hdmi()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        distribuidor_hdmi()


### ↑ Funções distribuidor_hdmi ↑ ###


### ↓ Escolhas ac800 ↓ ###
def ac800():
    escolha = input(
        '\nac800: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_ac800()
    elif escolha == "2":
        retorno_ac800()

    elif escolha == "3":
        cls()
        print_ac800_disponiveis()
        print_ac800_evento()
        ac800()

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
        ac800()


### ↑ Escolhas ac800 ↑ ###
### ↓ Funções ac800 ↓ ###

def retirar_ac800():
    cls()
    print_ac800_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_ac800:
        note_selecionado = codigo_de_barras_ac800.get(codigo_escaneado)
        if note_selecionado in ac800_disponiveis_dicionario:
            ac800_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou ac800\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            ac800_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/ac800_disponiveis_dicionario", 'w') as f:
                json.dump(ac800_disponiveis_dicionario, f)
            with open("eventos/ac800_evento_dicionario", 'w') as f:
                json.dump(ac800_evento_dicionario, f)
            cls()
            print_ac800_disponiveis()
            print_ac800_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra ac800\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_ac800_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_ac800:
                        note_selecionado = codigo_de_barras_ac800.get(codigo_escaneado)
                        if note_selecionado in ac800_disponiveis_dicionario:
                            ac800_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou ac800\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            ac800_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/ac800_disponiveis_dicionario", 'w') as f:
                                json.dump(ac800_disponiveis_dicionario, f)
                            with open("eventos/ac800_evento_dicionario", 'w') as f:
                                json.dump(ac800_evento_dicionario, f)
                            cls()
                            print_ac800_disponiveis()
                            print_ac800_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_ac800()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    ac800()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            ac800()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        ac800()


def retorno_ac800():
    cls()
    print_ac800_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_ac800:
        note_selecionado = codigo_de_barras_ac800.get(codigo_escaneado)
        if note_selecionado in ac800_evento_dicionario:
            ac800_evento_dicionario.pop(note_selecionado)
            ac800_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/ac800_evento_dicionario", 'w') as f:
                json.dump(ac800_evento_dicionario, f)
            with open("disponiveis/ac800_disponiveis_dicionario", 'w') as f:
                json.dump(ac800_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou ac800\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_ac800_disponiveis()
            print_ac800_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra ac800\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_ac800()
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
            ac800()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        ac800()


### ↑ Funções ac800 ↑ ###


### ↓ Escolhas caixa_de_som_pq ↓ ###
def caixa_de_som_pq():
    escolha = input(
        '\ncaixa_de_som_pq: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_caixa_de_som_pq()
    elif escolha == "2":
        retorno_caixa_de_som_pq()

    elif escolha == "3":
        cls()
        print_caixa_de_som_pq_disponiveis()
        print_caixa_de_som_pq_evento()
        caixa_de_som_pq()

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
        caixa_de_som_pq()


### ↑ Escolhas caixa_de_som_pq ↑ ###
### ↓ Funções caixa_de_som_pq ↓ ###

def retirar_caixa_de_som_pq():
    cls()
    print_caixa_de_som_pq_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_caixa_de_som_pq:
        note_selecionado = codigo_de_barras_caixa_de_som_pq.get(codigo_escaneado)
        if note_selecionado in caixa_de_som_pq_disponiveis_dicionario:
            caixa_de_som_pq_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou caixa_de_som_pq\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            caixa_de_som_pq_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/caixa_de_som_pq_disponiveis_dicionario", 'w') as f:
                json.dump(caixa_de_som_pq_disponiveis_dicionario, f)
            with open("eventos/caixa_de_som_pq_evento_dicionario", 'w') as f:
                json.dump(caixa_de_som_pq_evento_dicionario, f)
            cls()
            print_caixa_de_som_pq_disponiveis()
            print_caixa_de_som_pq_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra caixa_de_som_pq\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_caixa_de_som_pq_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_caixa_de_som_pq:
                        note_selecionado = codigo_de_barras_caixa_de_som_pq.get(codigo_escaneado)
                        if note_selecionado in caixa_de_som_pq_disponiveis_dicionario:
                            caixa_de_som_pq_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou caixa_de_som_pq\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            caixa_de_som_pq_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/caixa_de_som_pq_disponiveis_dicionario", 'w') as f:
                                json.dump(caixa_de_som_pq_disponiveis_dicionario, f)
                            with open("eventos/caixa_de_som_pq_evento_dicionario", 'w') as f:
                                json.dump(caixa_de_som_pq_evento_dicionario, f)
                            cls()
                            print_caixa_de_som_pq_disponiveis()
                            print_caixa_de_som_pq_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_caixa_de_som_pq()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    caixa_de_som_pq()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            caixa_de_som_pq()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        caixa_de_som_pq()


def retorno_caixa_de_som_pq():
    cls()
    print_caixa_de_som_pq_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_caixa_de_som_pq:
        note_selecionado = codigo_de_barras_caixa_de_som_pq.get(codigo_escaneado)
        if note_selecionado in caixa_de_som_pq_evento_dicionario:
            caixa_de_som_pq_evento_dicionario.pop(note_selecionado)
            caixa_de_som_pq_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/caixa_de_som_pq_evento_dicionario", 'w') as f:
                json.dump(caixa_de_som_pq_evento_dicionario, f)
            with open("disponiveis/caixa_de_som_pq_disponiveis_dicionario", 'w') as f:
                json.dump(caixa_de_som_pq_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou caixa_de_som_pq\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_caixa_de_som_pq_disponiveis()
            print_caixa_de_som_pq_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra caixa_de_som_pq\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_caixa_de_som_pq()
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
            caixa_de_som_pq()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        caixa_de_som_pq()


### ↑ Funções caixa_de_som_pq ↑ ###


### ↓ Escolhas caixa_de_som_g ↓ ###
def caixa_de_som_g():
    escolha = input(
        '\ncaixa_de_som_g: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_caixa_de_som_g()
    elif escolha == "2":
        retorno_caixa_de_som_g()

    elif escolha == "3":
        cls()
        print_caixa_de_som_g_disponiveis()
        print_caixa_de_som_g_evento()
        caixa_de_som_g()

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
        caixa_de_som_g()


### ↑ Escolhas caixa_de_som_g ↑ ###
### ↓ Funções caixa_de_som_g ↓ ###

def retirar_caixa_de_som_g():
    cls()
    print_caixa_de_som_g_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_caixa_de_som_g:
        note_selecionado = codigo_de_barras_caixa_de_som_g.get(codigo_escaneado)
        if note_selecionado in caixa_de_som_g_disponiveis_dicionario:
            caixa_de_som_g_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou caixa_de_som_g\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            caixa_de_som_g_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/caixa_de_som_g_disponiveis_dicionario", 'w') as f:
                json.dump(caixa_de_som_g_disponiveis_dicionario, f)
            with open("eventos/caixa_de_som_g_evento_dicionario", 'w') as f:
                json.dump(caixa_de_som_g_evento_dicionario, f)
            cls()
            print_caixa_de_som_g_disponiveis()
            print_caixa_de_som_g_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra caixa_de_som_g\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_caixa_de_som_g_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_caixa_de_som_g:
                        note_selecionado = codigo_de_barras_caixa_de_som_g.get(codigo_escaneado)
                        if note_selecionado in caixa_de_som_g_disponiveis_dicionario:
                            caixa_de_som_g_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou caixa_de_som_g\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            caixa_de_som_g_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/caixa_de_som_g_disponiveis_dicionario", 'w') as f:
                                json.dump(caixa_de_som_g_disponiveis_dicionario, f)
                            with open("eventos/caixa_de_som_g_evento_dicionario", 'w') as f:
                                json.dump(caixa_de_som_g_evento_dicionario, f)
                            cls()
                            print_caixa_de_som_g_disponiveis()
                            print_caixa_de_som_g_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_caixa_de_som_g()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    caixa_de_som_g()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            caixa_de_som_g()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        caixa_de_som_g()


def retorno_caixa_de_som_g():
    cls()
    print_caixa_de_som_g_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_caixa_de_som_g:
        note_selecionado = codigo_de_barras_caixa_de_som_g.get(codigo_escaneado)
        if note_selecionado in caixa_de_som_g_evento_dicionario:
            caixa_de_som_g_evento_dicionario.pop(note_selecionado)
            caixa_de_som_g_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/caixa_de_som_g_evento_dicionario", 'w') as f:
                json.dump(caixa_de_som_g_evento_dicionario, f)
            with open("disponiveis/caixa_de_som_g_disponiveis_dicionario", 'w') as f:
                json.dump(caixa_de_som_g_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou caixa_de_som_g\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_caixa_de_som_g_disponiveis()
            print_caixa_de_som_g_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra caixa_de_som_g\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_caixa_de_som_g()
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
            caixa_de_som_g()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        caixa_de_som_g()


### ↑ Funções caixa_de_som_g ↑ ###


### ↓ Escolhas analog_way ↓ ###
def analog_way():
    escolha = input(
        '\nanalog_way: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_analog_way()
    elif escolha == "2":
        retorno_analog_way()

    elif escolha == "3":
        cls()
        print_analog_way_disponiveis()
        print_analog_way_evento()
        analog_way()

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
        analog_way()


### ↑ Escolhas analog_way ↑ ###
### ↓ Funções analog_way ↓ ###

def retirar_analog_way():
    cls()
    print_analog_way_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_analog_way:
        note_selecionado = codigo_de_barras_analog_way.get(codigo_escaneado)
        if note_selecionado in analog_way_disponiveis_dicionario:
            analog_way_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou analog_way\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            analog_way_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/analog_way_disponiveis_dicionario", 'w') as f:
                json.dump(analog_way_disponiveis_dicionario, f)
            with open("eventos/analog_way_evento_dicionario", 'w') as f:
                json.dump(analog_way_evento_dicionario, f)
            cls()
            print_analog_way_disponiveis()
            print_analog_way_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra analog_way\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_analog_way_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_analog_way:
                        note_selecionado = codigo_de_barras_analog_way.get(codigo_escaneado)
                        if note_selecionado in analog_way_disponiveis_dicionario:
                            analog_way_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou analog_way\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            analog_way_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/analog_way_disponiveis_dicionario", 'w') as f:
                                json.dump(analog_way_disponiveis_dicionario, f)
                            with open("eventos/analog_way_evento_dicionario", 'w') as f:
                                json.dump(analog_way_evento_dicionario, f)
                            cls()
                            print_analog_way_disponiveis()
                            print_analog_way_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_analog_way()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    analog_way()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            analog_way()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        analog_way()


def retorno_analog_way():
    cls()
    print_analog_way_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_analog_way:
        note_selecionado = codigo_de_barras_analog_way.get(codigo_escaneado)
        if note_selecionado in analog_way_evento_dicionario:
            analog_way_evento_dicionario.pop(note_selecionado)
            analog_way_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/analog_way_evento_dicionario", 'w') as f:
                json.dump(analog_way_evento_dicionario, f)
            with open("disponiveis/analog_way_disponiveis_dicionario", 'w') as f:
                json.dump(analog_way_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou analog_way\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_analog_way_disponiveis()
            print_analog_way_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra analog_way\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_analog_way()
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
            analog_way()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        analog_way()


### ↑ Funções analog_way ↑ ###


### ↓ Escolhas video_wall_4k ↓ ###
def video_wall_4k():
    escolha = input(
        '\nvideo_wall_4k: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_video_wall_4k()
    elif escolha == "2":
        retorno_video_wall_4k()

    elif escolha == "3":
        cls()
        print_video_wall_4k_disponiveis()
        print_video_wall_4k_evento()
        video_wall_4k()

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
        video_wall_4k()


### ↑ Escolhas video_wall_4k ↑ ###
### ↓ Funções video_wall_4k ↓ ###

def retirar_video_wall_4k():
    cls()
    print_video_wall_4k_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_video_wall_4k:
        note_selecionado = codigo_de_barras_video_wall_4k.get(codigo_escaneado)
        if note_selecionado in video_wall_4k_disponiveis_dicionario:
            video_wall_4k_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou video_wall_4k\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            video_wall_4k_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/video_wall_4k_disponiveis_dicionario", 'w') as f:
                json.dump(video_wall_4k_disponiveis_dicionario, f)
            with open("eventos/video_wall_4k_evento_dicionario", 'w') as f:
                json.dump(video_wall_4k_evento_dicionario, f)
            cls()
            print_video_wall_4k_disponiveis()
            print_video_wall_4k_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra video_wall_4k\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_video_wall_4k_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_video_wall_4k:
                        note_selecionado = codigo_de_barras_video_wall_4k.get(codigo_escaneado)
                        if note_selecionado in video_wall_4k_disponiveis_dicionario:
                            video_wall_4k_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou video_wall_4k\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            video_wall_4k_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/video_wall_4k_disponiveis_dicionario", 'w') as f:
                                json.dump(video_wall_4k_disponiveis_dicionario, f)
                            with open("eventos/video_wall_4k_evento_dicionario", 'w') as f:
                                json.dump(video_wall_4k_evento_dicionario, f)
                            cls()
                            print_video_wall_4k_disponiveis()
                            print_video_wall_4k_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_video_wall_4k()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    video_wall_4k()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            video_wall_4k()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        video_wall_4k()


def retorno_video_wall_4k():
    cls()
    print_video_wall_4k_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_video_wall_4k:
        note_selecionado = codigo_de_barras_video_wall_4k.get(codigo_escaneado)
        if note_selecionado in video_wall_4k_evento_dicionario:
            video_wall_4k_evento_dicionario.pop(note_selecionado)
            video_wall_4k_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/video_wall_4k_evento_dicionario", 'w') as f:
                json.dump(video_wall_4k_evento_dicionario, f)
            with open("disponiveis/video_wall_4k_disponiveis_dicionario", 'w') as f:
                json.dump(video_wall_4k_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou video_wall_4k\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_video_wall_4k_disponiveis()
            print_video_wall_4k_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra video_wall_4k\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_video_wall_4k()
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
            video_wall_4k()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        video_wall_4k()


### ↑ Funções video_wall_4k ↑ ###


### ↓ Escolhas Distribuidor HDMI ↓ ###
def distribuidor_hdmi():
    escolha = input(
        '\nDistribuidor HDMI: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_distribuidor_hdmi()
    elif escolha == "2":
        retorno_distribuidor_hdmi()

    elif escolha == "3":
        cls()
        print_distribuidor_hdmi_disponiveis()
        print_distribuidor_hdmi_evento()
        distribuidor_hdmi()

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
        distribuidor_hdmi()


### ↑ Escolhas Distribuidor HDMI ↑ ###
### ↓ Funções Distribuidor HDMI ↓ ###

def retirar_distribuidor_hdmi():
    cls()
    print_distribuidor_hdmi_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_distribuidor_hdmi:
        note_selecionado = codigo_de_barras_distribuidor_hdmi.get(codigo_escaneado)
        if note_selecionado in distribuidor_hdmi_disponiveis_dicionario:
            distribuidor_hdmi_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou Distribuidor HDMI\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            distribuidor_hdmi_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/distribuidor_hdmi_disponiveis_dicionario", 'w') as f:
                json.dump(distribuidor_hdmi_disponiveis_dicionario, f)
            with open("eventos/distribuidor_hdmi_evento_dicionario", 'w') as f:
                json.dump(distribuidor_hdmi_evento_dicionario, f)
            cls()
            print_distribuidor_hdmi_disponiveis()
            print_distribuidor_hdmi_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra Distribuidor HDMI\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_distribuidor_hdmi_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_distribuidor_hdmi:
                        note_selecionado = codigo_de_barras_distribuidor_hdmi.get(codigo_escaneado)
                        if note_selecionado in distribuidor_hdmi_disponiveis_dicionario:
                            distribuidor_hdmi_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou Distribuidor HDMI\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            distribuidor_hdmi_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/distribuidor_hdmi_disponiveis_dicionario", 'w') as f:
                                json.dump(distribuidor_hdmi_disponiveis_dicionario, f)
                            with open("eventos/distribuidor_hdmi_evento_dicionario", 'w') as f:
                                json.dump(distribuidor_hdmi_evento_dicionario, f)
                            cls()
                            print_distribuidor_hdmi_disponiveis()
                            print_distribuidor_hdmi_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_distribuidor_hdmi()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    distribuidor_hdmi()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            distribuidor_hdmi()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        distribuidor_hdmi()


def retorno_distribuidor_hdmi():
    cls()
    print_distribuidor_hdmi_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_distribuidor_hdmi:
        note_selecionado = codigo_de_barras_distribuidor_hdmi.get(codigo_escaneado)
        if note_selecionado in distribuidor_hdmi_evento_dicionario:
            distribuidor_hdmi_evento_dicionario.pop(note_selecionado)
            distribuidor_hdmi_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/distribuidor_hdmi_evento_dicionario", 'w') as f:
                json.dump(distribuidor_hdmi_evento_dicionario, f)
            with open("disponiveis/distribuidor_hdmi_disponiveis_dicionario", 'w') as f:
                json.dump(distribuidor_hdmi_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou Distribuidor HDMI\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_distribuidor_hdmi_disponiveis()
            print_distribuidor_hdmi_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra Distribuidor HDMI\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_distribuidor_hdmi()
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
            distribuidor_hdmi()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        distribuidor_hdmi()


### ↑ Funções Distribuidor HDMI ↑ ###


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
            with open("disponiveis/tv49_disponiveis_dicionario", 'w') as f:
                json.dump(tv49_disponiveis_dicionario, f)
            with open("eventos/tv49_evento_dicionario", 'w') as f:
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
                            with open("disponiveis/tv49_disponiveis_dicionario", 'w') as f:
                                json.dump(tv49_disponiveis_dicionario, f)
                            with open("eventos/tv49_evento_dicionario", 'w') as f:
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
            with open("eventos/tv49_evento_dicionario", 'w') as f:
                json.dump(tv49_evento_dicionario, f)
            with open("disponiveis/tv49_disponiveis_dicionario", 'w') as f:
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


### ↓ Escolhas LED 29 ↓ ###
def led29():
    escolha = input(
        '\nLED 29: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_led29()
    elif escolha == "2":
        retorno_led29()

    elif escolha == "3":
        cls()
        print_led29_disponiveis()
        print_led29_evento()
        led29()

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
        led29()


### ↑ Escolhas LED 29 ↑ ###
### ↓ Funções LED 29 ↓ ###

def retirar_led29():
    cls()
    print_led29_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_led29:
        note_selecionado = codigo_de_barras_led29.get(codigo_escaneado)
        if note_selecionado in led29_disponiveis_dicionario:
            led29_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou LED 29\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            led29_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/led29_disponiveis_dicionario", 'w') as f:
                json.dump(led29_disponiveis_dicionario, f)
            with open("eventos/led29_evento_dicionario", 'w') as f:
                json.dump(led29_evento_dicionario, f)
            cls()
            print_led29_disponiveis()
            print_led29_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra LED 29\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_led29_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_led29:
                        note_selecionado = codigo_de_barras_led29.get(codigo_escaneado)
                        if note_selecionado in led29_disponiveis_dicionario:
                            led29_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou LED 29\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            led29_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/led29_disponiveis_dicionario", 'w') as f:
                                json.dump(led29_disponiveis_dicionario, f)
                            with open("eventos/led29_evento_dicionario", 'w') as f:
                                json.dump(led29_evento_dicionario, f)
                            cls()
                            print_led29_disponiveis()
                            print_led29_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_led29()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    led29()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            led29()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        led29()


def retorno_led29():
    cls()
    print_led29_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_led29:
        note_selecionado = codigo_de_barras_led29.get(codigo_escaneado)
        if note_selecionado in led29_evento_dicionario:
            led29_evento_dicionario.pop(note_selecionado)
            led29_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/led29_evento_dicionario", 'w') as f:
                json.dump(led29_evento_dicionario, f)
            with open("disponiveis/led29_disponiveis_dicionario", 'w') as f:
                json.dump(led29_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou LED 29\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_led29_disponiveis()
            print_led29_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra LED 29\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_led29()
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
            led29()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        led29()


### ↑ Funções LED 29 ↑ ###


### ↓ Escolhas LED 30 ↓ ###
def led30():
    escolha = input(
        '\nLED 30: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_led30()
    elif escolha == "2":
        retorno_led30()

    elif escolha == "3":
        cls()
        print_led30_disponiveis()
        print_led30_evento()
        led30()

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
        led30()


### ↑ Escolhas LED 30 ↑ ###
### ↓ Funções LED 30 ↓ ###

def retirar_led30():
    cls()
    print_led30_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_led30:
        note_selecionado = codigo_de_barras_led30.get(codigo_escaneado)
        if note_selecionado in led30_disponiveis_dicionario:
            led30_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou LED 30\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            led30_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/led30_disponiveis_dicionario", 'w') as f:
                json.dump(led30_disponiveis_dicionario, f)
            with open("eventos/led30_evento_dicionario", 'w') as f:
                json.dump(led30_evento_dicionario, f)
            cls()
            print_led30_disponiveis()
            print_led30_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra LED 30\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_led30_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_led30:
                        note_selecionado = codigo_de_barras_led30.get(codigo_escaneado)
                        if note_selecionado in led30_disponiveis_dicionario:
                            led30_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou LED 30\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            led30_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/led30_disponiveis_dicionario", 'w') as f:
                                json.dump(led30_disponiveis_dicionario, f)
                            with open("eventos/led30_evento_dicionario", 'w') as f:
                                json.dump(led30_evento_dicionario, f)
                            cls()
                            print_led30_disponiveis()
                            print_led30_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_led30()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    led30()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            led30()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        led30()


def retorno_led30():
    cls()
    print_led30_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_led30:
        note_selecionado = codigo_de_barras_led30.get(codigo_escaneado)
        if note_selecionado in led30_evento_dicionario:
            led30_evento_dicionario.pop(note_selecionado)
            led30_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/led30_evento_dicionario", 'w') as f:
                json.dump(led30_evento_dicionario, f)
            with open("disponiveis/led30_disponiveis_dicionario", 'w') as f:
                json.dump(led30_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou LED 30\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_led30_disponiveis()
            print_led30_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra LED 30\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_led30()
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
            led30()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        led30()


### ↑ Funções LED 30 ↑ ###


### ↓ Escolhas LED 39 ↓ ###
def led39():
    escolha = input(
        '\nLED 39: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_led39()
    elif escolha == "2":
        retorno_led39()

    elif escolha == "3":
        cls()
        print_led39_disponiveis()
        print_led39_evento()
        led39()

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
        led39()


### ↑ Escolhas LED 39 ↑ ###
### ↓ Funções LED 39 ↓ ###

def retirar_led39():
    cls()
    print_led39_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_led39:
        note_selecionado = codigo_de_barras_led39.get(codigo_escaneado)
        if note_selecionado in led39_disponiveis_dicionario:
            led39_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou LED 39\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            led39_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/led39_disponiveis_dicionario", 'w') as f:
                json.dump(led39_disponiveis_dicionario, f)
            with open("eventos/led39_evento_dicionario", 'w') as f:
                json.dump(led39_evento_dicionario, f)
            cls()
            print_led39_disponiveis()
            print_led39_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra LED 39\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_led39_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_led39:
                        note_selecionado = codigo_de_barras_led39.get(codigo_escaneado)
                        if note_selecionado in led39_disponiveis_dicionario:
                            led39_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou LED 39\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            led39_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/led39_disponiveis_dicionario", 'w') as f:
                                json.dump(led39_disponiveis_dicionario, f)
                            with open("eventos/led39_evento_dicionario", 'w') as f:
                                json.dump(led39_evento_dicionario, f)
                            cls()
                            print_led39_disponiveis()
                            print_led39_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_led39()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    led39()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            led39()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        led39()


def retorno_led39():
    cls()
    print_led39_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_led39:
        note_selecionado = codigo_de_barras_led39.get(codigo_escaneado)
        if note_selecionado in led39_evento_dicionario:
            led39_evento_dicionario.pop(note_selecionado)
            led39_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/led39_evento_dicionario", 'w') as f:
                json.dump(led39_evento_dicionario, f)
            with open("disponiveis/led39_disponiveis_dicionario", 'w') as f:
                json.dump(led39_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou LED 39\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_led39_disponiveis()
            print_led39_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra LED 39\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_led39()
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
            led39()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        led39()


### ↑ Funções LED 39 ↑ ###


### ↓ Escolhas LED 26 ↓ ###
def led26():
    escolha = input(
        '\nLED 26: O que você gostaria de fazer, escolha o número da ação:\n \n[1] Retirar \n[2] Retorno \n[3] Checar estoque \n[4] Menu Principal \n[9] Sair \nPleno:')

    if escolha == "1":
        retirar_led26()
    elif escolha == "2":
        retorno_led26()

    elif escolha == "3":
        cls()
        print_led26_disponiveis()
        print_led26_evento()
        led26()

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
        led26()


### ↑ Escolhas LED 26 ↑ ###
### ↓ Funções LED 26 ↓ ###

def retirar_led26():
    cls()
    print_led26_disponiveis()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
    if codigo_escaneado in codigo_de_barras_led26:
        note_selecionado = codigo_de_barras_led26.get(codigo_escaneado)
        if note_selecionado in led26_disponiveis_dicionario:
            led26_disponiveis_dicionario.pop(note_selecionado)
            evento = 'Evento: ' + input("Nome do evento:")
            data = 'Retorna: ' + input("Data de retorno:")
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retirou LED 26\": {} | para o {} | ás {} |".format(id, note_selecionado, evento,
                                                                                    datetime.now(tz)))
            logs.close()
            led26_evento_dicionario[note_selecionado] = (evento, data)
            with open("disponiveis/led26_disponiveis_dicionario", 'w') as f:
                json.dump(led26_disponiveis_dicionario, f)
            with open("eventos/led26_evento_dicionario", 'w') as f:
                json.dump(led26_evento_dicionario, f)
            cls()
            print_led26_disponiveis()
            print_led26_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            def confirmar_retirada():
                confirmar = input(
                    '\nGostaria de retirar outra LED 26\"? \n[1] Mesmo evento \n[2] Diferente evento \n[3] Não \nPleno:')
                if confirmar == "1":
                    cls()
                    print_led26_disponiveis()
                    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retirar:")
                    if codigo_escaneado in codigo_de_barras_led26:
                        note_selecionado = codigo_de_barras_led26.get(codigo_escaneado)
                        if note_selecionado in led26_disponiveis_dicionario:
                            led26_disponiveis_dicionario.pop(note_selecionado)
                            logs = open("logs.txt", "a+")
                            logs.write(
                                "\nID: {} |Retirou LED 26\": {} | para o {} | ás {} |".format(id, note_selecionado,
                                                                                             evento, datetime.now(tz)))
                            logs.close()
                            led26_evento_dicionario[note_selecionado] = (evento, data)
                            with open("disponiveis/led26_disponiveis_dicionario", 'w') as f:
                                json.dump(led26_disponiveis_dicionario, f)
                            with open("eventos/led26_evento_dicionario", 'w') as f:
                                json.dump(led26_evento_dicionario, f)
                            cls()
                            print_led26_disponiveis()
                            print_led26_evento()
                            print("\n{} retirado com sucesso.".format(note_selecionado))
                            confirmar_retirada()
                    else:
                        print(colored("\nERROR: Código de barras escaneado inválido.", 'yellow'))
                        confirmar_retirada()
                elif confirmar == "2":
                    cls()
                    retirar_led26()
                elif confirmar == "3":
                    print("Ok, você será redirecionado para o inicio do programa.")
                    cls()
                    led26()
                else:
                    print(colored("\nERROR: Número da ação inválido.", 'yellow'))
                    confirmar_retirada()

            confirmar_retirada()
        else:
            print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
            led26()

    else:
        print(colored("\n ERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        led26()


def retorno_led26():
    cls()
    print_led26_evento()
    codigo_escaneado = getpass("\nEscaneie o código de barras que você deseja retornar:")
    if codigo_escaneado in codigo_de_barras_led26:
        note_selecionado = codigo_de_barras_led26.get(codigo_escaneado)
        if note_selecionado in led26_evento_dicionario:
            led26_evento_dicionario.pop(note_selecionado)
            led26_disponiveis_dicionario[note_selecionado] = 'Em estoque.'
            with open("eventos/led26_evento_dicionario", 'w') as f:
                json.dump(led26_evento_dicionario, f)
            with open("disponiveis/led26_disponiveis_dicionario", 'w') as f:
                json.dump(led26_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou LED 26\": {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_led26_disponiveis()
            print_led26_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            def confirmar_retorno():
                confirmar = input('\nGostaria de retornar outra LED 26\"? \n[1] Sim \n[2] Não \nPleno:')
                if confirmar == "1":
                    retorno_led26()
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
            led26()
    else:
        print(colored("\nERROR: Código de barras escaneado inválido ou não está em estoque.", 'yellow'))
        led26()


### ↑ Funções LED 26 ↑ ###


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
            with open("disponiveis/tv22_disponiveis_dicionario", 'w') as f:
                json.dump(tv22_disponiveis_dicionario, f)
            with open("eventos/tv22_evento_dicionario", 'w') as f:
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
                            with open("disponiveis/tv22_disponiveis_dicionario", 'w') as f:
                                json.dump(tv22_disponiveis_dicionario, f)
                            with open("eventos/tv22_evento_dicionario", 'w') as f:
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
            with open("eventos/tv22_evento_dicionario", 'w') as f:
                json.dump(tv22_evento_dicionario, f)
            with open("disponiveis/tv22_disponiveis_dicionario", 'w') as f:
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
            with open("disponiveis/tv28_disponiveis_dicionario", 'w') as f:
                json.dump(tv28_disponiveis_dicionario, f)
            with open("eventos/tv28_evento_dicionario", 'w') as f:
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
                            with open("disponiveis/tv28_disponiveis_dicionario", 'w') as f:
                                json.dump(tv28_disponiveis_dicionario, f)
                            with open("eventos/tv28_evento_dicionario", 'w') as f:
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
            with open("eventos/tv28_evento_dicionario", 'w') as f:
                json.dump(tv28_evento_dicionario, f)
            with open("disponiveis/tv28_disponiveis_dicionario", 'w') as f:
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
            with open("disponiveis/tv32_disponiveis_dicionario", 'w') as f:
                json.dump(tv32_disponiveis_dicionario, f)
            with open("eventos/tv32_evento_dicionario", 'w') as f:
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
                            with open("disponiveis/tv32_disponiveis_dicionario", 'w') as f:
                                json.dump(tv32_disponiveis_dicionario, f)
                            with open("eventos/tv32_evento_dicionario", 'w') as f:
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
            with open("eventos/tv32_evento_dicionario", 'w') as f:
                json.dump(tv32_evento_dicionario, f)
            with open("disponiveis/tv32_disponiveis_dicionario", 'w') as f:
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
            with open("disponiveis/tv55_disponiveis_dicionario", 'w') as f:
                json.dump(tv55_disponiveis_dicionario, f)
            with open("eventos/tv55_evento_dicionario", 'w') as f:
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
                            with open("disponiveis/tv55_disponiveis_dicionario", 'w') as f:
                                json.dump(tv55_disponiveis_dicionario, f)
                            with open("eventos/tv55_evento_dicionario", 'w') as f:
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
            with open("eventos/tv55_evento_dicionario", 'w') as f:
                json.dump(tv55_evento_dicionario, f)
            with open("disponiveis/tv55_disponiveis_dicionario", 'w') as f:
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
            with open("disponiveis/tv65_disponiveis_dicionario", 'w') as f:
                json.dump(tv65_disponiveis_dicionario, f)
            with open("eventos/tv65_evento_dicionario", 'w') as f:
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
                            with open("disponiveis/tv65_disponiveis_dicionario", 'w') as f:
                                json.dump(tv65_disponiveis_dicionario, f)
                            with open("eventos/tv65_evento_dicionario", 'w') as f:
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
            with open("eventos/tv65_evento_dicionario", 'w') as f:
                json.dump(tv65_evento_dicionario, f)
            with open("disponiveis/tv65_disponiveis_dicionario", 'w') as f:
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
            with open("disponiveis/tv72_disponiveis_dicionario", 'w') as f:
                json.dump(tv72_disponiveis_dicionario, f)
            with open("eventos/tv72_evento_dicionario", 'w') as f:
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
                            with open("disponiveis/tv72_disponiveis_dicionario", 'w') as f:
                                json.dump(tv72_disponiveis_dicionario, f)
                            with open("eventos/tv72_evento_dicionario", 'w') as f:
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
            with open("eventos/tv72_evento_dicionario", 'w') as f:
                json.dump(tv72_evento_dicionario, f)
            with open("disponiveis/tv72_disponiveis_dicionario", 'w') as f:
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
            with open("disponiveis/tv75_disponiveis_dicionario", 'w') as f:
                json.dump(tv75_disponiveis_dicionario, f)
            with open("eventos/tv75_evento_dicionario", 'w') as f:
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
                            with open("disponiveis/tv75_disponiveis_dicionario", 'w') as f:
                                json.dump(tv75_disponiveis_dicionario, f)
                            with open("eventos/tv75_evento_dicionario", 'w') as f:
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
            with open("eventos/tv75_evento_dicionario", 'w') as f:
                json.dump(tv75_evento_dicionario, f)
            with open("disponiveis/tv75_disponiveis_dicionario", 'w') as f:
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
            with open("disponiveis/tv84_disponiveis_dicionario", 'w') as f:
                json.dump(tv84_disponiveis_dicionario, f)
            with open("eventos/tv84_evento_dicionario", 'w') as f:
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
                            with open("disponiveis/tv84_disponiveis_dicionario", 'w') as f:
                                json.dump(tv84_disponiveis_dicionario, f)
                            with open("eventos/tv84_evento_dicionario", 'w') as f:
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
            with open("eventos/tv84_evento_dicionario", 'w') as f:
                json.dump(tv84_evento_dicionario, f)
            with open("disponiveis/tv84_disponiveis_dicionario", 'w') as f:
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
            with open("disponiveis/vw47_disponiveis_dicionario", 'w') as f:
                json.dump(vw47_disponiveis_dicionario, f)
            with open("eventos/vw47_evento_dicionario", 'w') as f:
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
                            with open("disponiveis/vw47_disponiveis_dicionario", 'w') as f:
                                json.dump(vw47_disponiveis_dicionario, f)
                            with open("eventos/vw47_evento_dicionario", 'w') as f:
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
            with open("eventos/vw47_evento_dicionario", 'w') as f:
                json.dump(vw47_evento_dicionario, f)
            with open("disponiveis/vw47_disponiveis_dicionario", 'w') as f:
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
            with open("disponiveis/vw55_disponiveis_dicionario", 'w') as f:
                json.dump(vw55_disponiveis_dicionario, f)
            with open("eventos/vw55_evento_dicionario", 'w') as f:
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
                            with open("disponiveis/vw55_disponiveis_dicionario", 'w') as f:
                                json.dump(vw55_disponiveis_dicionario, f)
                            with open("eventos/vw55_evento_dicionario", 'w') as f:
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
            with open("eventos/vw55_evento_dicionario", 'w') as f:
                json.dump(vw55_evento_dicionario, f)
            with open("disponiveis/vw55_disponiveis_dicionario", 'w') as f:
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
            with open("disponiveis/tv42_disponiveis_dicionario", 'w') as f:
                json.dump(tv42_disponiveis_dicionario, f)
            with open("eventos/tv42_evento_dicionario", 'w') as f:
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
                            with open("disponiveis/tv42_disponiveis_dicionario", 'w') as f:
                                json.dump(tv42_disponiveis_dicionario, f)
                            with open("eventos/tv42_evento_dicionario", 'w') as f:
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
            with open("eventos/tv42_evento_dicionario", 'w') as f:
                json.dump(tv42_evento_dicionario, f)
            with open("disponiveis/tv42_disponiveis_dicionario", 'w') as f:
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
            with open("disponiveis/tv43_disponiveis_dicionario", 'w') as f:
                json.dump(tv43_disponiveis_dicionario, f)
            with open("eventos/tv43_evento_dicionario", 'w') as f:
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
                            with open("disponiveis/tv43_disponiveis_dicionario", 'w') as f:
                                json.dump(tv43_disponiveis_dicionario, f)
                            with open("eventos/tv43_evento_dicionario", 'w') as f:
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
            with open("eventos/tv43_evento_dicionario", 'w') as f:
                json.dump(tv43_evento_dicionario, f)
            with open("disponiveis/tv43_disponiveis_dicionario", 'w') as f:
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
            with open("disponiveis/tv46_disponiveis_dicionario", 'w') as f:
                json.dump(tv46_disponiveis_dicionario, f)
            with open("eventos/tv46_evento_dicionario", 'w') as f:
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
                            with open("disponiveis/tv46_disponiveis_dicionario", 'w') as f:
                                json.dump(tv46_disponiveis_dicionario, f)
                            with open("eventos/tv46_evento_dicionario", 'w') as f:
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
            with open("eventos/tv46_evento_dicionario", 'w') as f:
                json.dump(tv46_evento_dicionario, f)
            with open("disponiveis/tv46_disponiveis_dicionario", 'w') as f:
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
            with open("disponiveis/notes_disponiveis_dicionario", 'w') as f:
                json.dump(notes_disponiveis_dicionario, f)
            with open("eventos/notes_evento_dicionario", 'w') as f:
                json.dump(notes_evento_dicionario, f)
            cls()
            print_notes_disponiveis()
            print_notes_evento()
            print("\n{} retirado com sucesso.".format(note_selecionado))

            planilha_note = note_selecionado[-2:]
            planilha_note_int = int(planilha_note)
            cell = planilha_note_int + 1
            fix_planilha_evento = evento.replace('Evento: ', "")
            fix_planilha_data = data.replace('Retorna: ', "")
            atualizar_evento = sheet.update_cell(cell, 6, fix_planilha_evento)
            atualizar_retorno = sheet.update_cell(cell, 8, fix_planilha_data)
            atualizar_total_disponiveis = sheet.update_cell(38, 2, str(len(notes_disponiveis_dicionario.keys())))
            atualizar_total_evento = sheet.update_cell(39, 2, str(len(notes_evento_dicionario.keys())))

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
                            with open("disponiveis/notes_disponiveis_dicionario", 'w') as f:
                                json.dump(notes_disponiveis_dicionario, f)
                            with open("eventos/notes_evento_dicionario", 'w') as f:
                                json.dump(notes_evento_dicionario, f)
                            cls()

                            planilha_note = note_selecionado[-2:]
                            planilha_note_int = int(planilha_note)
                            cell = planilha_note_int + 1
                            fix_planilha_evento = evento.replace('Evento: ', "")
                            fix_planilha_data = data.replace('Retorna: ', "")
                            atualizar_evento = sheet.update_cell(cell, 6, fix_planilha_evento)
                            atualizar_retorno = sheet.update_cell(cell, 8, fix_planilha_data)
                            atualizar_total_disponiveis = sheet.update_cell(38, 2, str(len(notes_disponiveis_dicionario.keys())))
                            atualizar_total_evento = sheet.update_cell(39, 2, str(len(notes_evento_dicionario.keys())))

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
            with open("eventos/notes_evento_dicionario", 'w') as f:
                json.dump(notes_evento_dicionario, f)
            with open("disponiveis/notes_disponiveis_dicionario", 'w') as f:
                json.dump(notes_disponiveis_dicionario, f)
            logs = open("logs.txt", "a+")
            logs.write("\nID: {} |Retornou o notebook: {} | ás {} |".format(id, note_selecionado, datetime.now(tz)))
            logs.close()
            cls()
            print_notes_disponiveis()
            print_notes_evento()
            print("\n{} retornado com sucesso.".format(note_selecionado))

            planilha_note = note_selecionado[-2:]
            planilha_note_int = int(planilha_note)
            cell = planilha_note_int + 1
            atualizar_evento = sheet.update_cell(cell, 6, "Na unidade")
            atualizar_retorno = sheet.update_cell(cell, 8, "")
            atualizar_total_disponiveis = sheet.update_cell(38, 2, str(len(notes_disponiveis_dicionario.keys())))
            atualizar_total_evento = sheet.update_cell(39, 2, str(len(notes_evento_dicionario.keys())))
            
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
