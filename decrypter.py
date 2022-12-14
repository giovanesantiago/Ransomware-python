import os
import pyaes

## Abrir arquivo criptografado

file_name = input('Digite o diretorio/nome do arquivo : ')
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## Setando chave

key = b'testesansomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

### remover o arquivo criptografado 

os.remove(file_name)

## Criar um novo arquivo 

new_file = "arquivoSalvo." + input('Digite a extensão do arquivo (Ex: txt, doc ....) : ')
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()