import os
from time import sleep
os.system('clear || cls')
 


def transformador_n(numero):
    if numero % 2 == 0:
        print(f'Você digitou {numero}, é par')
    elif numero % 2 == 1:
        print(f'Voê digitou {numero}, é impar')


while True:
 try:
   numero_1 = int(input('Digite um numero: '))
   transformador_n(numero_1)

 except ValueError:
    print('Você digitou letras ou simbolos, tente novamente')
