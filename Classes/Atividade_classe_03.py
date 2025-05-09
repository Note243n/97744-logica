import os
os.system('clear || cls')
from time import sleep
from dataclasses import dataclass


@dataclass
class Endereco:
    def __init__(self, logradouro, numero, cidade):
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

    def mostrar_endereco(self):
        return f'Logradouro: {self.logradouro}\nNumero: {self.numero}\nCidade: {self.cidade}'


class Pessoa:
    def __init__(self, nome, email, endereco):
        self.nome = nome
        self.email = email
        self.endereco = endereco


    def mostrar_dados(self):
        print('\n__ dados Cadastrados __')
        print(f'Nome: {self.nome}')
        print(f'Email: {self.email}')
        print(self.endereco.mostrar_endereco())

print('\n __ Cadastrar de usuario __')
nome_user = input('Digite seu nome: ')
email_user = input('Digite seu email: ')



print('\n __ Endereço __')
logradouro_user = input('digite o logradouro (ex: rua, avenida):')
numero_user = input('Digite seu numero: ')
cidade_user = input('Digite sua cidade: ')


endereco_obj = Endereco(logradouro_user, numero_user, cidade_user)


pessoa_obj = Pessoa(nome_user, email_user, endereco_obj)

pessoa_obj.mostrar_dados()