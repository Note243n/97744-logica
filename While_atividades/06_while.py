from time import sleep
import os
os.system('clear')  # LIMPANDO O TERMINAL

Email = 'carlos'
Senha = 'carlos123'


while True:
  EmailU = str(input('Informe o seu login (Email)\n -> ')).lower()
  SenhaU = str(input('Informe a sua senha \n -> ')).lower()
  if Email == EmailU and Senha == SenhaU:
    print('Bem vindo!')
    break
  else:
    print('Acesso negado!')

