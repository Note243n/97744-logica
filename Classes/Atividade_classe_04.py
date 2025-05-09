import os
os.system('clear || cls')
from time import sleep
from dataclasses import dataclass


@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor
    

    def Exibir_detalhes(self):
        print(f'Titulo: {self.titulo}\nAno: {self.ano}\nNome do autor: {self.autor.nome} Biografia: {self.autor.biografia}')

instancia_Autor = Autor(
    nome = input('Qual o nome do autor? (Você): '),
    biografia = input('Qual a biografia: ')
)

Instancia_livro = Livro(
    titulo = input('digite o titulo do livro: '),
    ano = input('digite o ano do livro: '),
    autor = instancia_Autor
)
Instancia_livro.Exibir_detalhes()


