import os
from time import sleep
os.system('clear || cls')
 
def somar(n1,n2,n3):
    calcular = n1 + n2 + n3
    return calcular

n1 = int(input('Digite seu primeiro numero: '))

n2 = int(input('Digite seu segundo numero: '))

n3 = int(input('Digite seu terceiro numero: '))

soma = somar(n1, n2, n3)

print(f'A soma entre {n1} + {n2} + {n3} é {soma} !')
