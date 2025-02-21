import os
os.system("clear")
 
print("""
|========== Cardapio =========|\t\t Promoção só hoje !
|Código\tprato      \tValor | 
|1  \tPicanha    \t25,00 |
|2  \tLasanha  \t20,00 |
|3  \tStrogonoff  \t18,00 | 
|4  \tBife Acebolado \t15,00 |
|5  \tPão com ovo  \t5,00  |
|=============================|
""")
opcao = str(input("Digite o codigo do alimento -> "))

match opcao:
    case "1":
        print("Valor da Picanha 25,00")
    case "2":
        print("Valor da lasanha 20,00")
    case "3":
        print("Valor do Strogonoff 18,00")
    case "4":
        print("Valor do Bife Acebolado 15,00")
    case "5":
        print("Valor do Pão com ovo 5,0")
    case _:
        print("Opção invalida")













