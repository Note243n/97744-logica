import os 
os.system('clear || cls')

# CRIANDO UMA LISTA.
Lista_de_compras = []
QUANTIDADE = 3

# SOLICITANDO DADOS PARA O USUARIO.
print('= LISTA DE COMPRAS =')
for i in range(QUANTIDADE):
    item = input(f'Digite o {i + 1}ª intem para a lista: ')
    Lista_de_compras.append(item)
    os.system('clear || cls')

# SAIDA DE DADOS

print('= LISTA DE COMPRAS =')
for i, lista in enumerate(Lista_de_compras, start = 1):
    print(f'{i}ª item:{lista}')
print()
