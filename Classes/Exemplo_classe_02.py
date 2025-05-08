import os
os.system('clear || cls')
from time import sleep
from dataclasses import dataclass

@dataclass
class pessoa:
    nome: str
    idade: int

@dataclass
class pet:
    nome: str
    idade: int
    peso: float

pessoa1 = pessoa('Maria', 20)
pessoa2 = pessoa('Jose', 12)

pet1 = pet('TOTO', 6, 9.2)
pet2 = pet('tubarao', 6, 9.2)

print('Dados da pessoa')
print()
print(f'Nome: {pessoa1.nome}\nidade: {pessoa1.idade}')
print()
print(f'Nome: {pessoa2.nome}\nidade: {pessoa2.idade}')
print('\n')
print('Dados dos animais')
print()
print(f'Nome: {pet1.nome}\nidade: {pet1.idade}\nPeso: {pet1.peso}')
print()
print(f'Nome: {pet2.nome}\nidade: {pet2.idade}\npeso: {pet2.peso}')
print('\n')