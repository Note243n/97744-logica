import os
os.system('clear || cls')
from time import sleep
from dataclasses import dataclass

@dataclass
class Endereco:
    Lougadoro : str
    numero : int

@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco

    def exibir_dados(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nEndereço: {self.endereco.Lougadoro}, numero: {self.endereco.numero}")

endereco1 = Endereco('rua A', 23)
pessoa1 = Pessoa("marta", 44, endereco1)
pessoa1.exibir_dados()
print()
Endereco2 = Endereco('Rua B', 47)
pessoa2 = Pessoa('claudia', 84, Endereco2)
pessoa2.exibir_dados()
