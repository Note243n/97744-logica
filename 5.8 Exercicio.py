import os
os.system("clear") # LImpeza do terminal

# Solicitando dados para o usuario

print("""
|====== Calendario =====|
|1 | Segunda-Feira \t|
|2 | Terça-Feira \t|
|3 | Quarta-Feira \t|
|4 | Quinta-Feira \t| \t <- Escolha a opçao desejada
|5 | Sexta-Feira \t|
|6 | Sabado  \t \t|
|7 | Domingo   \t \t|
|=======================| 
""")


Dia_Semana = str(input("Digite um numero correspondente ao dia da semana -> "))

import os
os.system("clear")

# Exibindo dados

match Dia_Semana :
    case "1":
        print ("Segunda-Feira -> Dia útil")
    case "2":
        print ("Terça-Feira -> Dia útil")
    case "3":
        print ("Quarta-Feira -> Dia útil")
    case "4":
        print ("Quinta-Feira -> Dia útil")
    case "5": 
        print ("Sexta-Feira -> Dia útil")
    case "6":
        print("Final de Semana")
    case "7":
        print("FInal de Semana")
    case _:
        print("Invalido! ")
print()














