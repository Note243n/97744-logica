import os
from time import sleep
os.system('clear || cls')

def tabuada(numero):
    print('========= Tabuada =========')
    for i in range(1,11):
        print(f'A tabuada do numero {numero} X {i} = {i * numero} ')

numero_1 = int(input('Digite seu numero: '))
os.system('clear || cls')
tabuada(numero_1)
