import os
import time
os.system('clear')  # LIMPANDO O TERMINAL

#  SOLICITANDO DADOS

n = int(input('Digite um numero inteiro: '))

# MOSTRANDO DADOS

for i in range(n, 0, -1):
    print(f'O anterior a {i} é ')
    time.sleep(1)
    print()

print('Fim da execuçao do programa')
time.sleep(1)
os.system('clear')


print('Obrigado por utilizar o meu programa')
print()
