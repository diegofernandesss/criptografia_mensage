from function.criptografia import generate_key

def main():
    while True:
        print('--------- Menu --------------')
        print('selecione uma opção: ')
        print('1 - Gerar chave pública e privada!')
        print('2 - Fechar Programa!')
        print('-----------------------------\n')

        op = int(input())

        if op == 1:
            generate_key()

            print('Chave Gerada')
        if op== 2:
            print('fechando')
            break

if __name__== "__main__":
  main()