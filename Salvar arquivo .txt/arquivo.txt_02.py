import os 
os.system('clear || cls')
from time import sleep
from dataclasses import dataclass

@dataclass
class Loja_carro:
    marca: str
    modelo: str 
    categoria: str
    preco: float


Lista_carros = []
QUANTIDADE_CLIENTE = 2

for i in range(QUANTIDADE_CLIENTE):
    loja_carro = Loja_carro(
        marca = input('Digite a marca do teu carro: '),
        modelo = input('Digite o modelo do teu carro: '),
        categoria = input('digite a categoria do teu carro: '),
        preco = input('Digite o preço do teu carro: ')
    )
    Lista_carros.append(loja_carro)
    print()


os.system('clear || cls')
print('\n__ Exibindo dados __\n')
for loja in Lista_carros:
    print(f'A marca do teu carro: {loja.marca} ')
    print(f'O modelo do teu carro: {loja.modelo} ')
    print(f'A categoria do teu carro: {loja.categoria} ')
    print(f'O preço do teu carro: {loja.preco} ')
    print("_" * 30)

nome_arquivo = "XRC_ROSA"

with open (nome_arquivo, "a") as arquivos:
    for Loja_carro in Lista_carros:
        arquivos.write(f'A marca do cliente é: {Loja_carro.marca}O modelo do cliente é: {Loja_carro.modelo}A categoria do clienteé: {loja_carro.categoria}O preço do cliente é: {loja_carro.preco}\n')