import os 
os.system('Clear || cls')
from time import sleep
import dataclasses

# texto que você quer salvar
texto_para_salvar = "Texto de exemplo que será salvo no arquivo."

# abre o arquivo (ou cria se não existir) no modo de escrita ('w')
with open("meu_arquivo.txt", 'w') as arquivo:
    # escreve o texto no arquivo
    arquivo.write(texto_para_salvar)

print('O texto foi salvo com susseso no arquivo meu_arquivo.txt')
          

