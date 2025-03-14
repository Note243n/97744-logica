import os
import time
os.system('clear')  # LIMPANDO O TERMINAL

# SOLICITANDO DADOS

print('== Conversor de numeros inteiros para numeros impares ==')
print()

# SAIDA

for impares in range(1,21,2):
  print(f'Numero: {impares} é impar ')
  time.sleep(0.4)
  print()

print('Obrigado por usar o conversor 3>')
print()

os.system('clear')  # LIMPANDO O TERMINAL

# FIM DO PRIMEIRO ALGORITMO

print('== Conversor de numeros inteiros para numeros impares ==')
print()

for impares in range(1,21):
  if impares % 2 == 1:
   print(f'Numero: {impares} é impar ')
   time.sleep(0.4)
   print()

print('Obrigado por usar o conversor 3>')
print()

# FIM DO SEGUNDO ALGORITMO
