import os
from time import sleep
os.system('clear')  # LIMPANDO O TERMINAL


idade = int(input('Digite sua idade: '))


while idade < 18:
    print('Voce não pode proceguir, Somente maiores de 18.\n ')
    sleep(2)
    os.system('clear')  
    idade = int(input('Digite sua idade: '))

os.system('clear')  

print('Acesso permitido!')
sleep(1)
os.system('clear')  
print('Fim.')

sleep(5) # OUTRO PROGRAMA

os.system('clear')  # LIMPANDO O TERMINAL

while True:
    idade = int(input('Digite sua idade: '))

    os.system('clear')  # LIMPANDO O TERMINAL

    if idade < 18:
        print('Não autorizado')
        sleep(1)
        os.system('clear')  # LIMPANDO O TERMINAL
        sleep(1)
        print('Voce é menor idade')
        sleep(1)
        os.system('clear')  # LIMPANDO O TERMINAL
    else:
        break

print('Acesso permitido!')
sleep(1)
os.system('clear')
print('Fim')
print()



