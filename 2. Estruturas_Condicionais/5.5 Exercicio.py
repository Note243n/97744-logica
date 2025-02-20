import os
os.system("clear")

idade = int(input("Informe a sua idade: "))

if idade < 16 :
    print("Não pode votar")


elif idade == 16 or idade == 17:
    print("Voto opcional")




elif idade >= 18 and idade <= 65:
    print("Voce é obrigado a votar!")
else :
    print ("Não é obrigado a votar!")
















