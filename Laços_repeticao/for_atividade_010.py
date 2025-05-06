dfrom time import sleep
import os
os.system('clear')  # LIMPANDO O TERMINAL

Email = 'c'
Senha = '1'
CONTADOR = 0
CONTADOR2 = 3

for i in range(CONTADOR2):
    loginU = input('Digite o login: ')
    senhaU = input('Digite a senha: ')


    if Email == loginU and Senha == senhaU:
        print('Bem vindo!')
        break
    else:
        print('Acesso negado.\n')
        CONTADOR += 1
        if i == 2:
            print('Numero de tentativas acima do permitido\n')
 