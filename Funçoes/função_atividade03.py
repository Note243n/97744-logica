import os
from time import sleep
os.system('clear || cls')


def logo_senai():
    sleep(0.5)
    os.system('clear || cls')
    print('=== SENAI ===')

logo_senai()
nome = input('Digite seu nome: ')


logo_senai()
idade = input('Digite sua idade: ')


logo_senai()
print(f'\nNome: {nome}')
print(f'Idade: {idade}')


