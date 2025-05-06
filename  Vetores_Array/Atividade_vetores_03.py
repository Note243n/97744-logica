import os 
os.system('clear || cls')   
Numeros_armazenados = []

def Armazenar_valor():
  for i in range(5):
    valor = int(input('Digite um valor: '))
    Numeros_armazenados.append(valor)
  return Numeros_armazenados

def Lista_valores(Numeros_armazenados):
  os.system('clear || cls')   
  print('Valores do vetor: ')
  for lista in Numeros_armazenados:
    if lista < 0:
      lista = 0
    print(f'item: {lista}')

vetor = Armazenar_valor()
Lista_valores(vetor)
print()
