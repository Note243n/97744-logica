import os
import time
os.system('clear')  # LIMPANDO O TERMINAL
Nota = 0

# SOLICITANDO DADOS


for i in range(4):
 numero = float(input('Digte sua nota: '))
 Nota += numero

os.system('clear')
print()

# MOSTRANDO DADOS

print('Calculando sua media...')
time.sleep(1)
os.system('clear')

media = Nota /4  # CALCULANDO A MEDIA FINAL

print(f'A sua media é {media}')
time.sleep(3)
print()
os.system('clear')

print('Finalizando seção...')
time.sleep(1)
os.system('clear')

print('Obrigado por utilizar o programa 3> ')
print()

# FIM DO PROGRAMA