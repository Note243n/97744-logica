from time import sleep
import os
os.system('clear')  # LIMPANDO O TERMINAL

nota = int(input('Digite sua nota : '))
nota2 = int(input('Digite sua segunda nota : '))
os.system('clear')

while nota < 0  or nota > 10 or nota2 < 0 or nota2 > 10:
    print('Tente novamente')
    sleep(1)
    os.system('clear')
    nota = int(input('Digite sua nota: '))
    nota2 = int(input('Digite sua segunda nota : '))
    sleep(1)
    os.system('clear')

os.system('clear')



print(f'A sua nota é {nota}\nA soma das suas notas são {nota + nota2}\nA sua media é { (nota + nota2) /2}')
print()
