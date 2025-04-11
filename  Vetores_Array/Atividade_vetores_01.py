import os 
os.system('clear || cls')


lista_numeros = []

def Determinar_numeros(lista_numeros):
    print('Seus numeros')
    for i, l in enumerate (lista_numeros, start= 1):
        print(f'{i}ª {l}')
    print()
    Maior_numero = max(lista_numeros)
    Menor_numero = min(lista_numeros)
    return Maior_numero,Menor_numero


for i in range(5):
    n = int(input(f'Digite o seu {i + 1}ª numero: '))
    lista_numeros.append(n)
    os.system('clear || cls')

lista = Determinar_numeros(lista_numeros)



print(f"Maior numero: {lista[0]}\nMenor numero: {lista[1]}")
print()
