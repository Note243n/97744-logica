import os 
os.system('clear || cls')         
Alimentos = []
Precos = []

def Cardapio():
  print('''
  1 | Picanha | 25,00
  2 | Lasanha | 20,00
  3 | Strogonoff | 18,00
  4 | Bife acebolado | 15,00
  5 | Pão com ovo | 5,00
  -------------------------------
  0 pra sair
  ''')

def Cardapio_Comando():
  while True:
    escolha = int(input(f'Digite o codigo do prato que deseja: '))
    print()
    if escolha == 0:
      os.system('clear || cls')
      for i in Alimentos:
        print(f'{i}')
        print()
      print(f'O valor total a pagar é de R$ {Cardapio_Calcular()}')
      exit()
    elif escolha == 1:
      Alimentos.append('Picanha\nValor: 25.00')
      Precos.append(25.00)
    elif escolha == 2:
      Alimentos.append('Lasanha\nValor: 20,00')
      Precos.append(20.00)
    elif escolha == 3:
      Alimentos.append('Strogonoff\nValor: 18,00')
      Precos.append(18.00)
    elif escolha == 4:
      Alimentos.append('Bife acebolado\nValor: 15,00')
      Precos.append(15.00)
    elif escolha == 5:
      Alimentos.append('Pão com ovo\nValor: 5,00')
      Precos.append(5.0)

def Cardapio_Calcular():
  soma = sum(Precos)
  return soma
  

Cardapio()

Cardapio_Comando()

Cardapio_Calcular()



