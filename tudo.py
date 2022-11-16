from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

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

        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        with open('private_key.pem', 'wb') as f:
            f.write(pem)

        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        with open('public_key.pem', 'wb') as f:
            f.write(pem)

        print('Chave Gerada')
    if op== 2:
        print('fechando')
        break