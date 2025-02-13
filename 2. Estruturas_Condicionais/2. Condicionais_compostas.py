import os

os.system("Clear") # Limpar o trminal

# Solicitando dados

idade = int(input("Digite sua idade: "))

# Verificando (Processamento)

if idade < 18:
    print("Acesso negado!")
else:
    print("Acesso permitido!")

# Exibindo dados (saida)
print("== FIM ==")

