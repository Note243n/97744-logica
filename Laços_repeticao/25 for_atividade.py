import os

os.system("cls || clear")

Nome = input('digite seu nome: ')
nota = float(input('digite sua nota: '))

sequencia = 1
media = 1

while True:
   repetir = int(input('Deseja adicionar mais uma nota?\n(1) para sim\n (2) para não: '))
   if repetir == 1:
      sequencia += 1
      nota += float(input(f'Digite a sequencia {sequencia}ª nota '))
      media += 1
   else:
      break
   

print(f'Sua sequencia é {sequencia}')
print(f'Quantidades de notas encontradas {nota}')
print(f'Sua media é {nota / media}')
   
