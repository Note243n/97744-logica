import os
import time
os.system('clear')  # LIMPANDO O TERMINAL

print('Contagem pares')
for pares in range(100,121, 2):
 print(f'Numeros pares {pares}')
 time.sleep(0.5)

os.system('clear')


 # OUTRA FORMA DE FAZER 

print('Contagem de 100 até 120: ')
for i in range(100, 121):
 if i % 2 == 0:
  print(f'Numer: {i}')
  time.sleep(0.5)

