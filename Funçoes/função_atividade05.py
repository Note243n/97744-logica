import os
from time import sleep
os.system('clear || cls')

def transformador_n(numero):
    if numero % 2 == 0:
        print('é par')
    else:
        print('é impar')

numero_1 = int(input('Digite um numero: '))
transformador_n(numero_1)
