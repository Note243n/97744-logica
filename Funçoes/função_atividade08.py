import os
from time import sleep
os.system('clear || cls')
 
def somar(n1,n2,n3):
    calcular = n1 + n2 + n3
    return calcular

n1 = 5
n2 = 7
n3 = 10
soma = somar(n1, n2, n3)

print(f'A soma entre {n1} + {n2} + {n3} é {soma} !')
