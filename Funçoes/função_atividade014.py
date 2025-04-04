import os
from time import sleep
os.system('clear || cls')


def inflaciionamento(valor):
    if valor < 100:
        valor = n1 * 1.10
    elif valor >= 100:
        valor = n1 * 1.20
    return valor



n1 = int(input('digite seu numero pra aplicar a inflação: '))

valor = inflaciionamento(n1)
print(f'o valor com a tarifa aplicada é {valor:.2f}')
