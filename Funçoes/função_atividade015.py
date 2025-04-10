import os
from time import sleep
from datetime import date
os.system('clear || cls')


def conversor_idade(idade):
    return date.today().year - idade



ano = float(input('Digite o ano do seu nacimento: '))

idade = conversor_idade(ano)

print(f'Você tem {idade:.0f} anos ')

