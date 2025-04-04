import os
from time import sleep
os.system('clear || cls')
 
def somar(n1,n2):
    calcular = n1 + n2
    return calcular



def subtrair(n1,n2):
    calcular = n1 - n2
    return calcular


def dividir(n1,n2):
    calcular = n1 / n2
    return calcular


def multiplicar(n1,n2):
    calcular = n1 * n2
    return calcular


n1 = int(input('Digite seu primeiro numero: '))
os.system('clear || cls')
n2 = int(input('Digite seu segundo numero: '))
os.system('clear || cls')


soma = somar(n1, n2)
print()
print(f'A soma entre {n1} + {n2} = {soma} ')


subtracao = subtrair(n1, n2)
print(f'A subtracao entre {n1} - {n2} = {subtracao} ')
print()


divisao = dividir(n1, n2)
print(f'A Divisão entre {n1} / {n2} = {divisao} ')
print()


multiplicacao = multiplicar(n1, n2)
print(f'A Multiplicação entre {n1} * {n2} = {multiplicacao} ')
print()

