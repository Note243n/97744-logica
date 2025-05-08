import os
os.system('clear || cls')
from time import sleep
from dataclasses import dataclass


@dataclass
class Endereco:
    logradouro: str 
    numero: int
    cidade: str


@dataclass
class login:
    nome: str
    email: str
    endereco: Endereco

    def Exbir_dados(self):
        print(f'Nome: {self.nome}\nemail: {self.email}\nEndereço: {self.endereco.logradouro}\nNumero: {self.endereco.numero}\nCidade: {self.endereco.cidade}')


input('Digite seu')