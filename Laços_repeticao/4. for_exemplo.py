import os
import time
os.system('clear')  # LIMPANDO O TERMINAL

print('Contagem de 2 em 2.')
for i in range(1,11, 2):
    print(f'Valor da variavel i: {i}')
    time.sleep(1) # ESPERA 1 SEGUNDO 

print('Fim da execuçao!')
