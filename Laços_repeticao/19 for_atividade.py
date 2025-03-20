from time import sleep
import os
os.system('clear')  # LIMPANDO O TERMINAL

Email = 'carlos'
Senha = 'carlos123'
TENTATIVA = 3

for i in range(TENTATIVA):
 while True:
  EmailU = str(input('Informe o seu login (Email)\n -> ')).lower()
  SenhaU = str(input('Informe a sua senha \n -> ')).lower()
  os.system('clear')
  break

if Email == EmailU and Senha == SenhaU:
  print('Bem vindo!')

else:
 print('Acesso negado!')

print()