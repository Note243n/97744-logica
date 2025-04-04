import os
os.system("clear")

N1 = float(input("Digite o seu primeiro numero: "))
N2 = float(input("Digite o seu segundo numero: "))





Media = (N1 + N2) /2
Soma = (N1 + N2)
Multiplicacao = (N1 * N2)



Maior_numero = max(N1, N2)
Menor_numero = min(N1, N2)

if N1 == N2:
    print(f"Os numeros são iguais")
else:
    print(f"Não são iguais")

if N1 < N2:
    Maior_numero = N1
    Menor_numero = N2
else:
    Menor_numero = N2
    Maior_numero = N1




print(f"Mèdia: {Media}")
print(f"Soma: {Soma}")
print(f"Multiplicaçao {Multiplicacao}")
print(f"Menor numero: {Menor_numero}")
print(f"Maior numero: {Maior_numero}")








