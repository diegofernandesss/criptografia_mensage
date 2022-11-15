import rsa

while True:
    print('--------- Menu --------------')
    print('selecione uma opção: ')
    print('1 - Gerar chave pública e privada!')
    print('2 - Fechar Programa!')
    print('-----------------------------\n')

    op = int(input())

    if op == 1:
        #gerando chave privada
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        #gerando chave publica
        public_key = private_key.public_key()

        print('Chave Gerada')
    print("Chaves geradas.")
    if op== 2:
        print('fechando')
        break