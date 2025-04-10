import os
from time import sleep
os.system('clear || cls')

def Calcular_IMC(peso, altura):
    return peso / (altura * altura)

def classificar(imc):
    if imc < 18.5:
     print('Abaixo do peso\nConsulte um nutricionista para orientação')
    elif imc < 25:
     print('Peso normal\nMantenha habitos saudaveis!')
    elif imc < 29.9:
     print('Sobrepesso\nConsidere uma dieta balançeada e atividades fisicas')
    elif imc < 34.9:
     print('Obessidade grau 1\nProcure uma orientação de um profissional de saude')
    elif imc < 39.9:
     print('Obessidade grau 2\nConsulte um medico para avaliação e orientação')
    else:
     print('Obessidade 3\nBusque assistencia medica imediatamente')
     print()


peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
os.system('clear || cls')

imc = Calcular_IMC(peso, altura)
classificacao = classificar(imc)