import os
from time import sleep
os.system('clear || cls')

def Calcular_IMC():
    peso = int(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    imc_final = peso / (altura * altura)
    return imc_final

result_imc = Calcular_IMC()
os.system('clear || cls')

print(f'Peso: {result_imc:.2f}')
print()

if result_imc < 18.5:
    print('Abaixo do peso\nConsulte um nutricionista para orientação')
elif result_imc < 25:
    print('Peso normal\nMantenha habitos saudaveis!')
elif result_imc < 29.9:
    print('Sobrepesso\nConsidere uma dieta balançeada e atividades fisicas')
elif result_imc < 34.9:
    print('Obessidade grau 1\nProcure uma orientação de um profissional de saude')
elif result_imc < 39.9:
    print('Obessidade grau 2\nConsulte um medico para avaliação e orientação')
else:
    print('Obessidade 3\nBusque assistencia medica imediatamente')
print()

sleep(3)
os.system('clear || cls')
print('Obrigado por utilizar nosso sistema <3')

