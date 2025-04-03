from time import sleep
import os
os.system('clear')  # LIMPANDO O TERMINAL

nota = int(input('Digite sua nota : '))
os.system('clear')

while nota < 0  or nota > 10:
    print('Tente novamente')
    sleep(1)
    os.system('clear')
    nota = int(input('Digite sua nota: '))
    sleep(1)
    os.system('clear')

os.system('clear')

print(f'Sua nota é {nota}')
print()