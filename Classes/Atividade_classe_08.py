import os 
os.system('clear || cls')
from dataclasses import dataclass
from time import sleep

lista_funcionario = []

@dataclass
class Funcionario:
    Nome: str
    Data_de_nacimento: str
    Cpf: int
    Funçao: str
    
    @staticmethod
    def Adicionar(lista):
        funcionario = Funcionario(
            Nome = input('Digite seu nome: '),
            Data_de_nacimento = input('Digite sua data de nascimento: '),
            Cpf = str(input('Digite seu CPF: ')),
            Funçao = input('Qual é a sua função? -: ')
        )
        lista_funcionario.append(funcionario)

    @staticmethod
    def Dados_cadastrados(lista):
        print(f'Componentes ate agora:\n\n{lista_funcionario}')

    @staticmethod
    def Atualizar(lista):
        Funcionario.Dados_cadastrados(lista)
        funcionario_antigo = input('Qual o nome que voce deseja atualizar? ')
        for funcionario in lista_funcionario:
            if funcionario.Nome == funcionario_antigo:
                funcionario.Nome = input('digite o nome do funcionario: ')
                funcionario.Data_de_nacimento = input('Qual a nova data: ')
                funcionario.Cpf = input('Digite o seu cpf: ')
                funcionario.Funçao = input('Digite a sua função: ')
            else:
                print('Não existe nenhum funcionario com esse nome')


    @staticmethod
    def Excluir(lista):
        Funcionario.Dados_cadastrados(lista)
        nome_para_excluir = input('Digite o nome do funcionário que deseja excluir: ')
        for funcionario in lista:
            if funcionario.Nome == nome_para_excluir:
                lista.remove(funcionario)
                print(f'Funcionário "{nome_para_excluir}" removido com sucesso.')
                break
        else:
            print('Funcionário não encontrado.')

    @staticmethod
    def Sair(lista):
        print('Saindo...')
        exit()



while True:
    print("= Cadastramento =")
    print("1 - Adicionar")
    print("2 - Dados Cadastrados")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("5 - Sair")
   
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
           Funcionario.Adicionar(lista_funcionario)
        case 2:
            Funcionario.Dados_cadastrados(lista_funcionario)
        case 3:
            Funcionario.Atualizar(lista_funcionario)
        case 4:
            Funcionario.Excluir(lista_funcionario)
        case 5:
            Funcionario.Sair(lista_funcionario)
