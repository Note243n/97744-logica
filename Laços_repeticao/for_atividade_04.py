import os
import time
os.system('clear')  # LIMPANDO O TERMINAL

# SOLICITANDO DADOS

n1 = int(input('digite o numero que deseja saber a tabuada: '))
print()

# MOSTRANDO DADOS

for tabuada in range(1,11):
    multi = n1 * tabuada
    print(f'{n1} x {tabuada} = {multi} ')
    time.sleep(0.4)
    print()

print('Fim da execuçao, Obrigado por utilizar nosso programa 3>')
print()

# FIM DO ALGORITIMO