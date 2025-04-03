import os
from time import sleep
os.system('clear || cls')
 


def transformador_n(numero):
     
    if numero > 0:
        print(f'O numero {numero} é posiitivo')
        sleep(2)
        os.system('clear || cls')
    elif numero < 0:
        print(f'O numero {numero} é negativo')
        sleep(2)
        os.system('clear || cls')
    elif numero == 0:
       print('0 é neutro')
       os.system('clear || cls')
       sleep(2)


while True:
    try:
     numero1 = int(input('Digite seu numero ou (S pra sair) ->  '))
     os.system('clear || cls')
     transformador_n(numero1)


    except ValueError:
       os.system('clear || cls')
       print('Você digitou letras ou simbolos, tente novamente. ')
       sleep(1)
       os.system('clear || cls')
