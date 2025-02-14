import os
os.system("clear")

Numero_1 = float(input("Digite Sua primeira nota: "))
Numero_2 = float(input("Digite Sua segunda nota: "))
Numero_3 = float(input("Digite Sua terceira nota: "))


Media = (Numero_1 + Numero_2 + Numero_3) / 3




if Media < 7:
    print("Reprovado")
else:
    print("Aprovado!")


print()
print(f"Media:  {Media}")