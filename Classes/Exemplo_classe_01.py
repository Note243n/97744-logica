import os
os.system('clear || cls')
from time import sleep
from dataclasses import dataclass
@dataclass


class pessoa:
    nome: str
    idade: int

pessoa1 = pessoa('Alice', 30)
pessoa2 = pessoa('Bob', 25)

print(f'Nome: {pessoa1.nome}\nidade: {pessoa1.idade}')
print()
print(f'Nome: {pessoa2.nome}\nidade: {pessoa2.idade}')
print()