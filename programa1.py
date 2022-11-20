from function.criptografia import *
from function.open_txt import open_txt
import pickle
import rsa
import time
def main():
    while True:
        print('--------- Menu --------------')
        print('selecione uma opção: ')
        print('1 - Gerar chave pública e privada!')
        print('2 - Descompactar arquivos! ')
        print('3 - Comparar o Hash! ')
        print('4 - Fechar Programa!')
        print('-----------------------------\n')

        op = int(input())

        if op == 1:
            generate_key()

            print('Chave Gerada')
        if op== 2:
          descompact_files()

          print('Arquivos descompactados!')

        if op==3:
          file = open_txt('files/file.txt')
          newhash = generate_hash(file)
          hash_encrypt = take_hash_encryption()
          private_key = take_private_key()
          oldhash = dencryption_algorithm(hash_encrypt, private_key)

          if compare_hashes(oldhash, newhash):
            print("Arquivo autênticado!")
          else:
            print("Arquivo não autênticado!")
        if op==4:
          print('Fechando...')
          time.sleep(2)
          break
if __name__== "__main__":
  main()