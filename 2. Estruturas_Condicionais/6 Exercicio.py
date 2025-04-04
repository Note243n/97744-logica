import os
os.system("clear")

N1 = float(input("Digite o seu primeiro numero: "))
N2 = float(input("Digite o seu segundo numero: "))


if N1 == N2:
    print(f"Os numeros são iguais")
else:
    print("Não são iguais")



Media = (N1 + N2) /2
Soma = (N1 + N2)
Multiplicacao = (N1 * N2)

print(f"Mèdia: {Media}")
print(f"Soma: {Soma}")
print(f"Multiplicaçao {Multiplicacao}")





if N1 < N2:
    print(f"O maior numero é {N2}")
elif N2 < N1:
    print(f"O maior numero é {N1}")


if N1 > N2:
    print(f"O menor numero é {N2}")
elif N2 > N1:
    print(f"O menor numero é {N1}")





