import os
os.system("clear") # LImpeza do terminal

# Solicitando dados para o usuario

print("""
|  \t    Calendario            |
----------------------------------|
|1 | Janeiro \t|  | 7 | Julho    |
|2 | Fevereiro \t|  | 8 | Agosto   |
|3 | Março \t|  | 9 | Setembro |
|4 | Abril \t|  |10 | Outubro  |
|5 | Maio \t|  |11 | Novembro |
|6 | Junho\t|  |12 | Dezembro |
|=================================|
""")


Meses = str(input("Digite um numero correspondente ao Mes desejado -> "))

import os
os.system("clear")

# Exibindo dados

match Meses :
    case "1":
        print ("O mês é Janeiro")
    case "2":
        print ("O mês é Fevereiro")
    case "3":
        print ("O mês é Março")
    case "4":
        print ("O mês é Abril")
    case "5": 
        print ("O mês é Maio")
    case "6":
        print("O mês é Junho")
    case "7":
        print("O mês é Julho")
    case "8":
        print("O mês é Agosto")
    case "9":
        print("O mês é Setembro")
    case "10":
        print("O mês é Outubro")
    case "11":
        print("O mês é Novembro")
    case "12":
        print("O mês é Dezembro")
    case _:
        print("Invalido! ")
print()














