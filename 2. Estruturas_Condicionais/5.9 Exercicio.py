import os
os.system("clear") # LImpeza do terminal

# Solicitando dados para o usuario
 
Valor = float(input("Informe o valor do produto desejado -> "))

Desconto = 0.1

print(""" 
 1 = Pagamento a vista
 2 = Pagamento a prazo
""")

Pagamento = str(input("Informe a forma de Pagamento -> "))
print()
# Exibindo dados 

match Pagamento :
    case "1":
        print(f"Valor do Produto {Valor}")
        print("Forma de pagamento -> A vista")
        Desconto = Valor * Desconto
        print(f"Desconto: {Desconto}")
        print(f"Total a pagar é {Valor - Desconto}")


    case "2":
        Parcelas = int(input("Informe a quantidade de Parcelas -> "))
        print(f"Valor do Produto {Valor}")
        print("Forma de pagamento -> A Prazo")
        print(f"Quantidade de parcelas {Parcelas}")
        
        
    case _:
        print("Invalido !")

print()














