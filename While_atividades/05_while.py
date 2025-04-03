from time import sleep
import os
os.system('clear')  # LIMPANDO O TERMINAL

QUANTIDADES_NOTAS = 5
soma = 0

for i in range(QUANTIDADES_NOTAS):
    while True:
        nota = float(input(f'Digite {i+1}ª nota: '))

        if nota < 0 or nota > 10:
            print('Nota invalida, tente novamente. \n')

        else:
            soma += nota
            break


media = soma / QUANTIDADES_NOTAS

print(f'Sua media é {media}')