import os
import time
os.system('clear')  # LIMPANDO O TERMINAL
import os
from random import choice
from time import sleep 
os.system('clear')
Nota = 0

# SOLICITANDO DADOS


for i in range(4):
 numero = float(input('Digte sua nota: '))
 Nota += numero

os.system('clear')
print()

# MOSTRANDO DADOS

print('Calculando sua media...')
sleep(1)
os.system('clear')

media = Nota /4  # CALCULANDO A MEDIA FINAL

print(f'A sua media é {media}')
sleep(3)
print()
os.system('clear')


if media >= 7:
 print('Aprovado')
 print()
elif media <= 4:
 print('Reprovado')
 print()
else:
 print('Invalido')
 print()
 sleep(3)
 os.system('clear')
 
 print('Recarregue a pagina')
 print()
 sleep(3)
 os.system('clear')


print('Finalizando seção...')
print()
sleep(3)
os.system('clear')

print('Obrigado por utilizar o programa 3> ')
print()

# FIM DO PROGRAMA