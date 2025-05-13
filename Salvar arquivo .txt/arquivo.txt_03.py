import os 
os.system('clear || cls')
from time import sleep
import dataclasses
Lista_livros = []

class Ler_livro:
    def __init__(self, Nome, Autor, Categoria, Preco):
        self.Nome = Nome 
        self.Autor = Autor
        self.Categoria = Categoria
        self.Preco = Preco

    def Imprimir_resultados(self):
        print(f'O nome do teu livro é {self.Nome}')
        print(f'O nome do autor é {self.Autor}')
        print(f'O nome da categoria é {self.Categoria}')
        print(f'O preço do teu livro é {self.Preco}')



for i in range(3):
    Nome = input('Digite o nome do teu livro: ')
    Autor = input('Digite o Autor do teu livro: ')
    Categoria = input('Digite a categoria do teu livro: ')
    Preco = input('Digite o preço do teu livro: ')
    Lista_livros.append(Nome, Autor, Categoria, Preco)
    os.system('clear || cls')

Meu_livro = Ler_livro(Nome, Autor, Categoria, Preco)
Meu_livro.Imprimir_resultados()