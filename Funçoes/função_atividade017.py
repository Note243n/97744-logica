import os
from time import sleep
os.system('clear || cls')

def calcular_nota(Media):
   Media / 2
   return Media

for i in range(2):
   Media = 0
   nota = float(input(f'digite sua {i + 1} nota : '))
   Media += nota
   Media = calcular_nota(nota)

if Media >= 7:
   Resultado = 'Aprovado'
else:
   Resultado = 'Reprovado'

print(f'A sua media é {Media:.2f}')
print(f'{Resultado}')