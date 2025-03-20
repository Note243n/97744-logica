from time import sleep
import os
os.system('clear')  # LIMPANDO O TERMINAL

QUANTIDADE_NOTAS = 3
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
     nota = float(input(f'Digite a {i + 1}ª nota:'))
                     
     if nota < 0 or nota > 10:
        print('Nota invalida')
    else