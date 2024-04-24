# main.py
from utils import *

usuarios_cadastrados = {
        'adm': 'adm'
        }

lanches = {
    '': 0.0
}

# Exemplo de uso da função fazer_login()
print('Olá! Bem-vindo ao sistema Barriga Lanches!')
login(usuarios_cadastrados)
menu(lanches)