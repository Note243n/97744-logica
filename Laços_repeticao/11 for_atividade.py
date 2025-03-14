import os
import time
os.system('clear')  # LIMPANDO O TERMINAL
par = 0
impar = 0

for i in range(5):
 numero = int(input('Digte seu numero: '))
 if numero % 2 == 0 :
  par += 1
 else:
  impar += 1

print(f"{par} e {impar}")
