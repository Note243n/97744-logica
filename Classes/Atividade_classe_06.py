import os 
os.system('clear || cls')
from time import sleep



Lista_livros = []
QUANTIDADES_LIVROS = 3


class Ler_livro:
    def __init__(self, Nome, Autor, Categoria, Preco):
        self.Nome = Nome 
        self.Autor = Autor
        self.Categoria = Categoria
        self.Preco = Preco

    def Imprimir_resultados():
        for livro in Lista_livros:
            print(f'O nome do teu livro é {livro.Nome}')
            print(f'O nome do autor é {livro.Autor}')
            print(f'O nome da categoria é {livro.Categoria}')
            print(f'O preço do teu livro é {livro.Preco}')
            print('---------------------------------------')


for i in range(QUANTIDADES_LIVROS):
    meus_livros = Ler_livro(
        Nome = input('Digite o nome do teu livro: '),
        Autor = input('Digite o Autor do teu livro: '),
        Categoria = input('Digite a categoria do teu livro: '),
        Preco = input('Digite o preço do teu livro: ')
    )
    Lista_livros.append(meus_livros)
    os.system('clear || cls')


nome_arquivo = 'livro_txt'
print('Salvando')
with open(nome_arquivo, 'a') as arquivo:
    for livro in Lista_livros:
        arquivo.write(f'O nome do teu livro é {livro.Nome}\n')
        arquivo.write(f'O nome do autor é {livro.Autor}\n')
        arquivo.write(f'O nome da categoria é {livro.Categoria}\n')
        arquivo.write(f'O preço do teu livro é {livro.Preco}\n')
        arquivo.write('---------------------------------------\n')

try:
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linha.strip())
except FileNotFoundError:
    print(f'Arquivo {nome_arquivo} não encontrado.')
Ler_livro.Imprimir_resultados()

