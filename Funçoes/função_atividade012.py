import os
from time import sleep
os.system('clear || cls')


def contar_pares_impares():
    par = 0
    impar = 0

    for i in range(6):
        n1 = int(input('Digite um numero: '))
        if n1 % 2 == 0:
            par += 1
        else:
            impar += 1
    return par, impar
    
quantidade_pares, quantidade_impares = contar_pares_impares()

print(f'{quantidade_pares}')
print(f'{quantidade_impares}')
        
