import os
from time import sleep
os.system('clear || cls')

def calcular_nota(Media):
   Media / 3
   return Media

for i in range(3):
   Media = 0
   nota = float(input(f'digite sua {i + 1} nota : '))
   Media += nota
   Media = calcular_nota(nota)

print(f'A sua media é {Media:.2f}')
