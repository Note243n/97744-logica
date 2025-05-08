import os
os.system('clear || cls')
from time import sleep
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float


pessoa1 = Pessoa(
    input('Digite seu nome: '),
    input('Digite sua idade: '),
    input('Digite seu peso: '),
    input('digite sua altura:')
    )



os.system('clear || cls')

print(f'Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nPeso: {pessoa1.peso}\nAltura: {pessoa1.altura}  ')
