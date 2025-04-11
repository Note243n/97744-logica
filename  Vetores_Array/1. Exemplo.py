import os 
os.system('clear || cls')

# CRIANDO UMA LISTA.
Lista_de_compras = []
QUANTIDADE = 3

# SOLICITANDO DADOS PARA O USUARIO.
print('= LISTA DE COMPRAS =')
for i in range(QUANTIDADE):
    item = input('Digite um intem para a lista: ')
    Lista_de_compras.append(item)
    os.system('clear || cls')

# SAIDA DE DADOS

print('= LISTA DE COMPRAS =')
for lista in Lista_de_compras:
    print(lista)
print()
