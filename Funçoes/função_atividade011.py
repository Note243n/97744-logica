import os
from time import sleep
os.system('clear || cls')

# crie uma função que receba 2 numeros e mostre uma mensagem com a media destes dois numeros infomados.

 
def media(n1,n2):
    calcular = (n1 + n2) / 2
    return calcular


n1 = int(input('Digite seu primeiro numero: '))
n2 = int(input('Digite seu segundo numero: '))


mediaA = media(n1,n2)

print(f'A media é {mediaA}')

