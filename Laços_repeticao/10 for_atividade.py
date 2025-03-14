import os
import time
os.system('clear')  # LIMPANDO O TERMINAL

soma = 0

for i in range(1,6):
    numero = int(input('Digite um numero: '))
    soma += numero


print(f'Soma é {soma}')