import hashlib

from cryptography.hazmat.primitives import hashes,serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

# gerando as chaves
def generate_key():
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


#Pegando a chave publica
def take_public_key():
  with open('public_key.pem','rb') as key_file:
    public_key = serialization.load_pem_public_key(
      key_file.read(),
      backend=default_backend()
    )
    return public_key

#Gerando o hash
def generate_hash(arquivo):
  hash = hashlib.new('ripemd160')
  hash.update(arquivo.encode('utf-8'))
  hash = hash.hexdigest()
  return hash